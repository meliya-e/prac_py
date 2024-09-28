num = int(input())
res = []
if (num % 2 == 0) and (num % 25 == 0):
    res.append("A + ")
else:
    res.append("A - ")
if (num % 2 != 0) and (num % 25 == 0):
    res.append("B + ")
else:
    res.append("B - ")
if num % 8 == 0:
    res.append("C + ")
else:
    res.append("C - ")
print(*res, sep = " ")
