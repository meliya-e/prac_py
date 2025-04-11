from math import sin

def scale(a, b, A, B, x):
    y = A + (x - a) / (b - a) * (B - A)
    return y
A , B, w, h = -4, 4, 60, 20
screen = [["."]*w for i in range(h)]
for i in range(w):
        x = scale(0, w - 1, A, B, i)
        y = sin(x)
        spc = round(scale(-1, 1, 0, h - 1, y))
        screen[spc][i] = "@"
print("\n".join(["".join(s) for s in screen]))


