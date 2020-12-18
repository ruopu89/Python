# 1. Shape基类，要求所有子类都必须提供面积的计算，子类有三角形、矩形、圆。
# 2. 上题圆类的数据可序列化

# 思路
# 既然是基类，那么就应该有一个东西大家共同继承是最好的。都需要计算面积，面积可以是一个属性，也可以是一个方法。属性有两种东西，一种是真正的属性，一种是property装饰的属性，装饰的属性就是个方法。计算面积本来就是个动作，每一个子类都应该继承父类这个动作，至少应该实现一个求面积的方法，如何让这个动作像个属性暴露给别人，一调用就出来呢，这就需要装饰器
import math
import json
import msgpack

class Shape:
    @property
    def area(self):
        raise NotImplementedError('基类未实现')

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        p = (self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

def SerializableCircle(cls):
    def wrapper(self,t='json'):
        if t == 'json':
            return json.dumps(self.__dict__)
        elif t == 'msgpack':
            return msgpack.packb(self.__dict__)
        else:
            raise NotImplementedError('没有实现的序列化')
        # print('OKOKOKOK')
    cls.xulei = wrapper  # cls.xulei就是wrapper，所以调用时要向cls.xulei()中传入参数t的值，否则就使用默认值
    return cls

@SerializableCircle
class Circle(Shape):
    def __init__(self, radius):
        self.d = radius * 2
        # self.t = t

    @property
    def area(self):
        return math.pi * self.d * self.d * 0.25

scm = Circle(5)
print(scm.xulei('msgpack'))
print(scm.xulei())




# shapes = [Triangle(3,4,5), Rectangle(3,4), Circle(4)]
# for s in shapes:
#     print('The area of {} = {}'.format(s.__class__.__name__, s.area))



# class SerializableMixin:
#     def dumps(self, t='json'):
#         if t == 'json':
#             return json.dumps(self.__dict__)
#         elif t == 'msgpack':
#             return msgpack.packb(self.__dict__)
#         else:
#             raise NotImplementedError('没有实现的序列化')
#
# class SerializableCircleMixin(SerializableMixin,Circle):
#     pass

# scm = SerializableCircleMixin(4)
# print(scm.area)
# s = scm.dumps('msgpack')
# print(s)
# s = scm.dumps('json')
# print(s)
# scm = Circle(4)
# print(scm)