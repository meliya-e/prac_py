def BinPow(a, N, f):
        obj = a
        n = N-1
        while n > 0:
            if n % 2 == 1:
                obj = f(obj, a)
            #obj *= obj
            a = f(a, a)
            n //= 2
        return obj

#print(*BinPow((1,2,56,23,56,7), 99999, tuple.__add__))                  
