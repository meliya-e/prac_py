from collections import UserString
class DivStr(UserString):
    def __init__(self, s=""):
        super().__init__(s)

    def __floordiv__(self, n):
        length = len(self.data)
        part_size = length // n
        ost = length % n
        result = []

        start = 0
        for i in range(n):
            end = start + part_size + (1 if i < ost else 0)
            result.append(self.data[start:end])
            start = end

        return iter(result)
    def __mod__(self, n):
        return self.__class__(self.data[len(self)//n*n:])


import sys
exec(sys.stdin.read())
