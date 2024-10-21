from collections import Counter
from timeit import Timer
def fun():
    d = dict()
    t = "oer lr telj lr blrh"
    for i in t:
        d[i] = d.get(i, 0) + 1
    return d
def fun_count():
    t = "oer lr telj lr blrh"
    return Counter(t)
T1 = Timer(fun)
T2 = Timer(fun_count)
print(T1.autorange())
print(T2.autorange())
