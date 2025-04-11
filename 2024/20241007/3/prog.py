from math import *

def Calc(s, t, u):
    def fun_x(x):
        return eval(s)
    def fun_y(x):
        return eval(t)
    def fun_x_y(x, y):
        return eval(u)
    def res(x):
        return fun_x_y(fun_x(x), fun_y(x))
    return res
s,t,u = eval(input())
x = eval(input())
F = Calc(s, t, u)
print(F(x))

#from math import *
import sys
exec(sys.stdin.read())
