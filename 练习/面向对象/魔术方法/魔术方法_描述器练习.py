# class A:
#     def __init__(self):
#         print('A.init')
#         self.a1 = 'a1'
#
# class B:
#     x = A()
#
#     def __init__(self):
#         print('B.init')
#         self.x = 100
#
# print(B.x.a1)
#
# b = B()
# print(B.x.a1)
# print(b.x)
# print(b.x.a1)
# =====================================================
# class A:
#     def __init__(self):
#         print(1, 'A.init')
#         self.a1 = 'a1'
#
#     def __get__(self, instance, owner):
#         print(2, 'A.__get__', self, instance, owner)
#         return self
#
# class B:
#     x = A()
#
#     def __init__(self):
#         print(3, 'B.init')
#         self.x = A()

# print(B.x.a1)
# print(B.x)

# b = B.x
# print(b.__dict__)
# print('----------------+++++++++')
# print(b.__dict__)
# print(b.x)
# print('----------------')
# print(B.x.a1)
# print(b.x)
# print('----------------')
# print(B.x)
# print('----------------')
# print(b.x)
# print('----------------')
# print(b.__dict__)
# print('----------------')
# print(b.mro())
# =============================================
# class A:
#     def __init__(self):
#         print(1, 'A.init')
#         self.a1 = 'a1'
#
#     def __get__(self, instance, owner):
#         print(2, 'A.__get__', self, instance, owner)
#         return self
#
#     def __set__(self, key, value):
#         print(3, 'A.__set__', self, key, value)

    # def __str__(self):
    #     return str(self.x)


# class B:
#     y = A()
#     x = A()
#     def __init__(self):
#         print(4, 'B.init')
#         self.x = 3
#         self.y = 2

    # def __repr__(self):
    #     return str(self)
    #
    # __str__ = __repr__



# print(B.x)
# print('------------------')
# print(B.x.a1)
# print('------------------')
# b = B()
# print('------------------')
# print(B.x)
# print('------------------')
# print(b.y)
# print('------------------')
# b.y = 4
# print('-------===========')
# print(b.__dict__)
# print('------------------')
# print(B.__dict__)
# print('------------------')
# B.y = 12
# print(B.__dict__)
# b.x = 100
# print(b.__dict__)
# print(B.__dict__.items())
# print(B.x)
# print(b.x)
# ================================================================
# 总结
# class A:
#     def __init__(self):
#         print('A.init')
#         self.a1 = 'a1'
#
#     def __get__(self, instance, owner):
#         print(self, instance, owner)
#
#
# class B:
#     x = A()  # B类被扫描完就会生成A实例
#
#     def __init__(self):
#         print('B.init')
#         # self.x = 100
#         self.x = A()
#
#
# # print(B.x.a1)
# print(B.x)
# b = B()
# print(B.x)
# print('===============')
# print(b.x)
# print(b.x.__dict__)
# ================================================
# __set__方法
# class A:
#     def __init__(self):
#         print('A.init')
#         self.a1 = 'a1'
#
#     def __get__(self, instance, owner):
#         print('A.__get__', self, instance, owner)
#         return self
#
#     def __set__(self, instance, value):
#         print('A.__set__', self, instance, value)
#
#
# class B:
#     x = A()  # B类被扫描完就会生成A实例
#
#     def __init__(self):
#         print('B.init')
#         self.x = A()
#         # self.x = 100
#
# print(B.x)
# print(B.x.a1)
#
# b = B()
# print(B.x)
# print(b.x.a1)
#
# print('----------------')
# print(b.__dict__)
# print(B.__dict__)
#
# b.x =400
# print(b.x)
# =================================================
# class A:
#     def __init__(self):
#         print('A.init')
#         self.a1 = 'a1'
#
#     def __get__(self, instance, owner):
#         print('A.__get__', self, instance, owner)
#         return self  # 这里返回self，下面就可以使用b.x.a1了
#
#     def __set__(self, instance, owner):
#         print('A.__set__', self, instance, value)
#
#
# class B:
#     x = A()
#
#     def __init__(self):
#         print('B.init')
#
#     @classmethod
#     def clsmtd(cls):
#         pass
#
#     @staticmethod
#     def stmtd():
#         pass
#
#     @property
#     def age(self):
#         return self.age
#
#
# print(B.__dict__)

# B().age = 500
# ==============================================
# from functools import partial
#
# class StaticMethod:
#     def __init__(self, fn):  # 这样就可以在作为装饰器时把函数当作fn参数传进来了
#         print('a', '-', fn)
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print('b', '--', self, instance, owner)
#         return self.fn
#
#
# class ClassMethod:
#     def __init__(self, fn):  # 这样就可以在作为装饰器时把函数当作fn参数传进来了
#         print(1, '+', fn)
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print(2, '++', self, instance, owner)
#         # return self.fn
#         # return self.fn(owner)   # 写成这样就会调用A.bar，打印出类名并返回None，可以在打印中看到这些
#         return partial(self.fn, owner)   # 这样做只会返回固定的类名称
#
#
# class A:
#     @StaticMethod
#     def foo():
#         print('c', '---', 'static')
#
#     # 这里做完了，就相当于foo = StaticMethod(foo)。未来要用A.foo的方法调用
#
#     @ClassMethod
#     def bar(cls):
#         print(3, '+++', cls.__name__)
#         # pass
#
# f = A()  # 这一句触发了__get__方法。这一句会触发StaticMethod的__init__方法与__get__方法，也会触发ClassMethod类的__init__方法。也就是说在调用A类的时候就已经执行两个@装饰器了
# print(f)
# f()

# f1 = A.bar   # 这时就已经执行了ClassMethod类中__init__方法与__get__方法，是先执行的__init__再执行__get__方法
# print(f)
# f(A)  # A.bar(A)。我们的目录是A.bar()
# A.bar(StaticMethod)
# f1()  # 返回是None类型，因为def bar(cls)没有返回值
# ======================================================================================
# class Typed:
#     def __init__(self, type):
#         self.type = type
# # 各实例保存自己的类型，这样写没有问题
#
#     def __get__(self, instance, owner):
#         pass
#
#     def __set__(self, instance, value):
#         print('T.set', self, instance, value)   # 这里可以拿到传给Person的两个值
#         if not isinstance(value, self.type):
#             raise ValueError(value)  # 这里进行判断，如果不是指定的类型就抛错
# # 判断只在设置值时发生，也就是在__set__方法中发生，在取值时不管，所以写不写__get__，问题不大
# class Person:
#     name = Typed(str)
#     age = Typed(int)   # 这里直播将类型传入Typed类中去判断
#
#     def __init__(self, name:str, age:int):
#         self.name = name
#         self.age = age
#
# p1 = Person('tom', 90)
# # # 这样写不太好，下面改进
# ==============================================================================
import inspect

class Typed:
    def __init__(self, type):
        self.type = type
        print('w', self.type)
# 各实例保存自己的类型，这样写没有问题

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        print('T.set', self, instance, value)   # 这里可以拿到传给Person的两个值
        if not isinstance(value, self.type):
            raise ValueError(value)  # 这里进行判断，如果不是指定的类型就抛错


class TypeAssert:
    def __init__(self, cls):
        self.cls = cls   # 这里是给Person类加一个属性cls。这是在定义好装饰器函数时就会执行的，无需调用
        print(1, self.cls, cls)

    def __call__(self, *args, **kwargs):  # 这里拿传入的Person的两个参数
        params = inspect.signature(self.cls).parameters
        print(2, self.cls.__dict__)   # 可以看出这时的类还没有name和age属性
        for name, param in params.items():
            print(3, name, param.annotation)
            if param.annotation != param.empty:  # 如果Person中__init__方法的值有注解才能检查
                setattr(self.cls, name, Typed(param.annotation))   # Typed类是在这里被触发的，因为打印出了传入初始化方法的类型
                # self.cls.name = Typed(param.annotation)
                print(4, self.cls, self.cls.__dict__)   # 这里可以看到在Person类中加入了两个属性name和age，这两个属性的值是Typed类的实例
        # p = self.cls(name, age)
        print(5, self.cls.__dict__)
        return self.cls(*args, **kwargs)  # self.cls('tom', 77) => self.name = 'tom'

@TypeAssert
class Person:
    # name =
    # age =

    def __init__(self, name:str, age:int):
        self.name = name
        print(0, name)
        self.age = age
        print(0, self.age)

    # def show(self):
    #     return Person.name, Person.age, self.name, self.age

# params = inspect.signature(Person).parameters
# print(params)
# print(inspect.signature(Person))
# print(inspect.signature(Person).parameters)
# for name,param in params.items():
#     print(name, param.annotation)   # 这样就可以拿到类了。param.annotation返回的是类型

p1 = Person('tom', 67)
print(dir(Person('tom', 67).__dict__))
# print(100,
# 实例中并不存在任何内容，因为Person没有返回值，装饰器函数中的setattr(self.cls, name1, Typed(param.annotation))一句是在给类添加属性，触发的也是__set__方法，所以实例的属性是无效的。另外从Person类的初始化方法中打印的结果也可以看出是None。
#
# 
# print(p1)
