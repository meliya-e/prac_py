class InvalidInput(Exception): pass
class BadTriangle(Exception): pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except:
        raise InvalidInput
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except:
        raise InvalidInput

    try:
        if not all(isinstance(i, (int, float)) for i in [x1, y1, x2, y2, x3, y3]):
            raise InvalidInput
        area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

        if area == 0:
            raise BadTriangle

        return round(area, 2)

    except BadTriangle:
        raise BadTriangle
    except Exception:
        raise InvalidInput

while True:
    try:
        s = triangleSquare(input())
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{s:.2f}")
        break

import sys
exec(sys.stdin.read())

