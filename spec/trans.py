arr = []
line = list(eval(input()))
arr.append(line)
count = len(arr[0])
for i in range(1, count):
    line = list(eval(input()))
    arr.append(line)

size = 2*count - 1
trans = [["" for _ in range(size)] for _ in range(size)]
for i in range(count):
    for j in range(count):
        trans[i+j][count - 1 + (i-j)] = arr[i][j]
matr = [["" for _ in range(size)] for _ in range(size)]
for column in range(size):
   ind = size - 1
   for sep_line in range(size -1, -1, -1):
       if trans[sep_line][column] != "":
           matr[ind][column] = trans[sep_line][column]
           ind -= 1
for sep_line in matr:
    res = [str(i) for i in reversed(sep_line) if i != ""]
    print(",".join(res))
