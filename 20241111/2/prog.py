class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = (tuple(p1), tuple(p2), tuple(p3))
    
    def area(self):
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        x3, y3 = self.points[2]
        
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

    def __abs__(self):
        return self.area()

    def __bool__(self):
        return self.area() > 0

    def __lt__(self, other):
        return self.area() < other.area()

    def __contains__(self, other):
        if not self.__bool__():
            return True
        if not other.__bool__():
            return False
        
        return all(self.point_in(p, other.points) for p in other.points)

    def point_in(self, point, tr_points):
        x, y = point
        x1, y1 = tr_points[0]
        x2, y2 = tr_points[1]
        x3, y3 = tr_points[2]

        total = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
        area1 = abs(0.5 * (x*(y2-y3) + x2*(y3-y) + x3*(y-y2)))
        area2 = abs(0.5 * (x1*(y-y3) + x*(y3-y1) + x3*(y1-y)))
        area3 = abs(0.5 * (x1*(y2-y) + x2*(y-y1) + x*(y1-y2)))

        return total == area1 + area2 + area3

    def __and__(self, other):
        if not self.__bool__() or not other.__bool__():
            return False
        return any(self.point_in(p, other.points) for p in self.points) or any(other.point_in(p, self.points) for p in other.points)

    def __repr__(self):
        return f"Triangle({self.points})"

import sys
exec(sys.stdin.read())
