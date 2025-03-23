import cmd
import socket
import readline
import cowsay

class MUDClient(cmd.Cmd):
    prompt = "> "

    def __init__(self, host="localhost", port=12345):
        super().__init__()
        self.host = host
        self.port = port
        self.monsters = []
        self.weapons = ["sword", "spear", "axe"]
        self.fetch_game_data()

    def fetch_game_data(self):
        """Запрашивает у сервера список монстров"""
        try:
            with socket.create_connection((self.host, self.port)) as sock:
                sock.sendall(b"list_monsters")
                self.monsters = sock.recv(4096).decode().split()
        except Exception:
            print("Не удалось загрузить список монстров")

    def send_command(self, command):
        """Отправляет команду на сервер и получает ответ"""
        try:
            with socket.create_connection((self.host, self.port)) as sock:
                sock.sendall(command.encode())
                return sock.recv(4096).decode().strip()
        except Exception as e:
            return f"Ошибка соединения: {e}"

    def do_exit(self, arg):
        """Выход из игры"""
        print("Выход из игры")
        return True

    def do_EOF(self, arg):
        """Выход (Ctrl+D)"""
        return self.do_exit(arg)

    def default(self, line):
        """Отправляет любую неизвестную команду на сервер"""
        response = self.send_command(line)
        print(response)

    def complete_attack(self, text, line, begidx, endidx):
        """Автодополнение attack по именам доступных монстров"""
        parts = line.split()
        if len(parts) <= 2:
            return [m for m in self.monsters if m.startswith(text)]
        elif len(parts) >= 3 and parts[-2] == "with":
            return [w for w in self.weapons if w.startswith(text)]
        return []

    def complete_addmon(self, text, line, begidx, endidx):
        """Автодополнение addmon по доступным монстрам"""
        return [m for m in self.monsters if m.startswith(text)]

if __name__ == "__main__":
    client = MUDClient()
    client.cmdloop()

