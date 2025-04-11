class dump:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        res = self.fun(*args, **kwargs)
        print(res)
        return res
