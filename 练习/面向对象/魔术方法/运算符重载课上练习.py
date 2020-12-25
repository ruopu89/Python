# class A:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#     def __isub__(self, other):
#         return A(self.name, self-other)
#
# tom = A('tom')
# jerry = A('jerry', 16)
#
# print(tom-jerry)
# print(jerry-tom, jerry.__sub__(tom))
#
# print(id(tom))
# tom -= jerry
# print(tom.age, id(tom))
# ========================================================
# @functools.total_ordering 装饰器
# from functools import total_ordering
#
# @total_ordering
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
# tom = Person('tom', 20)
# jerry = Person('jerry', 16)
#
# print(tom > jerry)
# print(tom < jerry)
# print(tom >= jerry)
# print(tom <= jerry)
# ================================================
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __ge__(self, other):
#         return self.age >= other.age
#
# tom = Person('tom', 20)
# jerry = Person('jerry', 16)
#
# print(tom > jerry)
# print(tom < jerry)
# print(tom >= jerry)
# print(tom <= jerry)
# print(tom == jerry)
# print(tom != jerry)
# ====================================================
# class A:
#     def __init__(self,x):
#         self.x = x
#
#     def __sub__(self, other):
#         # self.x = self.x - other.x
#         # return self
#         return self.x - other.x
#
#     def __ne__(self, other):
#         return self.x != other.x
#
#     def __eq__(self, other):
#         return self.x == other.x
#
#     def __lt__(self, other):
#         return self.x < other.x
#
#     def __str__(self):
#         return str(self.x)
#
#     def __iadd__(self, other):
#         self.x = self.x + other.x
#         return self
#
#     __repr__ = __str__
#
# a1 = A(4)
# a2 = A(10)
# a3 = A(6)
#
# # print(a1.__sub__(a2))
# # print(a1-a2)
#
# # print(a1 == a2)
# # print(a1 != a2)
#
# lst = [a1, a2, a3]
# # print(sorted(lst))
# # print(list(reversed(sorted(lst))))
#
# a1 += a2
# print(a1)
# ===============================================
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __show__(self):
        print('self {} {}'.format(self.x, self.y))
        return self

    def __str__(self):
        print(123)
        return '{}'.format(self.x)

    __repr__ = __str__

p = A(3, 54)
print(p.__show__())