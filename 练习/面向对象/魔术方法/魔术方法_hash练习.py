# 设计二维坐标类Point，使其成为可hash类型，并比较2个坐标的实例是否相等？
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self is other:
            return True
        return self.x == other.x and self.y == other.y

p = Point(4, 5)
p1 = Point(4, 5)
p2 = Point(3, 4)
print(p)
print(p == p1)
print(p == p2)
print(p.__eq__(p1))
print(p.__eq__(p2))