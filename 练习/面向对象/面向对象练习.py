# 1.随机整数生成类
# 可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数
import random
#
# class GetRandom:
#     def __init__(self, start=1, end=100, count=10):
#         self.start = start
#         self.end = end
#         self.range = count
#
#     def getrandom(self, start=1, end=100, rang=10):
#         return [random.randint(start, end) for _ in range(rang)]
#
#
# a = GetRandom()
# print(a.getrandom())
# print(a.__dict__)
# =================================================
# class RandomGen:
#     @classmethod
#     # @staticmethod
#     def generate(cls, start=1, stop=100, count=10):
#         return [random.randint(start, stop) for x in range(count)]
#
# b = RandomGen()
# print(b.generate())
# 2. 随机整数生成类，可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数。使用生成器实现
# import random
#
# class RandomGenerator:
#     def __init__(self, count=10, start=1, stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#
#     def generate(self):
#         for _ in range(self.count):
#             # return random.randint(self.start, self.stop)
#             yield random.randint(self.start, self.stop)
#
# rg = RandomGenerator()
# gen = rg.generate()
# print(type(gen))
# ========================================================================
# import random
#
# class RandomGenerator:
#     def __init__(self, count=10, start=1, stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#         self._gen = self._generator()
#
#     def _generator(self):
#         while True:
#             yield random.randint(self.start, self.stop)
#
#     def generate(self):
#         return [next(self._gen) for _ in range(self.count)]
#
# rg = RandomGenerator(20,1,1000)
# print(rg.generate())
# ========================================================================
# import random
# class RandomGenerator:
#     def __init__(self, count=10, start=1, stop=100):
#         self.count = count
#         self.start = start
#         self.stop = stop
#         self._gen = self._generator()
#
#     def _generator(self):
#         while True:
#             yield [random.randint(self.start, self.stop) for i in range(self.count)]
#
#     def generate(self, count):
#         self.count = count
#         return next(self._gen)
#
# rg = RandomGenerator(15, 20, 30)
# print(rg.generate(10))
# ==========================================================
# 使用生成器实现1
# import random
#
# class RandomGenerator:
#     def __init__(self, count=10, start=1, stop=20):
#         self.count = count
#         self.start = start
#         self.stop = stop
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield random.randint(self.start, self.stop)
#
#     def generate(self, count=0):
#         if count <= 0:
#             print(self._gen,'---')
#             return [next(self._gen) for i in range(self.count)]
#         else:
#             return [next(self._gen) for i in range(count)]
#
# a = RandomGenerator()
# print(a.generate())
# print(a.generate(5))
# print(a.__dict__)
# ========================================================================
# import random
#
# class RandomGenerate:
#     def __init__(self, count=10, start=1, stop=30):
#         self.count = count
#         self.start = start
#         self.stop = stop
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield [random.randint(self.start, self.stop)  for _ in range(self.count)]
#
#     def generate(self, count=0):
#         if count > 0:
#             self.count = count
#         return [next(self._gen)]
#
# a = RandomGenerate()
# print(a.generate())
# print(a.generate(3))
# =======================================================
# import random
#
# class RandomGenerate:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:
#             yield [random.randint(self.start, self.stop) for i in range(self.patch)]
#
#     def generate(self):
#         return next(self._gen)
#
#     @property
#     def _patch(self):
#         return self.patch
#
#     @_patch.setter
#     def _patch(self, value):
#         self.patch = value
#
# rg = RandomGenerate()
# print(rg.generate())
# rg._patch = 5
# print(rg.generate())
# print(rg.__dict__)

# 3. 打印坐标。使用上题中的类，随机生成20个数字，两两配对形成二维坐标系的坐标，把这些坐标组织起来，并打印输出
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return '{}:{}'.format(self.x, self.y)
#
#     # def __repr__(self):
#     #     return '{}:{}'.format(self.x, self.y)
#
# lst1 = [Point(x,y) for x,y in zip(rg.generate(10), rg.generate(10))]
# print(lst1)
#
# for p in lst1:
#     print(p.x, p.y)
# =========================================================================
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# points = [Point(x,y) for x,y in zip(RandomGenerator().generate(15),RandomGenerator().generate(15))]
#
# for p in points:
#     print('{}:{}'.format(p.x, p.y))
# ============================================================
# 3. 车辆信息。记录车的品牌mark、颜色color、价格price、速度speed等特征，并实现增加车辆信息、显示全部车辆信息的功能
# class Car:
#     def __init__(self, mark, color, price, speed):
#         self.mark = mark
#         self.color = color
#         self.price = price
#         self.speed = speed
#
#     def _add(self):
#         carinfo = {}
#         carinfo['mark'] = self.mark
#         carinfo['color'] = self.color
#         carinfo['price'] = self.price
#         carinfo['speed'] = self.speed
#         # carinfo = []
#         # carinfo.append(self.mark)
#         # carinfo.append(self.color)
#         # carinfo.append(self.price)
#         # carinfo.append(self.speed)
#         print(carinfo)
#         return carinfo
#
#     def add(self):
#         return self._add()
#
#     @property
#     def carinf(self):
#         return self._add()
#
#     @carinf.setter
#     def carinf(self,price):
#         return self.price
#
#
# a = Car('awsaa','red',100,400)
# print(a.add())
# print(a.carinf)
# a.carinf = 500
# print(a.carinf)
# ==================================================================
# class Car:
#     def __init__(self, mark, speed, color, price):
#         self.mark = mark
#         self.speed = speed
#         self.color = color
#         self.price = price
#
# class CarInfo:
#     def __init__(self):
#         self.lst = []
#
#     def addcar(self, car:Car):
#         self.lst.append(car)
#
#     def getall(self):
#         print(self.lst)
#         return self.lst
#
#     def __repr__(self):
#         return '{},{}'.format(self.lst[0],self.lst[1])
#
# ci = CarInfo()
# car = Car('audi', 400, 'red', 100)
# ci.addcar(car)
# ci.getall()
# print(ci.lst)
# ==================================================================
# class Car:
#     def __init__(self, mark, speed, color, price):
#         self.mark = mark
#         self.speed = speed
#         self.color = color
#         self.price = price
#
# class CarInfo:
#     def __init__(self):
#         self.info = []
#
#     def addcar(self, car:Car):
#         self.info.append(car)
#
#     def getall(self):
#         return self.info
#
# ci = CarInfo()
# car = Car('audi', 400, 'red', 100)
# ci.addcar(car)
# print(type(ci.getall()))
# if __name__ == '__main__':
#     print(ci.getall())
# =======================================================
# 5. 实现温度的处理
# 思路
# 假定一般情况下，使用摄氏度为单位，传入温度值。
# 如果不给定摄氏度，一定会把温度值转换到摄氏度。
# 温度转换方法可以使用实例的方法，也可以使用类方法，使用类方法的原因是，为了不创建对象，就可以直接进行温度转换计算，这个类设计像个温度工具类。
# class Temperature:
#     def __init__(self, t, unit='c'):
#         self._c = None
#         self._f = None
#         self._k = None
#
#         if unit == 'k':
#             self._k = t
#             self._c = self.k2c(t)
#         elif unit == 'f':
#             self._f = t
#             self._c = self.f2c(t)
#         else:
#             self._c = t
#
#     @property
#     def c(self):
#         return self._c
#
#     @property
#     def k(self):
#         if self._k is None:
#             self._k = self.c2k(self._c)
#         return self._k
#
#     @property
#     def f(self):
#         if self._f is None:
#             self._f = self.c2f(self._c)
#         return self._f
#
#     # 温度转换
#     @classmethod
#     def c2f(cls, c):
#         return 9*c/5 + 32
#
#     @classmethod
#     def f2c(cls, f):
#         return 5*(f-32)/9
#
#     @classmethod
#     def c2k(cls, c):
#         return c + 273.15
#
#     @classmethod
#     def k2c(cls, k):
#         return k - 273.15
#
#     @classmethod
#     def f2k(cls, f):
#         return cls.c2k(cls.f2c(f))
#
#     @classmethod
#     def k2f(cls, k):
#         return cls.c2f(cls.k2c(k))
#
# print(Temperature.c2f(40))
# print(Temperature.c2k(40))
# print(Temperature.f2c(104.0))
# print(Temperature.k2c(313.15))
# print(Temperature.k2f(313.15))
# print(Temperature.f2k(104))
# # 上面这些print都是工具，下面两个是当属性装饰器来用，设计应该是这样的。
# t = Temperature(37)
# print(t.c, t.k, t.f)
#
# t = Temperature(300, 'k')
# print(t.c, t.k, t.f)
# ===================================================================
# 6. 模拟购物车购物
# 思路
# 购物车购物，分解得到两个对象`购物车`、`物品`，一个操作`购买`。
# 购买不是购物车的行为，其实是人的行为，但是对于购物车来说就是`增加add`。
# 商品有很多种类，商品的属性多种多样，怎么解决？
# 购物车可以加入很多不同的商品，如何实现？
# class Color:
#     RED = 0
#     BLUE = 1
#     GREEN = 2
#     GOLDEN = 3
#     BLACK = 4
#     OTHER = 1000
#
# class Item:
#     def __init__(self, **kwargs):
#         self.__spec = kwargs
#
#     def __repr__(self):
#         return str(sorted(self.__spec.items()))
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def additem(self, item:Item):
#         self.items.append(item)
#
#     def getallitems(self):
#         return self.items
#
# mycart = Cart()
# myphone = Item(mark='Huawei', color=Color.GOLDEN, memory='4G')
# mycart.additem(myphone)
#
# mycar = Item(mark='Red Flag', color=Color.BLACK, year=2017)
# mycart.additem(mycar)
#
# print(mycart.getallitems())

# ================================================================================