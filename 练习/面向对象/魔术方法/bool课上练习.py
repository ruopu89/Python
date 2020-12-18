# class A: pass
#
# # print(bool(A()))
# # if A():
# #     print('Real A')
#
# class B:
#     def __bool__(self):
#         return False
#
# print(bool(B()))
# if B():
#     print('Real B')
#
# class C:
#     def __len__(self):
#         return 1
#
# print(bool(C()))
# if C():
#     print('Real C')
# =====================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self is other:
            return True
        return self.x == other.x and self.y == other.y

    # def __len__(self, *args, **kwargs):
    #     return 1
    #
    # def __bool__(self):
    #     return False

print(bool(Point(4,5)))