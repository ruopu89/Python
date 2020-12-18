# 帮助文档中,查阅namedtuple,有使用例程
# namedtuple(typename, field_names, verbose=False, rename=False)
	# 命名元组,返回一个元组的子类,并定义了字段
	# field_names可以是空白符或逗号分割的字段的字符串,可以是字段的列表
    # field_names需要是字符串类型
from collections import namedtuple
Point = namedtuple('_Point', ['x', 'y'])
p = Point(11, 22)
print('!!!!!!!!',p,type(p))

Student = namedtuple('Student', ['name','age1','sg'])
tom = Student('tom', 20, 200)
jerry = Student('jerry', 18, 190)
print(tom.name)
print(jerry.age1, jerry.sg)
