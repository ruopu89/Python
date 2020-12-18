##### 定义一个斐波那契数列的类，方便调用，计算第n项
# class Fib:
#     def __init__(self):
#         self.items = [0, 1, 1]
#
#     def __call__(self, index):
#         if index < 0:
#             raise IndexError('Wrong Index')
#         if index < len(self.items):
#             return self.items[index]
#
#         for i in range(3, index+1):
#             self.items.append(self.items[i-1] + self.items[i-2])
#         return self.items
#
# print(Fib()(10))

######### 上例中，增加迭代的方法、返回容器长度、支持索引的方法
class Fib:
    def __init__(self):
        self.items = [0, 1, 1]

    def __call__(self, index):
        return self[index]   # 当使用fib(5)，这样调用时，但调用call方法，之后会返回self[index]，self[index]会调用getitem方法，返回实际的数字

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
        return self.items

    def __str__(self):
        return str(self.items)

    __repr__ = __str__

fib = Fib()
abc = Fib()
print(fib(5), len(fib))
print(fib(10), len(fib))
for x in fib:
    print(x)
print(fib)
print(fib[100])
print(abc[10])