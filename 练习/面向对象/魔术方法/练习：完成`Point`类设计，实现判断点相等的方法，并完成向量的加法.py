class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        tmpx = self.x + other.x
        tmpy = self.y + other.y
        return Point(tmpx, tmpy)

    def __str__(self):
        return '<Point: {},{}>'.format(self.x, self.y)

    def __repr__(self):
        return '<Point: {},{}>'.format(self.x, self.y)

p1 = Point(1,1)
p2 = Point(1,1)
points = (p1, p2)
print(points)
print(points[0]+points[1])
print(p1 == p2)