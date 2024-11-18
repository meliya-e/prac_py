class A:
     def __init__(self, val):
         self.val = val
     def __add__(self, other):
         return self.__class__(self.val + other.val)
     def __str__(self):
         return f"<{self.val}>"

class B(A):
     def __str__(self):
         return f"[{self.val}]"

a, b = B(9), B(7)
print(a, b, a+b)
