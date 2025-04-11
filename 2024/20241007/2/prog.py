def fun(a, b):
    if type(a) != type(b):
        print("objects have different types")
    if isinstance(a, (int, float)):
        return a-b
    if isinstance(a, (tuple, list)):
        res = [obj for obj in a if obj not in b]
        return type(a)(res)
    print("undefined type")

import sys
exec(sys.stdin.read())
