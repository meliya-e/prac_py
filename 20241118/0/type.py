CC = type("C", (), { "__init__": lambda self, val: setattr(self, "a", val)})
c = CC(123)
print(c.a)

