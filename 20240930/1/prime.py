m, n = eval(input())
print(list(x for x in range(m, n) if x > 1 and all(x % i != 0 for i in range(2, x))))
