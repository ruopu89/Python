# class MyClass:
#     """A example class"""
#     x = 'abc'
#
#     def foo(self):
#         return 'My Class'
#
# print(MyClass.x)
# print(MyClass.foo)
# print(MyClass.__doc__)
# ==========================================
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def showage(self):
#         print('{} is {}'.format(self.name, self.age))
#
# tom = Person('Tom', 20)
# jerry = Person('Jerry', 25)
# print(tom.name, jerry.age)
# jerry.age += 1
# print(jerry.age)
# jerry.showage()
# =================================================
# class MyClass:
#     def __init__(self):
#         print('self in init = {}'.format(id(self)))
#
# c = MyClass()
# print('c = {}'.format(id(c)))
# =================================================
# class Person:
#     age = 3
#     def __init__(self, name):
#         self.name = name
#
# tom = Person('Tom')
# jerry = Person('Jerry')
#
# print(tom.name, tom.age)
# print(jerry.name, jerry.age)
# print(Person.age)
# Person.age = 30
# print(Person.age, tom.age, jerry.age)
# =================================================
# class Person:
#     age = 3
#
#     def __init__(self, name):
#         self.name = name
#
# print('---------class-------------')
# print(Person.__class__)
# print(sorted(Person.__dict__.items()), end='\n\n')
#
# tom = Person('Tom')
# print('----------instance tom------------------')
# print(tom.__class__)
# print(sorted(tom.__dict__.items()),end='\n\n')
#
# print("--------------------tom's class----------------------")
# print(tom.__class__.__name__)
# print(sorted(tom.__class__.__dict__.items()), end='\n\n')
# =================================================
# class Person:
#     age = 3
#     height = 170
#
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
# tom = Person('Tom')
# jerry = Person('Jerry', 20)
#
# Person.age = 30
# print(Person.age, tom.age, jerry.age)
#
# print(Person.height, tom.height, jerry.height)
# jerry.height = 175
# print(Person.height, tom.height, jerry.height)
#
# tom.height += 10
# print(Person.height, tom.height, jerry.height)
#
# Person.height += 15
# print(Person.height, tom.height, jerry.height)
#
# Person.weight = 70
# print(Person.weight, tom.weight, jerry.weight)
#
# print(tom.__dict__['height'])
# print(tom.__dict__['weight'])
# =================================================
# def add_name(name, cls):
#     cls.NAME = name

# def add_name(name):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper
#
# @add_name('Tom')
# class Person:
#     AGE = 3
#
# print(Person.NAME)
# =================================================
# class Person:
#     def normal_method():
#         print('normal')
#
# Person.normal_method()
# Person().normal_method()
#
# print(Person.__dict__)
# =================================================
# class Person:
#     @classmethod
#     def class_method(cls):
#         print('class = {0.__name__}({0})'.format(cls))
#         cls.HEIGHT = 170
#
# Person.class_method()
# print(Person.__dict__)
# =================================================
# class Person:
#     @classmethod
#     def class_method(cls):
#         print('class = {0.__name__}({0})'.format(cls))
#         cls.HEIGHT = 170
#
#     @staticmethod
#     def static_methd():
#         print(Person.HEIGHT)
#
# Person.class_method()
# Person.static_methd()
# print(Person.__dict__)
# =================================================
# class Person:
#     def normal_method():
#         print('normal')
#
#     def method(self):
#         print("{}'s method".format(self))
#
#     @classmethod
#     def class_method(cls):
#         print('class = {0.__name__}({0})'.format(cls))
#         cls.HEIGHT = 170
#
#     @staticmethod
#     def static_method():
#         print(Person.HEIGHT)

# print('~~~~~~~~~~类访问')
# print(1, Person.normal_method())
# # print(2, Person.method())
# print(3, Person.class_method())
# print(4, Person.static_method())
# print(Person.__dict__)
# print('~~~~~~~~~~实例访问')
# print('tom------------')
# tom = Person()
# # print(1, tom.normal_method())
# print(2, tom.method())
# print(3, tom.class_method())
# print(4, tom.static_method())
# print('jerry-----------')
# jerry = Person()
# print(1, jerry.normal_method())
# print(2, jerry.method())
# print(3, jerry.class_method())
# print(4, jerry.static_method())
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def growup(self, i=1):
#         if 0 < i < 150:
#             self.age += i
#
# p1 = Person('tom')
# p1.growup(20)
# print(p1.age)
# p1.age = 160
# print(p1.age)
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     def growup(self, i=1):
#         if 0 < i < 150:
#             self.__age += i
#
#     def getage(self):
#         return self.__age
#
# p1 = Person('Tom')
# p1.growup(20)
# p1.__age = 28
# print(p1.__age)
# print(p1.getage())
# print(p1.__dict__)

# p1._Person__age = 15
# print(p1.getage())
# print(p1.__dict__)
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self._age = age
#
# tom = Person('Tom')
# print(tom._age)
# print(tom.__dict__)
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self._age = age
#
#     def _getname(self):
#         return self.name
#
#     def __getage(self):
#         return self._age
#
# tom = Person('Tom')
# print(tom._getname())
# # print(tom.__getage())
# print(tom.__dict__)
# print(tom.__class__.__dict__)
# print(tom._Person__getage())
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     def age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
# tom = Person('Tom')
# print(tom.age())
# tom.set_age(20)
# print(tom.age())
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @age.deleter
#     def age(self):
#         print('delaaa')
#
# tom = Person('Tom')
# print(tom.age)
# tom.age = 20
# print(tom.age)
# del tom.age
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     def getage(self):
#         return self.__age
#
#     def setage(self, age):
#         self.__age = age
#
#     def delage(self):
#         print('del')
#
#     age = property(getage, setage, delage, 'age property')
#
# tom = Person('Tom')
# print(tom.age)
# tom.age = 20
# print(tom.age)
# del tom.age
#==================================================
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     age = property(lambda self:self.__age)
#
# tom = Person('Tom')
# print(tom.age)
#==================================================
# import time
#
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     def __del__(self):
#         print('delete {}'.format(self.name))
#
# def test():
#     tom = Person('tom')
#     tom.__del__()
#     tom.__del__()
#     tom.__del__()
#     tom.__del__()
#     print('===========start==============')
#     tom2 = tom
#     tom3 = tom2
#     print(1, 'del')
#     del tom
#     time.sleep(3)
#
#     print(2, 'del')
#     del tom2
#     time.sleep(3)
#     print('~~~~~~~~~~~~~~~~~')
#
#     del tom3
#     time.sleep(3)
#     print('=============end')
#
# test()

# class MyClass:
#     x = 123
#
#     def foo(self):
#         print(id(self))
#         return id(self)
#         # print(self.x)
#
# # print(MyClass)
# # print(MyClass.__name__)
# # print(MyClass.x)
# # print(MyClass.foo)
# a = MyClass()
# # print(a.foo)
# print(a.foo())

class Person:
    # pass
    x = 'abc'

    def __init__(self, name, age=18):
        self.name = name
        self.y = age

    def show(self, x, y):
        print(self.name, self.y)
        self.y = x
        Person.x = x


a = Person('tom')
b = Person('jerry', 20)
print(a.__class__, b.__class__)
print(a.__class__.__qualname__, a.__class__.__name__)
a.show(100, 'a')
print(a.show(200, 'b'))
