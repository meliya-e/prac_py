from fractions import Fraction

def eval_poly(ks, deg, x):
    res = 0
    for i in range(deg + 1):
        res += ks[i] * (x**(deg - i))
    return res

def fun(s, w, deg_A, *ks):
    ks_A = ks[:deg_A + 1]
    deg_B = ks[deg_A + 1]
    ks_B = ks[deg_A + 2:]

    s = Fraction(s)
    w = Fraction(w)
    ks_A = [Fraction(c) for c in ks_A]
    ks_B = [Fraction(c) for c in ks_B]

    A_s = eval_poly(ks_A, deg_A, s)
    B_s = eval_poly(ks_B, deg_B, s)

    if B_s == 0:
        return False

    return A_s * Fraction(1, B_s) == w

import sys
exec(sys.stdin.read())
