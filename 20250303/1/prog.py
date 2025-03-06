import sys
import shlex
import cowsay

class MUD:
    def __init__(self):
        self.field = [[None for _ in range(10)] for _ in range(10)]
        self.player_position = (0, 0)
        print("<<< Welcome to Python-MUD 0.1 >>>")

        self.jgsbat_func = None
        try:
            with open("jgsbat.cow", "r", encoding="utf-8") as f:
                jgsbat_template = cowsay.read_dot_cow(f) #шаблон ackii-арта
                self.jgsbat_func = lambda msg: cowsay.cowsay(msg, cowfile=jgsbat_template)
        except Exception as e:
            print(f"Ошибка загрузки монстра jgsbat: {e}")

    def move_player(self, direction):
        x, y = self.player_position
        if direction == 'up':
            y = (y - 1) % 10
        elif direction == 'down':
            y = (y + 1) % 10
        elif direction == 'left':
            x = (x - 1) % 10
        elif direction == 'right':
            x = (x + 1) % 10
        else:
            print("Invalid command")
            return

        self.player_position = (x, y)
        print(f"Moved to ({x}, {y})")
        self.encounter(x, y)

    def add_monster(self, name, x, y, hello, hp):
        if name not in cowsay.list_cows() and name != "jgsbat":
            print("cannot add unknown monster")
            return
        if (x, y) == self.player_position:
            print("cannot add monster to player's position")
            return

        old_mon = self.field[x][y] is not None
        self.field[x][y] = (name, hello, hp)
        print(f"Added monster {name} to ({x}, {y}) saying {hello} with {hp} hitpoints")

        if old_mon:
            print("Replaced the old monster")

    def encounter(self, x, y):
        monster = self.field[x][y]
        if monster is not None:
            name, hello, _ = monster
            if name == "jgsbat" and self.jgsbat_func:
                print(self.jgsbat_func(hello))  
            else:
                print(cowsay.cowsay(hello, cow=name))

    def process_cmd(self, command):
        parts = shlex.split(command)
        if not parts:
            print("Invalid command")
            return

        if parts[0] in ['up', 'down', 'left', 'right']:
            self.move_player(parts[0])
        elif parts[0] == 'addmon':
            try:
                if len(parts) < 9:  # min число аргументов
                    raise ValueError("not enough arguments for addmon")

                name = parts[1]  #1 после addmon - имя монстра
                args = {}

                key = None
                for part in parts[2:]:  #пропускаем addmon и имя монстра
                    if part in ["hello", "hp", "coords"]:
                        key = part
                    elif key is not None:
                        if key in args:
                            args[key] += " " + part
                        else:
                            args[key] = part
               # print("Parsed args:", args)

                if not all(k in args for k in ["hello", "hp", "coords"]):
                    raise ValueError("missing required arguments")

                hello = args["hello"]
                hp = int(args["hp"])
                x, y = map(int, args["coords"].split())

                if hp <= 0:
                    print("hitpoints must be positive")
                    return

                self.add_monster(name, x, y, hello, hp)
            except (ValueError, KeyError):
                print("Invalid arguments")
        else:
            print("Invalid command")

game = MUD()
if sys.stdin.isatty():
    while True:
        #command = input("Enter command: ")
        game.process_cmd(input())
else:
    for line in sys.stdin:
        game.process_cmd(line.strip())

