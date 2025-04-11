from itertools import repeat

def repeater(seq, n):
    for i in range(seq):
        yield from repeat(i, n)
