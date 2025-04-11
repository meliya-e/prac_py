
def init(self, val):
    self.var = val

C = type("C", (), {"var":100500, "__init__":init})
print(C.var)
c = C(123)
print(c.var)
