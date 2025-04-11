
while s := input():
    a = eval(s)
    if a == 13:
        print("oops")
        break
    elif a % 2 == 0:
            print(a)
else:
        print("congrats")
