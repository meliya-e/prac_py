from itertools import filterfalse

def f(n, seq):
    yield from filterfalse(lambda x: x % n, seq)


def f2(n, seq):
    return filterfalse(lambda x: x % n, seq)

