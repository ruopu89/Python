# class A:
#     def __init__(self, name, age=18):
#         self.name = name
#
#     def __hash__(self):
#         return 1
#
#     def __eq__(self, other):
#         return self.name == other.name
#
#     def __repr__(self):
#         return self.name
#
# print(hash(A('tom')))
# print(A('tom'),A('tom'))
# print([A('tom'),A('tom')])
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
# s = {A('tom'),A('tom')}
# print(s)
# print({tuple('t'), tuple('t')})
# print({('tom',),('tom',)})
# print({'tom', 'tom'})
# ======================================================
from collections.abc import Hashable

class A:
    X = 123
    def __init__(self, y):
        self.y = y

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.y == other.y

# print(hash(A(5)))
lst = [A(4), A(5)]
# print(lst)
s = set(lst)
# print(len(s))
# print(s)
# for x in s:
#     print(hash(x))

def hash(x):
    print(x%3)

# print(isinstance(A(4), Hashable))