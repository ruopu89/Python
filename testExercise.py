# from pathlib import Path
#
# p = Path('/')
# print(p)
# print(type(p))


# key=lambda x:x[len(x) - 1]
# print(key)

# from setuptools import setup
# find = setup(name='vsftp')
# print(type(dist))

# import socket
# nw = socket.inet_aton('192.168.05.001')
# print(nw,socket.inet_ntoa(nw))

# import re
# s = '''bottle\nbag\nbig\napple'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')
#
# print('---match---')
# result = re.match('b',s)
# print(1, result)
# result = re.match('a',s)
# print(2, result)
# result = re.match('^a',s,re.M)
# print(3,result)
# result = re.match('^a',s,re.S)
# print(4, result)
#
# regex = re.compile('a')
# result = regex.match(s)
# print(5,result)
# result = regex.match(s,15)
# print(6,result)
# print()
#
# print('---search---')
# result = re.search('a',s)
# print(7, result)
# regex = re.compile('b')
# result = regex.search(s,0)
# print(8,result)
# regex = re.compile('^b',re.M)
# result = regex.search(s)
# print(8.5, result)
# result = regex.search(s,8)
# print(9,result)
#
# print('---fullmatch---')
# result = re.fullmatch('bag',s)
# print(10, result)
# regex = re.compile('bag')
# result = regex.fullmatch(s)
# print(11, result)
# result = regex.fullmatch(s,7)
# print(12, result)
# result = regex.fullmatch(s,7,10)
# print(13,result)
#
# print('---findall---')
# result = re.findall('b',s)
# print(14, result)
# regex = re.compile('^b')
# result = regex.findall(s)
# print(15, result)
# regex = re.compile('^b',re.M)
# result = regex.findall(s,7)
# print(16, result)
# regex = re.compile('^b', re.S)
# result = regex.findall(s)
# print(17,result)
# regex = re.compile('^b',re.M)
# result = regex.findall(s,7,10)
# print(18,result)
#
# print('---finditer---')
# result = regex.finditer(s)
# print(type(result))
# print(next(result))
# for i in result:
#     print(i)
#
# print('---sub---')
# regex = re.compile('b\wg')
# result = regex.sub('magedu',s)
# print(1, result)
# result = regex.sub('magedu',s,1)
# print(2,result)
#
# regex = re.compile('\s+')
# result = regex.subn('\t',s)
# print(3,result)

# import re
# s = '''01 bottle
# 02 bag
# 03       big1
# 100        able'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')
#
# print()
#
# print(s.split())
# result = re.split('[\s\d]+',s)
# print(1, result)
# regex = re.compile('^[\s\d]+')
# result = regex.split(s)
# print(2,result)
# regex = re.compile('^[\s\d]+',re.M)
# result = regex.split(s)
# print(3,result)
# regex = re.compile('\s+\d+\s+')
# result = regex.split(' ' + s)
# print(4,result)
# for i in result:
#     print(i,'!!!')

# import re
# s = '''bottle\nbag\nbig\napple'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')
# print()
#
# regex = re.compile('(b\w+)')
# result = regex.match(s)
# print(result)
# print(1,'match',result.groups())
#
# result = regex.search(s, 1)
# print(2, 'search', result.groups())
#
# regex = re.compile('(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)')
# result = regex.match(s)
# print(3,'match',result)

# d = {}
# print(type(d))
# # d['d'] = 1
# d['d'] += 1
# print(d)

# print('\x01')

# import datetime
#
# line = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-"
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
#
# CHARS = set(" \t")
#
# def makekey(line:str):
#     start = 0
#     skip =False
#     for i,c in enumerate(line):
#         if not skip and c in '"[':
#             start = i + 1
#             skip = True
#         elif skip and c in '"]':
#             skip = False
#             yield line[start:i]
#             start = i + 1
#             continue
#
#         if skip:
#             continue
#
#         if c in CHARS:
#             if start == i:
#                 start = i + 1
#                 continue
#             yield line[start:i]
#             start = i + 1
#     else:
#         if start < len(line):
#             yield line[start:]
#
# names = ('remote','','','datetime','request','status','length','','useragent')
#
# ops = (None,None,None,lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
#       lambda request: dict(zip(['method','url','protocol'],request.split())),
#       int,int,None,None
#       )
# # test=datetime.datetime.strptime('19/Feb/2013:10:23:29 +0800', '%d/%b/%Y:%H:%M:%S %z')
# # print(test)
# test=lambda item: (item[0], item[2](item[1]) if item[2] is not None else item[1])
# test1=zip(names, makekey(line),ops)
# print(type(test))
# print(list(test1))
# print(test(('datetime', '19/Feb/2013:10:23:29 +0800', lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'))))

# test=zip(names,makekey(line),ops)
# for i in map(lambda item:(item[0],item[2](item[1]) if item[2] is not None else item[1]),zip(names,makekey(line),ops)):
#     print(type(i))
# print(next(test))
# test=map(lambda item:(item[0],item[2](item[1]) if item[2] is not None else item[1]),zip(names,makekey(line),ops))
# print(next(test))

# test=zip(range(10))
# # print(next(test))
# # print(list(test))
# print(dict(test))

# l1 = [1, 2, 3, 4]
# l2 = [2, 3, 4, 5]
# l3 = zip(l1, l2)
#
# # for i in l3:
# #     print('for循环{}'.format(i))
# l4 = [x for x in l3]
# print(l4)

# line="GET /o2o/media.html?menu=3 HTTP/1.1"
# test=lambda request: dict(zip(['method','url','protocol'],request.split()))
# print(test(line))

# test=lambda item:(item[0], item[2](item[1]) if item[2] is not None else item[1])
# print(test())

# import re
#
# s = '''os.path([path])   sub-path.'''
# s1 = '''r'\\host\mount splitext('.cshrc splitdrive("//host/computer/dir . abc'''
# # lst = re.split('[^-\w]+', s)
# lst = re.split('[^\w-]+', s1)
# print(lst)

# import datetime
#
# logline = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
#
#
# def convert_time(timestr):
#     fmtstr = "%d/%b/%Y:%H:%M:%S %z"
#     dt = datetime.datetime.strptime(timestr, fmtstr)
#     print(dt)
#     return dt
#
# names = ['remote', '', '', 'datetime', 'request', 'status', 'size', '', 'useragent']
#
# ops = [None, None, None, convert_time, None, int, int, None, None]
#
# fields = []
# flag = False
# tmp = ""
#
# # print(fields[10:])
# for word in logline.split():
#     if not flag:
#         if (word.startswith('[') or word.startswith('"')):  # 以[或"开头
#             tmp = word[1:]
#             if word.endswith(']') or word.endswith('"'):
#                 tmp = word.strip('[]"')
#                 fields.append(tmp)
#             else:
#                 flag = True
#         else:
#             fields.append(word)
#         continue
#     if flag:
#         if word.endswith(']') or word.endswith('"'):
#             tmp += " " + word[:-1]  # word.strip[']"']
#             fields.append(tmp)
#
#             tmp = ""
#             flag = False
#         else:
#             tmp += " " + word
#         continue
#
#     # lst.append(word)   # 如何处理[]与"。上面两个条件都用了continue，所以这句没有用了
# # print(fields)
# d = {}
# for i, field in enumerate(fields):
#     key = names[i]
#     if ops[i]:  # 如果ops[i]不是None
#         d[key] = ops[i](field)  # ops[i](field)后面的括号表示一个操作，对field
#         print(field)
#         print(d,'!!!')
#         break
#     d[key] = field  # 如果是None的情况
# # print(type(field))
# # print(type(ops))
# # print(d)

# import re
# import datetime
#
# logline = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)""'''
#
# def extract(line):
#     pattern = '''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "[^"]+" "(?P<useragent>[^"]+)"'''
#     # pattern = '''[\d\.]{7,} - - \[([^\[\]]+)\] "([^"]+)" (\d+)'''
#     regex = re.compile(pattern)
#     matcher = regex.match(line)
#     # print(matcher)
#     return matcher.groupdict()
# print(extract(logline),'***')

# import re
# s = '''bottle\nbag\nbig\napple'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')
# print()
#
# regex = re.compile('b\w+\n(?P<name2>b\w+)\n(?P<name3>b\w+)\n')
# result = regex.match(s)
# # print(1, result.groups())
# print(1, result)
# print(1.5, result.group(1))
# print(2.5, result.groups())
# print(2, result.groupdict())


# logline = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
#
# ops = {
#     'datetime':lambda timestr:datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M:%S %z'),
#     'status':int,
#     'length':int,
#     'request':lambda request:dict(zip(('method','url','protocol'),request.split())),
#     'useragent':lambda useragent:parse(useragent)
# }
#
# data = ops.get()
# print(data)

# class Person:
#     age = 3
#     height = 170
#
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#
# tom = Person('Tom')  # 实例化、初始化
# jerry = Person('Jerry', 20)
#
# Person.age = 30
# print(Person.age, tom.age, jerry.age)  # 输出什么结果
#
# print(Person.height, tom.height, jerry.height)  # 输出什么结果
# jerry.height = 175
# print(Person.height, tom.height, jerry.height)  # 输出什么结果
#
# tom.height += 10
# print(Person.height, tom.height, jerry.height)  # 输出什么结果
#
# Person.height += 15
# print(Person.height, tom.height, jerry.height)  # 输出什么结果
#
# Person.weight += 70
# print(Person.weight, tom.weight, jerry.weight)  # 输出什么结果
#
# print(tom.__dict__['height'])
# print(tom.__dict__['weight'])  # 可以吗

# def add_name(name, cls):
#     cls.NAME = name  # 动态增加类属性


# 改进成装饰器
# def add_name(name):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#
#     return wrapper
#
#
# @add_name('Tom1')
# class Person:
#     AGE = 3
#
#
# print(Person.NAME)

# class Person:
#     @classmethod
#     def class_method(cls):  # cls是什么
#         print('class = {0.__name__}({0})'.format(cls))
#         cls.HEIGHT = 170
#
#
# Person.class_method()
# print(Person.__dict__)

# animal.py
# class Animal:
#     x = 123
#
#     def __init__(self, name):
#         self._name = name
#         self.__age = 10
#         self.weight = 20
#
#
# print('animal Module\'s names = {}'.format(dir()))  # 模块的属性

# cat.py
# import Animal
# from animal import Animal


# class Cat(Animal):
#     x = 'cat'
#     y = 'abcd'
#
#
# class Dog(Animal):
#     def __dir__(self):
#         return ['dog']  # 必须返回可迭代对象
#
#
# print('------------')
# print('Current Module\'s names = {}'.format(dir()))  # 模块名词空间内的属性
# print('animal Module\'s names = {}'.format(dir(animal)))  # 指定模块名词空间内的属性
# print("object's __dict__    = {}".format(sorted(object.__dict__.keys())))  # object的字典
# print("Animal's dir() = {}".format(dir(Animal)))  # 类Animal的dir()
# print("Cat's dir()    = {}".format(dir(Cat)))  # 类Cat的dir()
# print('~~~~~~~~~~~~~~~~')
# tom = Cat('tome')
# print(sorted(dir(tom)))  # 实例tom的属性、Cat类及所有祖先类的类属性
# print(sorted(tom.__dir__()))  # 同上
# # dir()的等价，近似如下，__dict__字典中几乎包括了所有属性
# print(sorted(set(tom.__dict__.keys()) | set(Cat.__dict__.keys()) | set(object.__dict__.keys())))
#
# print("Dog's dir = {}".format(dir(Dog)))
# dog = Dog('snoppy')
# print(dir(dog))
# print(dog.__dict__)
#
# class MyClass:
#     """this is a class"""
#     x = 123
#
#     def foo(self):
#         print(id(self))
#         # print(self.x)
#         # return self.x
#         return self
#
# print(MyClass)
# print(MyClass.__name__)
# print(MyClass.x)
# print(MyClass.foo)
# print(MyClass.__doc__)
# print(type(MyClass))
# print('下面就是实例的东西了')
# a = MyClass()
# print(a.foo)
# print('==============')
# print(a.foo())
# # print(a.x)
# print(id(a))

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
#
# a = MyClass()  # 实例化，初始化
# print(a.foo())

# class Person:
#     x = 'abc'
#     def __init__(self, name, age=18):
#         self.name = name
#         self.y = age
#     def show(self, x, y):
#         print(self.name, self.y, x, y)
#         # return self.name, self.y
#
# a = Person('tom')
# b = Person('tom', 20)
# # print(a.name, b.name)
# # print(a.x, b.x)
# #
# # print(a == b)
# # print(a is b)
# # a.show(100, 'a')
# # b.show(200, 'b')
# print(a.__class__, b.__class__)
# print(a.__class__.__qualname__, a.__class__.__name__)
# print(isinstance(b, a.__class__))
# print(int.__class__)
# print(isinstance(b, int.__class__))
# print(Person.__dict__)
# print(a.__dict__)
# print(b.__dict__)
# print(a.__dict__['name'])

# class Person:
#     age = 3
#     height = 170
#
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#
# tom = Person('tom')
# jerry = Person('jerry', 20)
#
# Person.age = 30
# print(Person.age, tom.age, jerry.age)
# print(Person.height, tom.height, jerry.height)
# Person.height += 20
# print(Person.height, tom.height, jerry.height)
# tom.height = 168
# print(Person.height, tom.height, jerry.height)
# jerry.height += 30
# print(Person.height, tom.height, jerry.height)

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

# class MyClass:
#     """this is a class"""
#     x = 123
#
#     def __init__(self):  # 初始化
#         print('init')
#
#     def foo(self):
#         return "foo = {}".format(self.x)
#
#     def bar():
#         print('bar')
#
#
# a = MyClass()  # 实例化，初始化
# print(a.foo())
#
# MyClass.bar()
# print(MyClass.__dict__)

# class MyClass:
#     """this is a class"""
#     xxx = 'XXX'
#
#     def foo(self):
#         print("foo")
#
#     def bar():  # 不建议这样使用
#         print('bar')
#
#     @classmethod  # 类方法
#     def clsmtd(cls):  # cls是自动加上的
#         print('{}.xxx={}'.format(cls.__name__, cls.xxx))
#
#
# a = MyClass()  # 实例化，初始化
# a.foo()
#
# MyClass.bar()
# print(MyClass.__dict__)
# MyClass.clsmtd()
# a.clsmtd()

# class Person:
#     def __init__(self, name, age=18):
#         self._name = name
#         self.__age = age
#
#     def __growup(self, incr=1):
#         if 0 < incr < 150:
#             self.__age += incr
#
#     def getage(self):
#         return self.__age
#
# tom = Person('tom')
# # tom.growup(2)
# print(Person.__dict__)
# print(tom.getage())
# # print(Person.__dict__)
# tom._name = 'jerry'
# print(tom._name)
# print(tom.__dict__)
# tom._Person__age = 200
# print(tom.getage())

# import random
#
#
# class RandomGenerator:
#     def __init__(self, count=10, start=1, stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#
#     def generate(self):
#         for _ in range(self.count):
#             yield random.randint(self.start, self.stop)
#
#
# rg = RandomGenerator()
# # print(type(rg.generate()))
# gen = rg.generate()  # 因为rg.generate()是生成器，所以要给一个变量
# # print(next(gen))
# # print(rg.count)
# print(next(gen))


# import random
#
#
# class RandomGenerator:
#     def __init__(self, count, start=1, stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield [random.randint(self.start, self.stop) for _ in range(self.count)]
#
#     def generate(self):
#         # self.count = count
#         return next(self._gen)
#
# rg = RandomGenerator(3)
# print(rg.generate())


# class Animal:
#     x = 123
#
#     def __init__(self, name):
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
#
# class Cat(Animal):
#     x = 'cat'
#
#     def shout(self):  # override
#         print('miao')
#
#
# class Garfield(Cat):
#     pass
#
#
# class PersiaCat(Cat):
#     # def __init__(self):
#     #		self.eyes = 'Blue'
#     pass
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog run')
#
#
# tom = Garfield('tom')
# print(tom.name)
# print(tom.shout())
# print(tom.__dict__)
# print(Garfield.__dict__)
# print(Cat.__dict__)
# print(Animal.__dict__)

# class Document:
#     def __init__(self, content):
#         self.content = content
#
#     def print(self):
#         print(self.content)
#
# class Word(Document):
#     pass
#
# class PrintableWord(Word):
#     def print(self):
#         print('Word print {}'.format(self.content))
#
# class Pdf(Document):
#     pass

# print(Word.mro())
# word = Word('test\nabc')
# print(str(word))

# print(PrintableWord.mro())
# word = PrintableWord('test\nabc')
# print(word.__dict__)

import datetime
import time

def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        dst.__qualname__ = src.__qualname__
        return dst
    return _copy
# 这个函数是为了保存原函数的属性的，被传入的函数叫src，被传入的函数的参数叫dst

def logger(duration):
# 这里前面的duration与后面的duration不是同一个，前面是logger函数的形参，后面的是匿名函数的形参
    func=lambda name,duration:print('{} to ok {}s'.format(name,duration))
    # print(duration, func)
    def _logger(fn):
        @copy_properties(fn)   # wrapper = wrapper(fn)(wrapper)
        def wrapper(*args,**kwargs):
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > duration:
                func(fn.__name__,delta)
           # 向匿名函数中传递两个参数，一个是执行函数的名称，一个是实际执行的时间
            print(fn.__name__)
            return ret
        return wrapper
    return _logger

@logger(3)  # add = logger(5)(add)
def add(x,y):
    time.sleep(3)
    return x + y

print(add(5,6))

# from functools import wraps
# def logged(func):
#     # @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__)      # 输出 'with_logging'
#         print(func.__doc__)       # 输出 None
#         return func(*args, **kwargs)
#     return with_logging
#
# # 函数
# @logged
# def f(x):
#    """does some math"""
#    return x + x * x
#
# logged(f)
# a = f(3)
# print(a)