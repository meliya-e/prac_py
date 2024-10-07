def average(a, *args):
    sum_1 = a
    for i in args:
        sum_1 += i
    res = sum_1/ (len(args)+1)
    return res

