# 这个方法可以做所有的比较，这是一个装饰器。但一定要定义eq方法，其他的要使用
# 一个一般用lt方法
from functools import total_ordering

@total_ordering
class A:
    def __init__(self,x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x

print(A(5) >= A(6))
print(A(5) > A(6))
print(A(5) <= A(6))
print(A(5) == A(6))