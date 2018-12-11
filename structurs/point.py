import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Point(-self.x, -self.y)

    def GetArrInt(self):
        return [int(self.x), int(self.y)]

    #degree
    def CreateDirection(angle):
        return Point(math.sin(angle * math.pi / 180), math.cos(angle * math.pi / 180))

