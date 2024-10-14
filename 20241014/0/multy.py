from fractions import Fraction
from decimal import Decimal

def multiplier(x, y, Type):
               x_t = Type(x)
               y_t = Type(y)
               res = x_t * y_t
               return res
print(multiplier("1.2", "3.4", float))
