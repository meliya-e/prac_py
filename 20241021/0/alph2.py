import string
from timeit import Timer
def fun():
    s = set("aabABbcD123")
    gl = set("aoueiy")
    sogl = set(string.ascii_lowercase) - gl
    res = (len(s & sogl), len(s & gl))
    return res
T = Timer(fun)
print(T.autorange())                                   
