# 完成`Point`类设计，实现判断点相等的方法，并完成向量的加法。
# 在直角坐标系里面，定义原点为向量的起点。两个向量和与差的坐标分别等于这两个向量相应坐标的和与差若向量的表示为`(x,y)`形式，`A(X1, Y1) B(X2, Y2)`，则`A+B=(X1+X2, Y1+Y2), A-B=(X1-X2, Y1-Y2)`

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def add(self,other):
        return (self.x + other.x, self.y + other.y)

    def __str__(self):
        return '<Point: {},{}>'.format(self.x, self.y)

p1 = Point(1,1)
p2 = Point(1,1)
points = (p1,p2)
print(points[1])
# print(points[0].add(points[1]))
print(11111111, p1.add(p2))
print(points[0])
print(points[0] + points[1])
print(p1 == p2)
print(id(p1),id(p2))
print(p1 is p2)