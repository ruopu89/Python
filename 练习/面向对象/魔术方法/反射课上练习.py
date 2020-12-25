# 有一个Point类，查看它实例的属性，并修改它。动态为实例增加属性
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "Point({}, {})".format(self.x, self.y)
#
#     def show(self):
#         print(self.x, self.y)
#
# p = Point(4, 5)
# # print(p)
# # print(p.__dict__)
# p.__dict__['y'] = 16
# # print(p.__dict__)
# p.z = 10
# # print(p.__dict__)
# # print(dir(p))
# print(sorted(p.__dir__()))
# print(p.__dir__())
# =============================================================
# 使用python提供的方法来实现上面的功能
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "Point({}, {})".format(self.x, self.y)
#
#     def show(self):
#         print(self)
#
# p1 = Point(4, 5)
# p2 = Point(10, 10)
# # print(repr(p1),repr(p2), sep='\n')
# # print(p1.__dict__)
# setattr(p1, 'y', 16)
# setattr(p1, 'z', 10)
# # print(getattr(p1, '__dict__'))
#
# # 动态调用
# # if hasattr(p1, 'show'):
# #     getattr(p1, 'show')()
#
# # 动态增加方法
# if not hasattr(Point, 'add'):
#     setattr(Point, 'add', lambda self,other:Point(self.x + other.x, self.y + other.y))
#
# # print(Point.add)
# # print(p1.add)
# # print(p1.add(p2))
#
# # 为实例增加方法，未绑定
# if not hasattr(p1, 'sub'):
#     setattr(p1, 'sub', lambda self,other:Point(self.x - other.x, self.y - other.y))
#
# # print(p1.sub(p1,p1))
# # print(p1.sub)
# print(p1.__dict__)
# print(Point.__dict__)
# ===============================================================================================
# class Dispatcher:
#     def __init__(self):
#         self._run()
#
#     def cmd1(self):
#         print("I'm cmd1")
#
#     def cmd2(self):
#         print("I'm cmd2")
#
#     def _run(self):
#         while True:
#             cmd = input('Plz input a command: ').strip()
#             if cmd == 'quit':
#                 break
#             getattr(self, cmd, lambda :print('Unknow Command {}.'.format(cmd)))()
#
# Dispatcher()
# ====================================================================================
# __getattr__() 方法测试
# class Base:
#     n = 0
#
# class Point(Base):
#     z = 6
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         print(self.x, self.y)
#
#     def __getattr__(self, item):
#         return "missing {}.".format(item)
#
# p1 = Point(4, 5)
# print(p1.x)
# print(p1.z)
# print(p1.n)
# print(p1.t)
# ================================================
# __setattr__() 方法测试
# class Base:
#     n = 0
#
# class Point(Base):
#     z = 6
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         print(self.x, self.y)
#
#     def __getattr__(self, item):
#         return "missing {}".format(item)
#
#     # def __setattr__(self, key, value):
#     #     print("setattr {}={}".format(key, value))
#
# p1 = Point(4, 5)
# # print(p1.x)
# print(p1.__dict__)
# # print(p1.z)
# # print(p1.n)
# # print(p1.t)
# p1.x = 50
# # print(p1.__dict__)
# p1.__dict__['x'] = 60
# print(p1.__dict__)
# print(p1.x)
#======================================================
# class Point(Base):
#     z = 6
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         print(self.x, self.y)
#
#     def __getattr__(self, item):
#         return  "missing {}.".format(item)
#
#     def __setattr__(self, key, value):
#         print("setattr {}={}".format(key, value))
#         self.__dict__[key] = value
#
# p1 = Point(4,5)
# print(p1.__dict__)
# print(dir(Point))
# ========================================================
# __delattr__()
# class Point:
#     z = 5
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __delattr__(self, item):
#         print('Can not del {}'.format(item))
#
# p = Point(14, 5)
# del p.x
# p.z = 15
# del p.z
# del p.z
# print(Point.__dict__)
# print(p.__dict__)
# del Point.z
# print(Point.__dict__)
# ===============================================================
# __getattribute__
# class Base:
#     n = 0
#
# class Point(Base):
#     z = 6
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getattr__(self, item):
#         return "missing {}".format(item)
#
#     def __getattribute__(self, item):
#         # return item
#         return object.__getattribute__(self, item)
#
# p1 = Point(4, 5)
# print(p1.__dict__)
# print(p1.t)
# print(Point.__dict__)
# print(Point.z)

# ================================================================
# class A():
#     def __init__(self):
#         self.x = 5
#
# a = A()
# setattr(A, 'y', 10)
# # print(A.__dict__)
# # print(a.__dict__)
# # print(getattr(a, 'x'))
# # print(getattr(a, 'y'))
# # print(getattr(a, 'y1', 100))
# # if hasattr(a, 'z'):
# #     print(getattr(a, 'z'))\
# setattr(a, 'y', 1000)
# print(A.__dict__)
# print(a.__dict__)
# print(getattr(a, 'y'))
# print(getattr(A, 'y'))
#
# setattr(a, 'mtd', lambda self:1)
# print(A.__dict__)
# print(a.__dict__)
# a.mtd(3)
# ===============================================
# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __getattr__(self, item):
#         print('__getattr__', item)
#
# print(A(10).x)
# print(A(10).y)
# =================================================
class Base:
    n = 5


class A(Base):
    m = 6

    def __init__(self, x):
        self.x = x

    def __getattr__(self, item):
        print('__getattr__', item)
        # self.__dict__[item]  = # 找不到给一个缺省值

    def __setattr__(self, key, value):
        print(1, key, value)

    # 当设置一个属性的时候，这个setattr方法是一定会被触发的，但是究竟放不放到里面去就是我们的事了

    def __delattr__(self, item):
        print('delattr')  # 删除实例属性


# setattr和delattr是不论是否找到了属性，就会被触发。getattr是如果找到了并且定义了才会被触发，不然即使找到也不会触发。一般delete都是删除自己有的属性，setattr有没有没关系，都可以加进来，getattr如果没有就找不到，应该抛异常的，但是因为有getattr方法，如果找不到getattr就会拦一道，有了这个拦截，异常就没有了。
a = A(10)
# a.x = 100
# a.m = 200
print(2, a.__dict__)
print(3, A.__dict__)
a.y
a.w
# a.z
# a.m
# a.n  # 这是测试__getattr__方法
# del a.x
# del a.m  # 通过实例可以访问到的属性都可以删除