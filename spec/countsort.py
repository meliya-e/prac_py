arr = [[0]*101 for _ in range(101)]
while True:
    pars = input()
    if pars == "":
        break
    separate = pars.split(",")
    a = int(separate[0])
    b = int(separate[1])
    if 1<= a <=100 and 1<= b <=100:
        arr[a][b] += 1
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] > 0:
            for _ in range(arr[i][j]):
                print(f"{i}, {j}")


