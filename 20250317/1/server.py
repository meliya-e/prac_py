import socket
import shlex
import cowsay

class MUDServer:
    weapons = {"sword": 10, "spear": 15, "axe": 20}

    def __init__(self, host="localhost", port=12345):
        self.host = host
        self.port = port
        self.field = [[None for _ in range(10)] for _ in range(10)]
        self.player_position = (0, 0)

    def start(self):
        """Запуск сервера"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            print(f"Сервер запущен на {self.host}:{self.port}")

            while True:
                conn, addr = server_socket.accept()
                with conn:
                    print(f"Новое подключение: {addr}")
                    while True:
                        data = conn.recv(1024).decode().strip()
                        if not data:
                            break
                        response = self.handle_command(data)
                        conn.sendall(response.encode())

    def handle_command(self, command):
        """Обрабатывает команду, полученную от клиента"""
        parts = shlex.split(command)
        if not parts:
            return "Empty command"

        cmd = parts[0]

        if cmd in ["up", "down", "left", "right"]:
            return self.move_player(cmd)
        elif cmd == "attack":
            return self.attack(parts[1:])
        elif cmd == "addmon":
            return self.addmon(parts[1:])
        return "Unknown command"

    def move_player(self, direction):
        """Двигает игрока и проверяет встречу с монстром"""
        x, y = self.player_position
        if direction == "up":
            y = (y - 1) % 10
        elif direction == "down":
            y = (y + 1) % 10
        elif direction == "left":
            x = (x - 1) % 10
        elif direction == "right":
            x = (x + 1) % 10

        self.player_position = (x, y)
        result = f"Moved to ({x}, {y})"
        result += "\n" + self.encounter(x, y)
        return result

    def attack(self, args):
        """Атака монстра"""
        if len(args) == 0:
            return "Usage: attack <monster_name> [with <weapon>]"

        if len(args) == 3 and args[1] == "with":
            monster_name, weapon = args[0], args[2]
        elif len(args) == 1:
            monster_name, weapon = args[0], "sword"
        else:
            return "Usage: attack <monster_name> with <weapon>"

        if weapon not in self.weapons:
            return "Unknown weapon"

        x, y = self.player_position
        monster = self.field[x][y]
        if not monster or monster[0] != monster_name:
            return f"No {monster_name} here"

        name, hello, hp = monster
        damage = min(self.weapons[weapon], hp)
        hp -= damage
        result = f"Attacked {name} with {weapon}, damage {damage} hp\n"

        if hp <= 0:
            self.field[x][y] = None
            result += f"{name} died"
        else:
            self.field[x][y] = (name, hello, hp)
            result += f"{name} now has {hp} hp"

        return result

    def addmon(self, args):
        """Добавление монстра"""
        try:
            if len(args) < 7:
                return "Invalid arguments: not enough parameters"

            name = args[0]
            params = {}
            key = None
            for part in args[1:]:
                if part in ["hello", "hp", "coords"]:
                    key = part
                elif key is not None:
                    params[key] = part if key not in params else params[key] + " " + part

            if not all(k in params for k in ["hello", "hp", "coords"]):
                return "Invalid arguments: missing required fields"

            hello = params["hello"]
            hp = int(params["hp"])
            x, y = map(int, params["coords"].split())

            if hp <= 0:
                return "Hitpoints must be positive"

            if name not in cowsay.list_cows():
                return "Unknown monster"

            if (x, y) == self.player_position:
                return "Cannot add monster to player's position"

            old_mon = self.field[x][y] is not None
            self.field[x][y] = (name, hello, hp)

            result = f"Added {name} at ({x}, {y}) saying '{hello}' with {hp} HP"
            if old_mon:
                result += "\nReplaced old monster"
            return result
        except ValueError:
            return "Invalid number format"

    def encounter(self, x, y):
        """Проверяет, есть ли монстр в клетке"""
        monster = self.field[x][y]
        if monster is None:
            return ""
        name, hello, _ = monster
        return cowsay.cowsay(hello, cow=name)


if __name__ == "__main__":
    server = MUDServer()
    server.start()

