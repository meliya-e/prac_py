import sys

data = sys.stdin.buffer.read().rstrip(b"\n")
N = data[0]
tail = data[1:]
L = len(tail)
part = []
for i in range(N):
    nach =( i*L) // N
    end = ((i+1)*L) // N
    part.append(tail[nach:end])

sys.stdout.buffer.write(bytearray([N]) + b"".join(sorted(part)))
