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
# =======================================
# 装饰一个类
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
# print(Person.NAME,Person.__dict__)
# ======================================================
# class MyClass:
#     """this is a class"""
#     x = 123
#
#     def foo(self):
#         print(id(self))
#         # return self
#         print(self.x)
#
# print(1, MyClass)
# print(2, MyClass.__name__)
# print(3, MyClass.x)
# print(4, MyClass.foo)
# print(5, MyClass.__doc__)
# print(6, type(MyClass))
# # print(7,MyClass.foo())
# print('下面就是实例的东西了')
# a = MyClass()
# print(8,a.foo())
# print(9,a.x)
# print(10,a.foo)
# print('==========================')
# print(id(a))
# ================================================
# class MyClass:
#     """this is a class"""
#     x = 123
#
#     def __init__(self):
#         print('init')
#
#     def foo(self):
#         return "foo = {}".format(self.x)
#
# a = MyClass()
# print(a.foo())
# ===============================================
# class Person:
#     x = 'abc'
#     def __init__(self,name,age=18):
#         self.name = name
#         self.y = age
#
#     def show(self,x,y):
#         print(self.name,self.y)
#         # print(4,self.y)
#         # self.y = x
#         # print(5,self.y)
#         # print(6,Person.x)
#         Person.x = x
#         # print(7,Person.x)
#
# a = Person('tom')
# b = Person('tom',20)
# # print(a.name,b.name)
# # print(a.x,b.x)
# # print(a == b)
# # print(a is b)
# print(a.y,b.y)
# a.show(100,'a')
# # b.show(200,'b')
# # print(Person.x)
# # print(a.y)
# print(a.__dict__)
# a.y = 200
# print(a.__dict__)
# ====================================
# class Person:
#     x = 'abc'
#
#     def __init__(self,name,age=18):
#         self.name = name
#         self.y = age
#
#     def show(self,x,y):
#         print(self.name,self.y)
#         self.y = x
#         Person.x = x
#
# a = Person('tom')
# b = Person('jerry',20)
# print(a.__class__,b.__class__)
# print(a.__class__.__qualname__,a.__class__.__name__)
# print(isinstance(a,a.__class__))
# print(int.__class__)
# print(isinstance(b,int.__class__))
# print(Person.__dict__)
# print(a.__dict__)
# print(b.__dict__)
# print(a.__dict__['name'])
# =================================================================
# class Person:
#     age = 3
#     height = 170
#
#     def __init__(self,name,age=18):
#         self.name = name
#         self.age = age
#
# tom = Person('tom')
# jerry = Person('jerry',20)
#
# Person.age = 30
# print(1, Person.age, tom.age, jerry.age)
# print(2, Person.__dict__, tom.__dict__, jerry.__dict__, sep='\n')
# print(3, Person.height, tom.height, jerry.height)
# Person.height += 20
# print(4, Person.height, tom.height, jerry.height)
# print(5, Person.__dict__, tom.__dict__, jerry.__dict__, sep='\n')
# # 到目前为止tom和jerry中还没有新key
# tom.height = 168   # 赋值即定义，在这个实例上定义一个height
# print(6, Person.height, tom.height, jerry.height)
# print(7, Person.__dict__, tom.__dict__, jerry.__dict__, sep='\n')
# # 这时tom中添加了一个新key
# jerry.height += 30   # 开始jerry没有height，它会到Person中拿这个属性再加上30。这样定义破坏了封装
# print(8, Person.height, tom.height, jerry.height)
# # 先查找自己的字典，自己的字典没有就到类字典中找，如果还是没有就报找不到。如果自己有就不找类的了。
# # 先找自己再找自己的类
# print(9, Person.__dict__, tom.__dict__, jerry.__dict__, sep='\n')
# # jerry现在也有了新key
# Person.weight = 70   # 在类上添加一个新属性
# print(10, Person.weight, tom.weight, jerry.weight)
#
# print(11, Person.__dict__['weight'])  # 这没问题，可以找到
# # print(12, tom.__dict__['weight'])  # 这样不行，会报找不到key
# print(13, tom.weight)  # 这样没问题，会到类里找
# =============================================================================================
# 装饰一个类，不是类装饰器
# def setnameproperty(name):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper
#
# @setnameproperty('MY CLASS')
# class MyClass:
#     pass
#
# print(MyClass.__dict__)
# ============================================================================
# 类方法与静态方法
# class MyClass:
#     """this is a class"""
#     xxx = 'XXX'
#
#     # def __init__(self):
#     #     print('init')
#
#     def foo(self):
#         # return "foo = {}".format(self.x)
#         print("foo")
#
#     def bar():
#         print('bar')
#
#     @classmethod
#     def clsmtd(cls,*,a):
#         print('{}.xxx={}'.format(cls.__name__,cls.xxx))
#
#     @staticmethod
#     def staticmtd(x):
#         print('static')
#         MyClass
#
# a = MyClass()
# a.foo()
#
# MyClass.bar()
# print(MyClass.__dict__)
# MyClass.clsmtd(a=123)
# a.clsmtd(a=234)
# # # 因为a实例中没有clsmtd，所以会到类中找。这相当于传入一个a.__class__给cls。这条等价于
# # # a.__class__.clsmtd()
# MyClass.staticmtd(5)
# a.staticmtd(x=5)  # 这样是可以调用的，不会传第一个位置参数
# # # MyClass.clsmtd(a=MyClass())  # 一般不会这样做
# MyClass().clsmtd(a=000)  # MyClass()表示实例化出一个对象，只是没有名字
# 类方法举例
# class Data_test(object):
#     day = 0
#     month = 0
#     year = 0
#     def __init__(self,year=0,month=0,day=0):
#         self.day = day
#         self.month = month
#         self.year = year
#         print('OK')
#
#     def out_date(self):
#         print("year:")
#         print(self.year)
#         print("month:")
#         print(self.month)
#         print("day:")
#         print(self.day)
#
# class Str2IntParam(Data_test):
#     @classmethod
#     def get_date(cls,string_date):
#         year,month,day=map(int,string_date.split('-'))
#         date1=cls(year,month,day)
#         return date1
#
# r = Str2IntParam.get_date("2019-09-06").out_date()
# # r.out_date()
# ====================================================================
# 访问控制
# class Person:
#     def __init__(self,name,age=19):
#         self.name = name
#         self.__age = age
#
#     def growup(self,incr=1):
#         if 0 < incr < 150:
#             self.__age += incr
#
#     def getage(self):
#         return self.__age
#
# tom = Person('tom')
# tom.growup(2)
# # print(tom.age)  # 因为是隐藏属性，所以这里访问不了__age属性
# print(tom.getage())  # 这样就可以访问隐藏属性了
# print(Person.__dict__)
# print(tom.__dict__)
#
# # 代码不要写成下面这样的方式
# tom._Person__age = 200  # 这时类中的检查函数就没用了，还是可以改隐藏属性的值
# print(tom.getage())
#
# tom.age = 300   # 这样是新增一个属性，与类中的__age没有关系
# print(1, tom.getage())
# print(tom.age)
#
# print(tom.__dict__)
# ===========================================================================
# 属性装饰器
class Person:
    def __init__(self,chinese,english,history):
        self._chinese = chinese
        self._eng = english
        self.__his = history

    def seteng(self,v):
        self._eng = v


    @property
    def chinese(self):
        return self._chinese

    @chinese.setter
    def chinese(self,value):
        self._chinese = value

    eng = property(lambda self:self._eng,seteng)


student1 = Person(80,90,88)
print(student1.chinese)
student1.chinese = 100
print(student1.chinese)
print(student1.eng)
student1.eng = 110
print(student1.eng)