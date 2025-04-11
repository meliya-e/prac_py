from math import *

funcs = dict()
count_str = 0
while (s := input()):
    count_str += 1
    if s.startswith("quit"):
        print(eval(s[5:].format(len(funcs) + 1, count_str)))
        #print(f"{s[5:]}: {len(funcs)+1}, {count_str}")
        break
    elif s.startswith(":"):
        parts = s[1:].split(" ")
        name = parts[0]
        *args, fun = parts[1:]
        funcs[name] = eval(f"lambda {", ".join(args)}: {fun}")
    else:
        parts = s.split()
        name = parts[0]
        args = list(map(eval, parts[1:]))
        if name in funcs:
            print(funcs[name](*args))
import sys
exec(sys.stdin.read())
