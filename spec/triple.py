def acmp(a, b):
    return(a[0] == b[0] and a[1] == b[1] and a[2] == b[2]) - (a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2])

seq = []
while s := input():
    seq.append(eval(s))

res = []
while seq:
    for n, a in enumerate(seq):
        if all(not acmp(sorted(a), sorted(b)) for b in seq):
            res.append(seq.pop(n))
            break

for el in res:
    print(*el, sep=", ")
