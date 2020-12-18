# class A:
#     X = 1
#     def __init__(self):
#         self.y = 5
#         self.z = 6
#
#     def show(self):
#         print(self.X, self.y, self.z)
#
# a = A()
# print(A.__dict__)
# print(a.__dict__)
# =========================================
# __slots__
class A:
    X = 1
    __slots__ = ('y', 'z')

    def __init__(self):
        self.y = 5

    def show(self):
        print(self.X, self.y)

a = A()
a.show()
print('A', A.__dict__)

print(a.__slots__)