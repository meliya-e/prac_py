class Typ:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        def f(*args):
            for i in args:
                if not isinstance(i, self.typ):
                    raise TypeError
            return fun(*args)
        return f


