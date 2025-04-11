def isint(f):
    def newfun(*args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError
        return f(*args)
    return newfun
@isint
def summa(a, b, c):
    return a+b+c

print(summa(1, 2, 3))
print(summa(1.0, 2.0, 3.0))
