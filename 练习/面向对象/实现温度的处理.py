# 思路
# 假定一般情况下，使用摄氏度为单位，传入温度值。
# 如果不给定摄氏度，一定会把温度值转换到摄氏度。
# 温度转换方法可以使用实例的方法，也可以使用类方法，使用类方法的原因是，为了不创建对象，就可以直接进行温度转换计算，这个类设计像个温度工具类。
class Temperature:
    def __init__(self,t,unit='c'):
        self._c = None
        self._f = None
        self._k = None

        if unit == 'k':
            self._k = t
            self._c = self.k2c(t)
        elif unit == 'f':
            self._f = t
            self._c = self.f2c(t)
        else:
            self._c = t

    @property
    def c(self):
        return self._c

    @property
    def k(self):
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k

    @property
    def f(self):
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @classmethod
    def c2f(cls,c):
        return 9*c/5+32

    @classmethod
    def f2c(cls,f):
        return 5*(f-32)/9

    @classmethod
    def c2k(cls,c):
        return c+273.15

    @classmethod
    def k2c(cls,k):
        return k-273.15

    @classmethod
    def f2k(cls,f):
        return cls.c2k(cls.f2c(f))

    @classmethod
    def k2f(cls,k):
        return cls.c2f(cls.k2c(k))

print(Temperature.c2f(40))
print(Temperature.c2k(40))
print(Temperature.f2c(104.0))
print(Temperature.k2c(313.15))
print(Temperature.k2f(313.15))
print(Temperature.f2k(104))

t = Temperature(37)
print(t.c, t.k, t.f)

t = Temperature(300, 'k')
print(t.c, t.k, t.f)