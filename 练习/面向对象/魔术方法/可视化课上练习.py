# class A:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return 'repr: {},{}'.format(self.name, self.age)
#
#     def __str__(self):
#         return 'str: {},{}'.format(self.name, self.age)
#
#     def __bytes__(self):
#         # return "{} is {}".format(self.name, self.age).encode()
#         import json
#         return json.dumps(self.__dict__).encode()
#
# print(A('tom'))
# print([A('tom')])
# print(([str(A('tom'))]))
# print('str:a,1')
# s = '1'
# print(s)
# print(['a'],(s,))
# =========================================================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self is other:
            return True
        return self.x == other.x and self.y == self.y

    def __repr__(self):
        return str(123)

    def __str__(self):
        return str('abc')

p1 = Point(4,5)
p2 = Point(5,6)
# print(p1)
lst = [p1,p2]
# for x in lst:
#     print(x)
# print(*lst)
print(list(map(str, lst)))