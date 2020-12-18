class Fib:
    def __init__(self):
        self.lst = [0,1,1]

    def __len__(self):
        return len(self.lst)

    def __call__(self, x):
        if x < len(self.lst):
            return self.lst

        for i in range(2, x):
            self.lst.append(self.lst[i-1]+self.lst[i])
        return self.lst

    def __getitem__(self, index):
        if index < 0:
            return None
        if index < len(self):
            return self.lst[index]
        return self(index)

    def __iter__(self):
        return iter(self.lst)

a = Fib()
# print(a[10])
# print(a[12])
print(a(4))
print(a(10))
# print(a.lst)
# print(a[3])