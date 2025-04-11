from math import *
def scale(a, b, A, B, x):
    return A + (x - a) / (b - a) * (B -A)

def graph(w, h, A, B, f):
    arr = list()
    screen = [[" "] * w for i in range(h)]
    for i in range(w):
        x = scale(0, w - 1, A, B, i)
        y = h - eval(f.replace('x', str(x)))
        arr.append(y)
    m_max = max(arr)
    m_min = min(arr)
    for i in range(w -1):
        y1 = scale(m_min, m_max, 0, h - 1, arr[i])
        y2 = scale(m_min, m_max, 0, h - 1, arr[i+1])
        for j in range(round(min(y1, y2)), round(max(y1, y2)) + 1):
            if 0 <= j < h:
                screen[j][i] = "*"
    return screen

def show(screen):
    print("\n".join("".join(s) for s in screen))

w, h, a, b, f = input().split()
show(graph(int(w), int(h), int(a), int(b), f))


import sys
exec(sys.stdin.read())
