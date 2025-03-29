import asyncio
import cowsay
import shlex

clients = {}  # Словарь для хранения подключенных пользователей
games = {}    # Словарь для хранения игровых сессий

class MUD:
    def __init__(self, username):
        self.field = [[None for _ in range(10)] for _ in range(10)]
        self.player_position = (0, 0)
        self.weapons = {"sword": 10, "spear": 15, "axe": 20}
        self.username = username
        self.monsters = set()  # Добавляем множество для отслеживания существующих монстров
        self.jgsbat_func = None
        try:
            with open("jgsbat.cow", "r", encoding="utf-8") as f:
                jgsbat_template = cowsay.read_dot_cow(f)
                self.jgsbat_func = lambda msg: cowsay.cowsay(msg, cowfile=jgsbat_template)
        except Exception as e:
            print(f"Ошибка загрузки монстра jgsbat: {e}")

    def move_player(self, d_x, d_y):
        x, y = self.player_position
        x = (x + d_x) % 10
        y = (y + d_y) % 10
        self.player_position = (x, y)
        return f"{x} {y}"

    def encounter(self, x, y):
        monster = self.field[x][y]
        if monster:
            name, hello, _ = monster
            if name == "jgsbat" and self.jgsbat_func:
                return self.jgsbat_func(hello)
            return cowsay.cowsay(hello, cow=name)
        return ''

    def moving(self, d_x, d_y):
        new_position = self.move_player(d_x, d_y)
        encounter_message = self.encounter(self.player_position[0], self.player_position[1])
        if encounter_message:
            return f"Moved to ({new_position})\n{encounter_message}"
        return f"Moved to ({new_position})"

    def add_monster(self, x, y, hp, hello, name):
        if name not in cowsay.list_cows() and name != "jgsbat":
            return "cannot add unknown monster"
        if (x, y) == self.player_position:
            return "cannot add monster to player's position"

        old_mon = self.field[x][y] is not None
        self.field[x][y] = (name, hello, hp)
        self.monsters.add(name)  # Добавляем монстра в множество
        return "1" if old_mon else "0"

    def attack(self, weapon, name):
        if name not in self.monsters:  # Проверяем, существует ли вообще такой монстр
            return f'no such monster {name}'
        x, y = self.player_position
        monster = self.field[x][y]
        if not monster or monster[0] != name:
            return f'no {name} here'  # Монстр существует, но не в этой клетке
        name, hello, hp = monster
        damage = min(self.weapons[weapon], hp)
        hp -= damage
        if hp <= 0:
            self.field[x][y] = None
            self.monsters.remove(name)  # Удаляем монстра из множества при его смерти
            return f'{damage} 0'
        self.field[x][y] = (name, hello, hp)
        return f'{damage} {hp}'

async def broadcast_message(message, exclude=None):
    for username, queue in clients.items():
        if username != exclude:
            await queue.put(message)

async def handle_client(reader, writer):
    username = (await reader.readline()).decode().strip()

    if username in clients:
        writer.write(b"Username already taken\n")
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        return

    clients[username] = asyncio.Queue()
    games[username] = MUD(username)

    writer.write(b"Welcome to MUD!\n")
    await writer.drain()

    await broadcast_message(f"{username} has joined the game")
    print(f"{username} connected")

    send_task = asyncio.create_task(send_messages(writer, username))

    try:
        while not reader.at_eof():
            data = await reader.readline()
            if not data:
                break

            message = data.decode().strip()
            parts = message.split()
            if not parts:
                continue

            cmd = parts[0]
            game = games[username]

            if cmd == "addmon":
                name, x, y, hp = parts[1:5]
                hello = ' '.join(parts[5:])
                response = game.add_monster(int(x), int(y), int(hp), hello, name)

                if response == "cannot add unknown monster":
                    await clients[username].put(response)
                elif response == "cannot add monster to player's position":
                    await clients[username].put("cannot add the monster in player's position")
                else:
                    await broadcast_message(f"{username} added monster {name} to ({x}, {y}) with {hp} hp")

            elif cmd == "attack":
                weapon, name = parts[1:3]
                response = game.attack(weapon, name)
                if response.startswith('no'):
                    await clients[username].put(response)
                else:
                    damage, hp = map(int, response.split())
                    if hp == 0:
                        await broadcast_message(f"{username} attacked {name} with {weapon} for {damage} hp, {name} died")
                    else:
                        await broadcast_message(f"{username} attacked {name} with {weapon} for {damage} hp, {name} has {hp} hp left")

            elif cmd == "move":
                d_x, d_y = map(int, parts[1:3])
                response = game.moving(d_x, d_y)
                await clients[username].put(response)

            else:
                await clients[username].put("Unknown command")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        send_task.cancel()
        try:
            await send_task
        except asyncio.CancelledError:
            pass

        if username in clients:
            del clients[username]
        if username in games:
            del games[username]

        await broadcast_message(f"{username} has left the game")

        writer.close()
        await writer.wait_closed()
        print(f"{username} disconnected")

async def send_messages(writer, username):
    try:
        while True:
            message = await clients[username].get()
            writer.write(message.encode() + b'\n')
            await writer.drain()
    except asyncio.CancelledError:
        pass

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())

