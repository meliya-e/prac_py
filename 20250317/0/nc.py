import sys
import socket
import cmd

class nc(cmd.Cmd):
    prompt = ">"
    def __init__(self, *ap, socket=None, **kwargs):
        self.socket = socket
        super().__init__(*ap, **kwargs)

    def do_print(self, arg):
        self.socket.sendall(f"info {arg}\n".encode())
        self.response()        

    def complete_info(self, text, line, begidx, endidx):
        adr = "host", "port"
        return [m for m in adr if m.startwith(text)]

    def do_info(self, arg):
        self.socket.sendall(f"info {arg}\n".encode())
        self.response()


host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while msg := sys.stdin.buffer.readline():
        s.sendall(msg)
        print(s.recv(1024).rstrip().decode())
