def objcount(cls):
    class wrapped(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            self.__class__.counter += 1
            if hasattr(cls, "__init__"):
                super().__init__(*args, **kwargs)

        def __del__(self):
            self.__class__.counter -= 1
            if hasattr(cls, "__del__"):
                super().__del__()
    return wrapped

import sys
exec(sys.stdin.read())
