
lst = list(eval(input()))
res = sorted(lst, key = lambda x: x*x % 100)
print(res)

