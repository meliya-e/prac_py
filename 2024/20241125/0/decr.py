class C:
    def __get__(self, obj, cls):
        print("Get", obj)
        return obj._val
       
    def __set__(self, obj, val):
        print("SET", obj, val)
        obj._val = abs(val)

    def __delete__(self, val):
        print("DELETE", obj)

class D:
    descr = C()

d = D()
d.descr = -12345
d.descr
