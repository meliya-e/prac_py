while (s:=input()):
    match s.split():
        case "mov", r1, r2:
            print(f"moving {r2} to {r1}")
        case ("push"|"pop") as cmd, *reglist:
            print(f"{cmd}ing {reglist}")
        case cmd, r1:
            print(f"making {cmd} with {r1}")
        case _:
            print("Parse error")

