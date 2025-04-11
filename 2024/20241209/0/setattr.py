C = type("C", (), {"var":100500, "__init__": lambda self, val: setattr(self, "var", val)})
print(C.var)
c = C(123)
print(c.var)

