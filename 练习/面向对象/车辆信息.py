# 记录车的品牌mark、颜色color、价格price、速度speed等特征，并实现增加车辆信息、显示全部车辆信息的功能
# class Car:
#     def __init__(self,mark,speed,color,price):
#         self.mark = mark
#         self.speed = speed
#         self.color = color
#         self.price = price
#
# class CarInfo:
#     def __init__(self):
#         self.lst = []
#
#     def addcar(self,car:Car):
#         self.lst.append(car)
#
#     def getall(self):
#         return '{}'.format(self.lst)
#
#     def __repr__(self):
#         return '{}'.format(self.lst)
#
#     def __str__(self):
#         return '{}'.format(self.lst)
#
# ci = CarInfo()
# car = Car('audi',400,'red',100)
#
# ci.addcar(car)
# # abc = ci.getall()
# abc = ci.__dict__
# print(type(abc))
# print(abc)
# ==============================================
class Car:  # 记录单一车辆
    def __init__(self, mark, speed, color, price):
        self.mark = mark
        self.speed = speed
        self.color = color
        self.price = price
    # def __init__(self, **kwargs):
    #     self.kwargs = kwargs

    # def __repr__(self):
    #     return str(self.kwargs.items())

    # def __repr__(self):
    #     return '{}:{},{},{}'.format(self.mark,self.speed,self.color,self.price)
        # return str(self.mark), str(self.speed), str(self.color), str(self.price)
    # def __str__(self):
    #     # return str(self.mark,self.speed,self.color,self.price)
    #     return self.mark, self.speed, self.color, self.price

class CarInfo:
    def __init__(self):
        self.info = []

    def addcar(self, car: Car):
        # for i in car.items():
        #     self.info.append(i)
        self.info.append(car)

    def getall(self):
        return '{}/{}/{}/{}'.format(self.info..mark,car.price,car.color,car.speed)


ci = CarInfo()
car = Car(mark='audi', speed=400, color='red', price=100)
# print(car.__dict__,type(car))
# print(car.mark)
ci.addcar(car)
#
abc = ci.getall()
print(abc)
# print(car,type(car))
# print(car)