from itertools import product

print(list((f"{a}{n}" for a, n in product("abcdefg", "12345678"))))
