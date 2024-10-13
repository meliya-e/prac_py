matr1 = []
line = list(eval(input()))
matr1.append(line)
count = len(matr1[0])
for i in range(1, count):
    line = list(eval(input()))
    matr1.append(line)

matr2 = []
line = list(eval(input()))
matr2.append(line)
for i in range(1, count):
    line = list(eval(input()))
    matr2.append(line)

res = list([0] * count for _ in range(count))
for i in range(count):
    for j in range(count):
        for k in range(count):
            res[i][j] += matr1[i][k] * matr2[k][j]
for row in res:
    for ind in range(len(row)):
        if ind > 0:
            print(",", end="")
        print(row[ind], end="")
    print()
