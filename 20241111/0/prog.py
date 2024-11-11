class Rectangle:
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)

    def __abs__(self):
        return abs((self.x2 - self.x1) * (self.y2 - self.y1))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __mul__(self, num):
        return self.__class__(self.x1 * num, self.y1 * num, self.x2 * num, self.y2 * num)
    __rmul__ = __mul__

    def __bool__(self):
        return abs(self) > 0

    #def __getitem__(self, idx):
       # return ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1))[idx]
    
    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.rectcnt)

    def __iter__(self):
        return iter(((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)))

    def __str__(self):
        return f"({self.x1}, {self.y1}), ({self.x1}, {self.y2}), ({self.x2}, {self.y2}), ({self.x2}, {self.y1}) kolich obj: {Rectangle.rectcnt}"

for x, y in Rectangle(1, 3, 5, 6):
    print(x, y)

#def fun():
 #   r = Rectangle(1, 2, 3, 6)

#r2 = Rectangle(2, 4, 5, 7)
#r3 = Rectangle(1, 2, 3, 6)
r4 = Rectangle(1, 1, 1, 1)
if r4:
    print(abs(r4))
else:
    print("noooooo")
