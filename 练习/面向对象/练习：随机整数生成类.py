# 可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数
# import random
#
# class produceRandom:
#     def __init__(self):
#         # self.quantity = quantity
#         # self.start = start
#         # self.end = end1
#         print('oooooooooooooo')
#
#     def produceRa(self,start,end2,quantity):
#         return [random.randint(start,end2) for x in range(quantity)]
#
# # tom = produceRandom(20,1,11)
# tom = produceRandom()
# print(tom.produceRa(10,100,10))

# ,quantity,start,end1
# ===========================================================
# 类方法
# 自己写的
# import random
#
# class Randm:
#     @classmethod
#     def randmGen(cls,start,stop):
#         return [random.randint(start,stop) for _ in range(10)]
#
# a = Randm.randmGen(1,100)
# print(a)
# ===================================================================
# 使用生成器实现1
# import random
#
# class RandomGenerator:
#     def __init__(self,count=10,start=1,stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#
#     def generate(self):
#         for _ in range(self.count):
#             yield random.randint(self.start,self.stop)
#
# rg = RandomGenerator(count=22)
# gen = rg.generate()
# # print(next(gen))
# for i,v in enumerate(gen):
#     print(i,v)
# ============================================================
# 使用生成器实现2
# import random

# class RandomGenerator:
#     def __init__(self,count=10,start=1,stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield random.randint(self.start,self.stop)
#
#     def generate(self):
#         return [next(self._gen) for _ in range(self.count)]
#
# rg = RandomGenerator(10,1,100)
# print(rg.generate())
# ==============================================================
# 使用生成器实现3
# import random
#
# class RandomGenerator:
#     def __init__(self,count=10,start=1,stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield [random.randint(self.start,self.stop) for _ in range(self.count)]
#
#     def generate(self,count):
#         self.count = count
#         return next(self._gen)
#
# rg = RandomGenerator()
# print(rg.generate(5))
# =================================================================
# 使用生成器实现4
# import random
#
# class RandomGenerator:
#     def __init__(self,start=1,stop=100,patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield random.randint(self.start,self.stop)
#
#     def generate(self,count=0):
#         if count <= 0:
#             return [next(self._gen) for _ in range(self.patch)]
#         else:
#             return [next(self._gen) for _ in range(count)]
#
# a = RandomGenerator()
# print(a.generate())
# print(a.generate(5))
# ====================================================================================
# 使用生成器实现5
# import random
#
# class RandomGenerator:
#     def __init__(self,start=1,stop=100,patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield [random.randint(self.start,self.stop) for _ in range(self.patch)]
#
#     def generate(self,count=0):
#         if count > 0:
#             self.patch = count
#         return next(self._gen)
#
# a = RandomGenerator()
# print(a.generate())
# print(a.generate(5))
# ======================================================================================
# 使用property
import random

class RandomGenerator:
    def __init__(self,start=1,stop=100,patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield [random.randint(self.start,self.stop) for _ in range(self.patch)]

    def generate(self):
        return next(self._gen)

    # @property
    # def patch(self):
    #     return self._patch
    #
    # @patch.setter
    # def patch(self,value):
    #     self._patch = value

    @property
    def _patch(self):
        return self.patch

    @_patch.setter
    def _patch(self,value):
        self.patch = value

a = RandomGenerator()
print(a.generate())
a.patch = 5
print(a.generate())
