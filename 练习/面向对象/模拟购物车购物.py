# 思路
# 购物车购物，分解得到两个对象`购物车`、`物品`，一个操作`购买`。
# 购买不是购物车的行为，其实是人的行为，但是对于购物车来说就是`增加add`。
# 商品有很多种类，商品的属性多种多样，怎么解决？
# 购物车可以加入很多不同的商品，如何实现？
# 拿到需求先区分出对象有哪些，这是一个抽象类的过程。之后分析类之间是如何作用的，每个类自身有什么特点。如果是工具，就可以写成类方法或静态方法，与实例无关。如果要为用户保存一些数据进来，并且实例可能发生变化，这时就要做成实例属性
class Color:
    RED = 0
    BLUE = 1
    GREEN = 2
    GOLDEN = 3
    BLACK = 4
    OTHER = 1000

class Item:
    def __init__(self,**kwargs):
        self.__spec = kwargs

    # def __repr__(self):
    #     return str(sorted(self.__spec.items()))

class Cart:
    def __init__(self):
        self.items = []

    def additem(self,item:Item):
        self.items.append(item)

    def getallitems(self):
        return self.items

mycart = Cart()
myphone = Item(mark='Huawei', color=Color.GOLDEN, memory='4G')
mycart.additem(myphone)

mycar = Item(mark='Red Flag', color=Color.BLACK, year=2017)
mycart.additem(mycar)

print(mycart.getallitems())