import random

class RandomGenerator:
    def __init__(self, start=1, stop=100, patch=10):
        self.start = start
        self.stop = stop
        self.__patch = patch
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield [random.randint(self.start, self.stop) for _ in range(self.patch)]

    def generate(self):
        return next(self._gen)

    #    @property
    #    def patch(self):
    # 这里定义的方法名称与初始化的名称一样，是为了覆盖初始化的数据。因为这里的调用就是self.patch，和初始化中的
    # 一样。方法的返回值self._patch才是实例dict中保存的内容，实例dict中不会保存patch。这里就是利用相同的调用
    # 方法，用return的属性覆盖了原来的属性，_patch是自定义的，可以是任何值。也可以写成
    # def abc(self): return self.patch，这样也可以改变初始化的patch值，也就是return的属性与初始化的属性
    # 是一样的也可以。
    #        return self._patch
    # 返回值中必须用_patch，或者说不能和这个方法本身的名字重复，不然就会变成递归调用，无法执行。

    #    @patch.setter
    #    def patch(self, value):
    #        self._patch = value

    # 按照课上讲授的方法，还是应该写成下面这样。方法名称是自定义的，而返回的属性是上面定义过的，修改的也是上面定义过的属性
    @property
    def patch(self):
        return self.__patch

    @patch.setter
    def patch(self, value):
        self.__patch = value


a = RandomGenerator()
print(a.generate())
a.patch = 5
print(a.generate())
print("class dict: ", RandomGenerator.__dict__)
print("instance dict: ", a.__dict__)
# a.patch = 9
# print(a.patch)
# print(a.generate())
# print("instance dict: ", a.__dict__)