sum = 0
while True:
    num = int(input())
    if num <= 0:
        print(num)
        break
    sum += num
    if sum >= 21:
        print(sum)
        break

    
