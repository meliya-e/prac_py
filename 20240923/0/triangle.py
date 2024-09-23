a, b, c = eval(input())
if max(a, b, c) < (a + b + c) - max(a, b, c) and min(a, b, c) > 0:
    print("treug")
else:
    print("ne treug")
