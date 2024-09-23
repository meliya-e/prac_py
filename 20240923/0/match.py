
match int(input()):
    case 1:
        print("odin")
    case 2:
        print("dwa")
    case 3:
        print("tri")
   # case val if val > 0:
    #    print(val, "pologitel")
    case val if val % 2 == 0:
        print("chetnoe")
    case val if val % 2 != 0:
        print(val, "--eto mnogo")
    case _:
        print("mnogo")
