import sys

data = sys.stdin.buffer.read()
dec = data.decode("utf-8", errors = "replace").encode("latin1", errors = "replace").decode("cp1251", errors = "replace")
print(dec)

