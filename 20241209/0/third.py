class A:
    a, b, c = input().split()
while (s := input()):
    res = s.split()
    match res:
        case (A.a, *tail) if "yes" in s:
            print(1)
        case [A.b]:
            print(2)
        case A.c, *tail, A.b:
            print(3)

