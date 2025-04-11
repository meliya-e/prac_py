class dump(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                def wrapper(func):
                    def wrapped(self, *args, **kwargs):
                        print(f"{func.__name__}: {args}, {kwargs}")
                        return func(self, *args, **kwargs)
                    return wrapped

                dct[attr_name] = wrapper(attr_value)

        return super().__new__(cls, name, bases, dct)

import sys
exec(sys.stdin.read())
