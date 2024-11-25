class Counter:
    def __init__(self):
        self.num = 0

    def __set__(self, obj, val):
        self.num = val 

    def __get__(self, obj, cls):
        return self.num



class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1

c = C()
print(c.counter)
d = C()
print(c.counter, d.counter)
del c
print(d.counter)
     

