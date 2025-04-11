from itertools import count


def f():
    s = 0
    i = 1
    while True:
        s += 1/(i*i)
        yield s
        i += 1

