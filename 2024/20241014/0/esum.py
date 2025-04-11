from decimal import Decimal
from fractions import Fraction

def esum(N, one):
    fact = 1
    sum_temp = one
    for n in range(1, N + 1):
        fact *= n
        sum_temp += one / fact
        return sum_temp

    

