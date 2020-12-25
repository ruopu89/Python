# class A(dict):
#     def __missing__(self, key):
#         print('Missing key :', key)
#         return 0
#
# a = A()
# print(a['k'])
# 将购物车类改造成方便操作的容器类
class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def additem(self, item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return  self.items[index]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __str__(self):
        return str(self.items)

    def __add__(self, other):
        self.items.append(other)
        return self

cart = Cart()
cart.additem(1)
cart.additem('abc')
cart.additem(3)

# print(len(cart))
# print(bool(cart))
# print(cart)
# for x in cart:
#     print(x)
# print(3 in cart)
# print(2 in cart)
# print(cart[1])
# cart[1] = 'xyz'
# print(cart)
print(cart + 4 + 5 + 6)
print(cart.__add__(17).__add__(18))