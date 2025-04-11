N = int(input())
result = []
i = N
while i <= N+2:
    curr_i = ""
    j= N
    while j <= N+2:
        prod = i * j

        temp_res = prod
        count_num = 0
        while temp_res > 0:
            count_num += temp_res % 10
            temp_res //= 10
        if count_num == 6:
            res = ":=)"
        else:
            res = str(prod)
        curr_i += str(i) +  " * " + str(j) +  " = " + res + " "
        j += 1
    result.append(curr_i)
    i+=1
for string in result:
    print(string)

