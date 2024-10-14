from math import sin
def scale(a, b, A, B, x):
    y = A + (x - a) / (b - a) * (B - A)
    return y
A , B = -4, 4 
for i in range(20):
        x = scale(0, 19, A, B, i)
        y = sin(x)
        spc = round(scale(-1, 1, 0, 40, y))
        print(spc * " ", "*")

