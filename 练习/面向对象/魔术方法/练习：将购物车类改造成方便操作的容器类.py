class Item:
    def __init__(self, name, **kwargs):
        self.name = name
        self._spec = kwargs

    def __repr__(self):
        return "{} = {}".format(self.name, self._spec.values())

class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def additem(selfself, item):
        self.items.append(item)

    def __add__(self, other):
        # print(other)
        # if isinstance(other, Item):
        # print(1, other, 1)
        self.items.append(other)
        return self

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        print(key, value)
        self.items[key] = value

    def __iter__(self):
        return iter(self.items)

    def __missing__(self, key):
        print("key="+key)

    def __repr__(self):
        return str(self.items)

cart = Cart()
# print(cart.__dict__)
# print(cart)
print(cart+2+3 + 4 + 5)
# print(cart.__dict__)
# cart.__add__(2).__add__(3)
# for x in cart:
#     print(x)
print(cart[1])
cart[500] = 500
cart[3] = 400
print(cart[3])