def div_ab(a, b):
    if b < 0.001:
        raise ValueError("denominator is too small")
    return a / b

def new(f, a, b):
    try:
        return f(a, b)
    except:
        return -1

for a, b in  ((10, 2), (1, 0), (9, 3)):
    print(new(div_ab, a, b))

div_ab(12, 0.0001)
