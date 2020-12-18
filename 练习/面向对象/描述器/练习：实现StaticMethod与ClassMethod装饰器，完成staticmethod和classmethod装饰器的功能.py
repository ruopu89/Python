# from functools import partial
#
# class StaticMethod:
#     def __init__(self, fn):
#         print(fn)
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print(1, self, instance, owner)
#         return self.fn
#
# class ClassMethod:
#     def __init__(self, fn):
#         print(fn)
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print(2, self, instance, owner)
#         return partial(self.fn, owner)
#
# class A:
#     @StaticMethod  # StaticMethod(foo) = foo
#     def foo():
#         print('static')
#
#     @ClassMethod
#     def bar(cls):
#         print(cls.__name__)

# A.foo()
# f = A.foo
# f()

# f = A.bar
# print(f)
# f()
# A.bar(A)
# ==============================================================================
# from functools import partial
# class StaticMethod:
#     def __init__(self, fn):
#         print(fn)
#         self._fn = fn
#
#     def __get__(self, instance, owner):
#         print(self, instance, owner)
#         return self._fn
#
# class ClassMethod:
#     def __init__(self, fn):
#         print(fn)
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print(self, instance, owner)
#         return partial(self.fn, owner)
#
# class A:
#     @StaticMethod
#     def foo():
#         print('static method')
#
#     @ClassMethod
#     def bar(cls):
#         print(cls.__name__)
        # return cls.__name__

# A.stmtd()
# A().stmtd()
# f = A.foo
# f = A.bar
# print(f())
# ===========================================================
from functools import partial

class ClassMethod:  # 怕冲突改名
    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, cls):
        # ret = self._fn(cls)
        print(self, instance, cls)
        ret = partial(self._fn, cls)
        return ret

class A:
    @ClassMethod
    # clsmtd = ClassMethod(clsmtd)
    # 调用A.clsmtd() 或者 A().clsmtd()
    def clsmtd(cls):
        print(cls.__name__)

print(A.__dict__)
A.clsmtd
A.clsmtd()
A().clsmtd()