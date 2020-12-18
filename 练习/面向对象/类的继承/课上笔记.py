# 继承中的访问控制
# class Animal:
#     __COUNT = 100
#     HEIGHT = 0
#     NAME = '123'
#
#     def __init__(self,age,weight,height):
#         self.__COUNT += 1
#         self.age = age
#         self.__weight = weight
#         self._HEIGHT = height
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
#         return cls.__COUNT
#
#     def showcount3(self):
#         print(self.__COUNT)
#
#     def showcount4(self):
#         print(self.__showcount2())
#
# class Cat(Animal):
#     # NAME = 'CAT'
#     __COUNT1 = 200
#
#     def Cou(self):
#         print(Cat.__COUNT1)
#
# c = Cat(3,5,15)
# # c.eat()
# c.showcount4()
# c.Cou()
# ======================================================
# 方法的重写、覆盖override
# class Animail:
#     def shout(self):
#         print('Animal shouts')
#
# class Cat(Animail):
#     def shout(self):
#         print('miao')
#
# a = Animail()
# a.shout()
# c = Cat()
# c.shout()
# print(Cat.__dict__)
# =========================================================
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
#         super(Cat,self).shout()
#         self.__class__.__base__.shout(self)
#
# a = Animal()
# a.shout()
# c = Cat()
# c.shout()
#
# print(Cat.__dict__)
# ==========================================================
# 继承中的初始化
# class Animal:
#     def __init__(self,age):
#         print('Animal init')
#         self.__age = age
#
#     def show(self):
#         print(self.__age)
#
# class Cat(Animal):
#     def __init__(self,age,weight):
#         super().__init__(age)
#         print('Cat init')
#         self.__age = age+1
#         self.__weight = weight
#
# c = Cat(10,5)
# c.show()
# print(c.__dict__)
# ====================================================
# __mro__ 非常重要，它会保存方法的查找顺序
# print(int.__subclasses__())
# print(int.__bases__)
# print(int.__base__)
# print(int.mro())
# print(bool.mro())
# print(bool.__subclasses__())
# ============================================================
# class Animal:
#     x = 123
#     def __init__(self,name):
#         self._name = name
#         self.__age = 10
#
#     @property
#     def name(self):
#         return self._name
#
#     def shout(self):
#         print('Animal shout')
#
#     @classmethod
#     def clsmtd(cls):
#         print(123, cls, cls.__name__)
#
# class Cat(Animal):
#     x = 'cat'
#     def __init__(self, name):
#         super().__init__(name)
#         self._name1 = "Cat"+name
#         self.__age = 20
#
#     def shout(self):
#         super().shout()
#         super(Cat, self).shout()
#         print('Cat shout')
#
#     @classmethod
#     def clsmtd(cls):
#         print(222, cls, cls.__name__)
#
# class Garfield(Cat):
#     pass
#
# class PersiaCat(Cat):
#     pass
#
# class Dog(Animal):
#     def run(self):
#         print('Dog run')

# tom = Garfield('tom')
# print(tom.__dict__,tom.name)
# print(tom.name)
# print(tom.shout())
# print(tom.__dict__)
# print(Garfield.__dict__)
# print(Cat.__dict__)
# print(Animal.__dict__)
# print(tom.clsmtd())
# dog = Dog('ahuang')
# dog.shout()
# print(dog.x)
# print(dog.__dict__)
# print(dog.__class__.__mro__)
# print(dog.__class__.__bases__)
# =====================================================
# 装饰器方法给类添加功能
# class Document:
#     def __init__(self,content):
#         self.content = content
#
#     def print(self):
#         print(self.content)
#
# class Word(Document): pass
#
# def printable(cls):
#     cls.print = lambda se: print(self.content)
#     return cls
#
# @printable
# class PrintableWord(Word):
#     def __init__(self,content):
#         self.content = content
#
#     # def print(self):
#     #     print('Word print {}'.format(self.content))
#
# class Pdf(Document):
#     pass
#
# # print(PrintableWord.mro())
# # print(Word.mro())
# # word = PrintableWord('test\nabc')
# # print(word.__dict__)
# print(PrintableWord.__dict__)
# a = PrintableWord('abc')
# a.print()
# =========================================================================
# Mixin
class PrintableMixin:
    def print(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        print('{}'.format(self.content))

class Document:
    def __init__(self,content):
        self.content = content

    def print(self):
        print(123, self.content)

def printable(cls):
    def _print(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print('{}'.format(self.content))
    cls.print = _print
    return cls

class Word(Document): pass

@printable
class PrintableWord(Word): pass

class Pdf(Document): pass

class PrintablePdf(PrintableMixin,Pdf): pass

# print(PrintablePdf.mro())
word = PrintablePdf('test\nabc')
# print(word.__dict__)
word.print()