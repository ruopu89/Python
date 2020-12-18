# def foo():
#     print(foo.__module__, foo.__name__)
#
# foo()
# foo.__call__()
# =================================================
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, *args, **kwargs):
#         return "<Point {}:{}>".format(self.x, self.y)
#
# p = Point(4,5)
# print(p)
# print(p())
#
# class Adder:
#     def __call__(self, *args, **kwargs):
#         ret = 0
#         for x in args:
#             ret += x
#         # self.ret = ret
#         return ret
#
# adder = Adder()
# print(adder(4,5,6))
# print(adder.ret)
# ==========================================================
# def foo(x):
#     print(x)
# foo(5)
# print(foo.__dict__)
# print(foo.__call__(5))
# print(dir(foo))
# ===========================================================
class A:
    def __call__(self, *args, **kwargs):
        print(5)
A()()
a = A()
a(4,5,6)
a()