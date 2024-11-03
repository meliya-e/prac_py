from itertools import tee, islice
def slide(seq, n):
    iters = tee(seq, 3)
    while len(list(islice(iters[0], n))):
        yield from islice(iters[1], n)
        iters = tee(islice(iters[2], 1, None), 3)  

import sys
exec(sys.stdin.read())
