class Doubleton(type):
    _instance = []
    count = -1
    def __call__(cls, *args, **kw):
        if len(cls._instance) < 2:
             cls._instance.append(super().__call__(*args, **kw))
             
        cls.count += 1
        return cls._instance[cls.count % 2]

class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")
