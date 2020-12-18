class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        print(self, 'add')
        return self.x + other.x

    def __iadd__(self, other):
        print(self, 'iadd')
        return A(self.x + other.x)

    def __radd__(self, other):
        print(self, 'radd')
        return self.x + other.x


a = A(4)
b = A(5)
# print(a, b)
# print(a + b)
# print(b + a)
b += a
# a += b
# ==================================================
#
# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         print(self, 'add')
#         return self.x + other.x
#
#     def __iadd__(self, other):
#         print(self, 'iadd')
#         return A(self.x + other.x)
#
#     def __radd__(self, other):
#         print(self, 'radd')
#         return self.x + other.x
#
#
# a = A(4)
# 1 + a
# ==============================================
# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         print(self, 'add')
#         return self.x + other.x
#
#     def __iadd__(self, other):
#         print(self, 'iadd')
#         return self.x + other.x
#
#     def __radd__(self, other):
#         print(self, 'radd')
#         return self.x + other.x
#
#
# class B:  # 未实现__add__
#     def __init__(self, x):
#         self.x = x
#
#
# a = A(4)
# b = B(10)
# print(a + b)
# print(b + a)
# =========================================
# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         print(self, 'add')
#         try:
#             x = other.x
#             return self.x + other.x
#         except AttributeError:
#             try:
#                 x = int(other)
#             except:
#                 x = 0
#             return self.x + x
#
#     def __iadd__(self, other):
#         print(self, 'iadd')
#         return A(self.x + other.x)
#
#     def __radd__(self, other):
#         print(self, 'radd')
#         return self + other
#
#
# class B:
#     def __init__(self, x):
#         self.x = x
#
#
# a = A(4)
# b = B(10)
# print(a + b)
# print(b + a)
# print(a + 2)
# print(2 + a)
# print(a + 'abc')
# print('abc' + a)