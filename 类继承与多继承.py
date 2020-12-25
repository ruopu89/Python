# class Animal:
#     def shout(self):
#         print('Animal shouts')
#
# a = Animal()
# a.shout()
#
# class Cat:
#     def shout(self):
#         print('Cat shouts')
#
# c = Cat()
# c.shout()
# ================================================
# class Animal:
#     def __init__(self, name):
#         self._name = name
#
#     def shout(self):
#         print('{} shouts'.format(self.__class__.__name__))
#
#     @property
#     def name(self):
#         return self._name
#
# a = Animal('monster')
# a.shout()
#
# class Cat(Animal):
#     pass
#
# cat = Cat('garfield')
# cat.shout()
# print(cat.name)
#
# class Dog(Animal):
#     pass
#
# dog = Dog('ahuang')
# dog.shout()
# print(dog.name)
# ================================================
# class Animal:
#     __COUNT = 100
#     HEIGHT = 0
#
#     def __init__(self, age, weight, height):
#         self.__COUNT += 1
#         self.age = age
#         self.__weight = weight
#         self.HEIGHT = height
#
#     def eat(self):
#         print('{} eat'.format(self.__class__.__name__))
#
#     def __getweight(self):
#         print(self.__weight)
#
#     @classmethod
#     def showcount1(cls):
#         print(cls.__COUNT)
#
#     @classmethod
#     def __showcount2(cls):
#         print(cls.__COUNT)
#
#     def showcount3(self):
#         print(self.__COUNT)
#
# class Cat(Animal):
#     NAME = 'CAT'
#     __COUNT = 200
#
# c = Cat(3, 5, 15)
# c.eat()
# print(c.HEIGHT)
# c.showcount1()
# # c.showcount2()
# c.showcount3()
# print(c.NAME)
#
# print("{}".format(Animal.__dict__))
# print("{}".format(Cat.__dict__))
# print(c.__dict__)
# print(c.__class__.mro())
# ========================================================
# class Animal:
#     def shout(self):
#         print('Animal shouts')
#
# class Cat(Animal):
#     def shout(self):
#         print('miao')
#
# a = Animal()
# a.shout()
# c = Cat()
# c.shout()
#
# print(a.__dict__)
# print(c.__dict__)
# print(Animal.__dict__)
# print(Cat.__dict__)
# ===========================================================
# class Animal:
#     def shout(self):
#         print('Animal shout')
#
# class Cat(Animal):
#     def shout(self):
#         print('miao')
#
#     def shout(self):
#         print(super())
#         print(super(Cat, self))
#         super().shout()
#         super(Cat, self).shout()
#         self.__class__.__base__.shout(self)
#
# a = Animal()
# a.shout()
# c = Cat()
# c.shout()
#
# print(a.__dict__)
# print(c.__dict__)
# print(Animal.__dict__)
# print(Cat.__dict__)
# =================================================================
# class Animal:
#     @classmethod
#     def class_method(cls):
#         print('class_method_animal')
#
#     @staticmethod
#     def static_method():
#         print('static_method_animal')
#
# class Cat(Animal):
#     @classmethod
#     def class_method(cls):
#         print('class_method_cat')
#
#     @staticmethod
#     def static_method():
#         print('static_method_cat')
#
# c = Cat()
# c.class_method()
# c.static_method()
# ====================================================================
# class A:
#     def __init__(self, a):
#         self.a = a
#
# class B(A):
#     def __init__(self, b, c):
#         self.b = b
#         self.c = c
#
#     def printv(self):
#         print(self.b)
#         # print(self.a)
#
# f = B(200, 200)
# print(f.__dict__)
# print(f.__class__.__bases__)
# f.printv()
# ====================================================================
# class A:
#     def __init__(self, a, d=10):
#         self.a = a
#         self.__d = d
#
# class B(A):
#     def __init__(self, b, c):
#         A.__init__(self, b + c, b - c)
#         self.b = b
#         self.c = c
#
#     def printv(self):
#         print(self.b)
#         print(self.a)
#         # print(self.d)
#
# f = B(200, 300)
# print(f.__dict__)
# print(f.__class__.__bases__)
# f.printv()
# ==============================================================
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         self.__a2 = 'a2'
#         print('A init')
#
# class B(A):
#     pass
#
# b = B()
# print(b.__dict__)
# =============================================================
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         self.__a2 = 'a2'
#         print('A init')
#
# class B(A):
#     def __init__(self):
#         self.b1 = 'b1'
#         print('B init')
#
# b = B()
# print(b.__dict__)
# ==============================================
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         self.__a2 = 'a2'
#         print('A init')
#
# class B(A):
#     def __init__(self):
#         self.b1 = 'b1'
#         print('B init')
#         A.__init__(self)
#
# b = B()
# print(b.__dict__)
# ==============================
# class Animal:
#     def __init__(self, age):
#         print('Animal init')
#         self.__age = age
#
#     def show(self):
#         print(self.__age)
#
# class Cat(Animal):
#     def __init__(self, age, weight):
#         super().__init__(age)
#         print('Cat init')
#         self.age = age + 1
#         self.weight = weight
#         # super().__init__(age)
#
# c = Cat(10, 5)
# c.show()
#
# print(c.__dict__)
# =======================================================
# class Document:
#     def __init__(self, content):
#         self.content = content
#
#     def print(self):
#         raise NotImplementedError()
#
# class Word(Document): pass
# class Pdf(Document): pass
# ============================================================
# class Printable:
#     def print(self):
#         print(self.content)
#
# class Document:
#     def __init__(self, content):
#         self.content = content
#
# class Word(Document): pass
# class Pdf(Document): pass
#
# class PrintableWord(Printable, Word): pass
# print(PrintableWord.__dict__)
# print(PrintableWord.mro())
#
# pw = PrintableWord('test string')
# pw.print()
# print(pw.__dict__)
# ==================================================================
# 使用装饰器增强一个类，把功能给类附加上去，哪个类需要，就装饰它
def printable(cls):
    def _print(cls):
        print(cls.content, '装饰器')
    cls.print = _print
    return cls

class Document:
    def __init__(self, content):
        self.content = content

class Word(Document): pass
class Pdf(Document): pass

@printable
class PrintableWord(Word): pass
print(PrintableWord.__dict__)
print(PrintableWord.mro())

pw = PrintableWord('test string')
pw.print()

@printable
class PrintablePdf(Word): pass