def istype(typ):
    def decor(fun):
        def newfun(*args):
            for i in args:
                if not isinstance(i, typ):
                    raise TypeError
            return fun(*args)
        return newfun
    return decor

@istype(int)
def summa(a, b, c):
    return a+b+c

print(summa(1, 2, 3))
print(summa(1.0, 2.0, 3.0))

