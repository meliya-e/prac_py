class C:
    __v = 0

    def inc(self):
        self.__v += 1

    def __str__(self):
        return f"<{self.__v}>"

class D(C):
    def __init__(self):
        self.v = 100500

c = C()
print(c)
c.inc()
print(c)
d = ()
d = D()
print(d)

