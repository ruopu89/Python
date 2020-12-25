# class Person:
#     def __init__(self, name:str, age:int):
#         self.name = name
#         self.age = age
#
# 对上面的类的实例的属性name、age进行数据校验
#
# 思路
#
# 1. 写函数，在`__init__`中先检查，如果不合格，直接抛异常
# 2. 装饰器，使用`inspect`模块完成
# 3. 描述器

# 写函数检查
# class Person:
#     def __init__(self, name:str, age:int):
#         params = ((name, str),(age, int))
#         # print(self.checkdata(params))
#         if not self.checkdata(params):
#             # print(1, 'TypeError')
#             raise TypeError()
#         self.name = name
#         self.age = age
#
#     def checkdata(self, params):
#         for p,t in params:
#             # print(p, t)
#             # print("params:{}, p:{}, t:{}".format(params, p, t))
#             if not isinstance(p, t):
#                 # print('TypeError')
#                 return False
#         return  True
#
# p = Person('tom', '20')
# print(p.__dict__)

# =========================================================
# 描述器方式
# class Typed:
#     def __init__(self, name, type):
#         # print(1, 'first')
#         self.name = name
#         self.type = type
#         # print(3333333333333333)
#
#     def __get__(self, instance, owner):
#         if instance is not None:
#             return instance.__dict__[self.name]
#         return self
#
#     def __set__(self, instance, value):
#         # print(2, 'two', instance)
#         if not isinstance(value, self.type):
#             raise TypeError(value)
#         instance.__dict__[self.name] = value
#
# class Person:
#     name = Typed('name', str)
#     age = Typed('age', int)
#     # print(name.__dict__, age.__dict__)
#
#     def __init__(self, name:str, age:int):
#         self.name = name
#         self.age = age
#
# p = Person('tom', 20)
# print("p:{}, Person:{}".format(p.__dict__, Person.__dict__))
# =======================================================
# 使用inspect模块
class Typed:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __get__(self, instance, owner):
        if instance is not None:
            return instance.__dict__[self.name]
        return self

    def __set__(self, instance, value):
        print("set:{},{}".format(self,instance))
        if not isinstance(value, self.type):
            raise TypeError(value)
        instance.__dict__[self.name] = value

import inspect

def typeassert(cls):
    params = inspect.signature(cls).parameters
    print(1, "params:{}".format(params))
    for name,param in params.items():
        print(2, "name:{}, param:{}".format(param.name, param.annotation))
        print(3, "params.items:{}".format(params.items()))
        if param.annotation != param.empty:
            setattr(cls, name, Typed(name, param.annotation))
    return cls

@typeassert
class Person:
    def __init__(self, name:str, age):
        self.name = name
        self.age = age
        print("Person:{}".format('class'))

    def __repr__(self):
        return "{} is {}".format(self.name, self.age)

p = Person('tom', '20')
# p = Person('tom', 20)
print(p.__dict__)
print(p)
# =====================================================================
# class Typed:
#     def __init__(self, type):
#         self.type = type
#
#     def __get__(self, instance, owner):
#         pass
#
#     def __set__(self, instance, value):
#         print('T.set', self, instance, value)
#         if not isinstance(value, self.type):
#             raise ValueError(value)
#
# import inspect
#
# class TypeAssert:
#     def __init__(self, cls):
#         self.cls = cls  # 记录着被包装的Person类
#         params = inspect.signature(self.cls).parameters
#         print(params)
#         for name, param in params.items():
#             print(name, param.annotation)
#             if param.annotation != param.empty:
#                 setattr(self.cls, name, Typed(param.annotation))  # 注入类属性
#         print(self.cls.__dict__)
#
#     def __call__(self, name, age):
#         p = self.cls(name, age)  # 重新构建一个新的Person对象
#         return p
#
# @TypeAssert
# class Person:  # Person = TypeAssert(Person)
#     # name = Typed(str)
#     # age = Typed(int)
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

# p1 = Person('tom', 18)
# print(id(p1))
# p2 = Person('tom', 20)
# print(id(p2))
# p3 = Person('tom', '20')