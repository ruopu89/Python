# 使用随机整数生成类，随机生成20个数字，两两配对形成二维坐标系的坐标，把这些坐标组织起来，并打印输出
import random

class RandomGen:
    @classmethod
    def randmGen(cls,start=1,stop=100,count=20):
        while True:
            return [random.randint(start,stop) for _ in range(count)]
            # yield random.randint(start, stop)

# rg = RandomGen.randmGen()
# print(next(a))

# for _ in range(10):
#     print(next(rg))
# print(RandomGen.randmGen())
# for i in RandomGen.randmGen():
#     print(next(i))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return '{}:{}'.format(self.x,self.y)
    #
    # def __repr__(self):
    #     return '{}:{}'.format(self.x,self.y)

lst1 = [Point(x,y) for x,y in zip(RandomGen.randmGen(10),RandomGen.randmGen(10))]
print(lst1)
for p in lst1:
    print(p.x,p.y)
    print(p)