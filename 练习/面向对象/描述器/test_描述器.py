# class Typed:
#     def __init__(self, type):
#         self.type = type
#         print(self.type, type)
#
#     def __get__(self, instance, owner):
#         print('__get__ mothed')
#         return instance.__dict__[self.type]
#         # pass
#
#     def __set__(self, instance, value):
#         print('T.set', self, instance, value)
#         print(self.__dict__)
#         if not isinstance(value, self.type):
#             raise ValueError(value)
#         instance.__dict__[self.type] = value
#
# # set方法中可以做给实例属性赋值的动作，不然下面的Person类中调用set方法时就只能操作类属性，要修改实例属性就
# # 需要在set方法中对实例字典进行修改。另外，set方法中定义如何赋值，get方法中就要定义用同样的方法去取值，比如
# # set方法中定义了给实例属性赋值，get方法就要到实例属性取这个值。
# class Person:
#     name = Typed(str)
#     age = Typed(int)
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
# p1 = Person('tom', 18)
# print(p1.__dict__)
# print(type(p1.name))
# p2 = Person('jerry', 20)
# print(p2.name)
# ================================================================================================
# 自定义StaticMethod和ClassMethod，为什么使用__get__方法可以实现，而不需要定义__call__方法
# from functools import partial
#
# class Foo:
#     def __init__(self, fn):
#         print(fn)
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print(self, instance, owner)
#         return self.fn
#
#     # def __call__(self, *args, **kwargs):
#     #     print('call', self, *args, **kwargs)
#     #     return self.fn
#
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
#     # def __call__(self, *args, **kwargs):
#     #     print('call', self, *args, **kwargs)
#     #     return partial(self.fn, *args, **kwargs)
#
# class A:
#     @Foo
#     def foo():
#         print('static')
#
#     @ClassMethod
#     def bar(cls):
#         print(cls.__name__)
#
# A.foo()
# f = A.foo
# print(f)
# f()
#==========================================================
# 类装饰器
# from functools import partial
# class Foo:
#     def __init__(self, func):
#         self._func = func
#
#     # def __call__(self):
#     #     print('class decorator runing')
#     #     self._func()
#     #     print('class decorator ending')
#
#     def __get__(self, instance, owner):
#         print('class decorator runing')
#         return self._func()
#         # return partial(self._func, owner)
#
# # class A:
# @Foo
# def bar():
#     print('bar')
#
# bar()
#===============================================================
# 测试，实现property装饰器
# class TestProperty(object):
#     def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#         self.__doc__ = doc
#
#     def __get__(self, obj, objtype=None):
#         print("in __get__")
#         if obj is None:
#             return self
#         if self.fget is None:
#             raise AttributeError
#         return self.fget(obj)
#
#     def __set__(self, obj, value):
#         print("in __set__")
#         if self.fset is None:
#             raise AttributeError
#         self.fset(obj, value)
#
#     def __delete__(self, obj):
#         print("in __delete__")
#         if self.fdel is None:
#             raise AttributeError
#         self.fdel(obj)
#
#     def getter(self, fget):
#         print("in getter")
#         return type(self)(fget, self.fset, self.fdel, self.__doc__)
#
#     def setter(self, fset):
#         print("in setter")
#         return type(self)(self.fget, fset, self.fdel, self.__doc__)
#
#     def delete(self, fdel):
#         print("in deleter")
#         return type(self)(self.fget, self.fset, fdel, self.__doc__)
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     @TestProperty
#     def math(self):
#         return self._math
#
#     @math.setter
#     def math(self, value):
#         if 0 < value <= 100:
#             self._math = value
#         else:
#             raise ValueError("Valid value must be in [0, 100]")
#
# test = Student('ab')
# test.math = -100
# # print(test.__dict__)
# print(test.math)
# =================================================================
class Test:
    a = 5
    def __init__(self, b):
        self.b = b

test = Test(23)
print(test.a)
test.a = 10
print(test.a, test.b)
print(Test.__dict__.items(), end='\n\n')