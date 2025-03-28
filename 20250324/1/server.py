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
            return f"{new_position}\n{encounter_message}"
        return new_position

    def add_monster(self, x, y, hp, hello, name):
        if name not in cowsay.list_cows() and name != "jgsbat":
            return "cannot add unknown monster"
        if (x, y) == self.player_position:
            return "cannot add monster to player's position"

        old_mon = self.field[x][y] is not None
        self.field[x][y] = (name, hello, hp)
        return "1" if old_mon else "0"

    def attack(self, weapon, name):
        x, y = self.player_position
        monster = self.field[x][y]
        if not monster or monster[0] != name:
            return 'no'
        name, hello, hp = monster
        damage = min(self.weapons[weapon], hp)
        hp -= damage
        if hp <= 0:
            self.field[x][y] = None
            return f'{damage} 0'
        self.field[x][y] = (name, hello, hp)
        return f'{damage} {hp}'

async def handle_client(reader, writer):
    username = (await reader.readline()).decode().strip()

    # Проверяем, что имя уникально
    if username in clients:
        writer.write(b"Username already taken\n")
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        return  # Просто выходим, не затрагивая старого клиента

    try:
        # Регистрируем нового пользователя
        clients[username] = asyncio.Queue()
        games[username] = MUD(username)
        writer.write(b"Welcome to MUD!\n")
        await writer.drain()

        print(f"{username} connected")

        # Основной цикл обработки команд
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
            elif cmd == "attack":
                weapon, name = parts[1:3]
                response = game.attack(weapon, name)
            elif cmd == "move":
                d_x, d_y = map(int, parts[1:3])
                response = game.moving(d_x, d_y)
            else:
                response = "Unknown command"

            writer.write(response.encode() + b'\n')
            await writer.drain()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Удаляем только если клиент действительно был в игре
        if username in clients:
            del clients[username]
        if username in games:
            del games[username]

        writer.close()
        await writer.wait_closed()
        print(f"{username} disconnected")


async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())

