from fractions import Fraction
def is_solution(a):

    s = Fraction(a[0])
    w = Fraction(a[1])
    degree_A= int(a[2])
    coeffs_A = list(map(Fraction, a[3:4 + degree_A]))
    degree_B = int(a[4 + degree_A])
    coeffs_B = list(map(Fraction, a[5 + degree_A:]))

    A_s = 0
    for i in range(degree_A + 1):
        A_s += coeffs_A[i] * (s ** i)
    B_s = 0
    for i in range(degree_B + 1):
        B_s += coeffs_B[i] * (s ** i)

    return Fraction(A_s, B_s) == w if B_s else False
    
a = input().split(', ')
print(is_solution(a))

