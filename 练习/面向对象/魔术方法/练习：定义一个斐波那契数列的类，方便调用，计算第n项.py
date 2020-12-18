# class Fib:
#     def __init__(self):
#         self.items = [0,1,1]
#
#     def __call__(self, index):
#         if index < 0:
#             raise IndexError('Wrong Index')
#         if index < len(self.items):
#             return self.items[index]
#
#         for i in range(3, index+1):
#             self.items.append(self.items[i-1]+self.items[i-2])
#         return self.items
#
# print(Fib()(100))
# ==================================================================================
class Fib:
    def __init__(self):
        self.items123 = ['a','b','c']
        self.items = [0, 1, 1]

    def __call__(self, index):
        # print(1, self[index], self, self.items, self.__dict__)
        return self[index]

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError('Wrong Index')
        if index < len(self.items):
            return self.items[index]

        for i in range(len(self), index+1):
            self.items.append(self.items[i-1] + self.items[i-2])
        # print(2, len(self), index+1, self.items[index], self.items)
        return self.items[index]

    def __str__(self):
        # print(122222)
        return str(self.items)

    __repr__ = __str__

fib = Fib()
# print(fib(3), len(fib), fib)
# print(fib(10), len(fib), fib)
# for i in fib:
#     print(i)
print(fib(5))