class Undead(Exception): pass
class Skeleton(Undead): pass
class Zombie(Undead): pass
class Ghoul(Undead): pass

def necro(a):
    if a % 3 == 0:
        raise Skeleton
    elif a % 3 == 1:
        raise Zombie
    elif a % 3 == 2:
        raise Ghoul

for a in range(*eval(input())):
    try:
        necro(a)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")

import sys
exec(sys.stdin.read())

