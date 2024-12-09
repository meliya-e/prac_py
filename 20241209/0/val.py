import inspect
class C:
    a: int 
    def __init__(self, val):
        typ = inspect.get_annotations(self.__class__)["a"]
        if not isinstance(val, typ):
            raise TypeError(f"val must be {typ}")
        self.a = val
