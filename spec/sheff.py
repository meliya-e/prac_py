def sheff(a, b):
    if a and not b:
        return a
    elif b and not a:
        return b
    elif not a and not b:
        return True
    else:
        return False
