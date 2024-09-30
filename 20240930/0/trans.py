res = []
while arr := input():
    res.append(eval(arr))
if all([len(res) == len(a) for a in res]):
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            res[i][j], res[j][i] = res[j][i], res[i][j]
else:
    print("nado vvesty kvadratnuyu")
for num in res:
    print(num)
