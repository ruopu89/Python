# 1. Spape基类，要求所有子类都必须提供面积的计算，子类有三角形、矩形、圆
# 个人
# class Spape:
#     def __init__(self, long=None, wide=None, high=None, radius=None):
#         self.long = long
#         self.wide = wide
#         self.high = high
#         self.radius = radius
#
# class Triangle(Spape):
#     def __init__(self, bottom, high):
#         self.bottom = bottom
#         self.high = high
#
#     def area(self):
#         return self.bottom * self.high / 2
#
#
# class Rectangle(Spape):
#     def __init__(self, long, wide):
#         self.long = long
#         self.wide = wide
#
#     def area(self):
#         return self.long * self.wide
#
#
#
# class Round(Spape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius * 3.14
#
#
# a = Triangle(3, 5)
# print(a.area())
#
#
# b = Rectangle(5, 5)
# print(b.area())
#
#
# c = Round(5)
# print(c.area())
# =========================================================
# import math
#
# class Shape:
#     @property
#     def area(self):
#         raise NotImplementedError('基类未实现')
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @property
#     def area(self):
#         p = (self.a + self.b + self.c)/2
#         return math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.d = radius * 2
#
#     @property
#     def area(self):
#         return math.pi * self.d * self.d * 0.25
#
# a = Circle(5)
# print(a.__dict__)
# print(a.__class__.__dict__)
# shapes = [Triangle(3, 4, 5), Rectangle(3, 4), Circle(5)]
# for s in shapes:
#     print('The area of {} = {}'.format(s.__class__.__name__, s.area))
# ================================================================================
# 2. 上题圆类的数据可序列化
# import json
# import msgpack
# # 这里需要到环境中安装pip install msgpack
#
# class SerializableMixin:
#     def dumps(self, t='json'):
#         if t == 'json':
#             return json.dumps(self.__dict__)
#         elif t == 'msgpack':
#             return msgpack.packb(self.__dict__)
#         else:
#             raise NotImplementedError('没有实现的序列化')
#
# class SerializableCircleMixin(SerializableMixin, Circle):
#     pass
#
# scm = SerializableCircleMixin(4)
# print(scm.area)
# s = scm.dumps('msgpack')
# print(s)
# s = scm.dumps('json')
# print(s)
# ===============================================================================
# 用面向对象实现LinkedList链表
# 单向链表实现`append`、`iternodes`方法
# 双向链表实现`append`、`pop`、`insert`、`remove`、`iternodes`方法
#
# 参考
# 对于链表来说，第一个结点是一个独立的对象，结点自己知道内容是什么，下一跳是什么。而链表则是一个窗口，
# 它内部闭关一个个结点对象。所以，建议设计2个类，一个结点Node类，一个链表LinkedList类。
#
# 单向链表1
# class SingleNode:
#     def __init__(self, item, next=None):
#         self.item = item
#         self.next = next
#
#     def __repr__(self):
#         return repr(self.item)
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, item):
#         node = SingleNode(item)
#         if self.head is None:
#             self.head = node
#         else:
#             self.tail.next = node
#         self.tail = node
#         return self
#
#     def iternodes(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#
# ll = LinkedList()
# ll.append('abc')
# ll.append(1).append(2)
# ll.append('def')
#
# print(ll.head, ll.tail)
# for item in ll.iternodes():
#     print(item)
# ======================================================================
# 单向链表
# class SinleNode:
#     def __init__(self, item, next=None):
#         self.item = item
#         self.next = next
#
#     def __repr__(self):
#         return repr(self.item)
#
# class SingleNode:
#     def __init__(self, item, next=None):
#         self.item = item
#         self.next = next
#
#     def __repr__(self):
#         return  repr(self.item)
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.items = []
#
#     def append(self, item):
#         node = SingleNode(item)
#         if self.head is None:
#             self.head = node
#         else:
#             self.tail.next = node
#         self.tail = node
#
#         self.items.append(node)
#         return self
#
#     def iternodes(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#
#     def getitem(self, index):
#         return self.items[index]
#
# ll = LinkedList()
# ll.append('abc')
# ll.append(1).append(2).append('def')
#
# print(ll.head, ll.tail)
#
# for item in ll.iternodes():
#     print(item)
#
# for i in range(len(ll.items)):
#     print(ll.getitem(i))
# ===============================================================
# 双向链表
# class SingleNode:
#     def __init__(self, item, prev=None, next=None):
#         self.item = item
#         self.next = next
#         self.prev = prev
#
#     def __repr__(self):
#         return "({} <== {} ==> {})".format(self.prev.item if self.prev else None, self.item, self.next.item if self.next else None)
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def append(self, item):
#         node = SingleNode(item)
#         if self.head is None:
#             self.head = node
#         else:
#             self.tail.next = node
#             node.prev = self.tail
#         self.tail = node
#         return self
#
#     def insert(self, index, item):
#         if index < 0:
#             raise IndexError('Not negative index {}'.format(index))
#         current = None
#         for i,node in enumerate(self.iternodes()):
#             if i == index:
#                 current = node
#                 break
#         else:
#             self.append(item)
#             return
#
#         node = SingleNode(item)
#         prev = current.prev
#         next = current
#
#         if prev is None:
#             self.head = node
#         else:
#             prev.next = node
#             node.prev = prev
#         node.next = next
#         next.prev = node
#
#     def pop(self):
#         if self.tail is None:
#             raise Exception('Empty')
#
#         node = self.tail
#         item = node.item
#         prev = node.prev
#         if prev is None:
#             self.head = None
#             self.tail = None
#         else:
#             prev.next = None
#             self.tail = prev
#         return item
#
#     def remove(self, index):
#         if self.tail is None:
#             raise Exception('Empty')
#
#         if index < 0:
#             raise IndexError('Not negative index {}'.format(index))
#
#         current = None
#         for i,node in enumerate(self.iternodes()):
#             if i == index:
#                 current = node
#                 break
#         else:
#             raise IndexError('Wrong index {}'.format(index))
#
#         prev = current.prev
#         next = current.next
#
#         if prev is None and next is None:
#             self.head = None
#             self.tail = None
#         elif prev is None:
#             self.head = next
#             next.prev = None
#         elif next is None:
#             self.tail = prev
#             prev.next = None
#         else:
#             prev.next = next
#             next.prev = prev
#
#         del current
#
#     def iternodes(self, reverse=False):
#         current = self.tail if reverse else self.head
#         while current:
#             yield current
#             current = current.prev if reverse else current.next
#
# ll = LinkedList()
# ll.append('abc')
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# ll.append('def')
# print(ll.head, ll.tail)
#
# for x in ll.iternodes(True):
#     print(x)
#
# print('=========================================')
#
# ll.remove(6)
# ll.remove(5)
# ll.remove(0)
# ll.remove(1)
#
# for x in ll.iternodes():
#     print(x)
#
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#
# ll.insert(3, 5)
# ll.insert(20, 'def')
# ll.insert(1, 2)
# ll.insert(0, 'abc')
# for x in ll.iternodes():
#     print(x)










