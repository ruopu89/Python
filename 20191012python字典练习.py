# 字典是可变的，无序的，key不重复。item指kv对。字典是唯一的内置映射类型

# names = ['Alice','Beth','Cecil','Dee-Dee','Earl']
# numbers = ['2314','9191','23423','1230','3333']
# print(numbers[names.index('Cecil')])

# 初始化/定义

# phonebook = {'Alice':1234,'Beth':'90129','Cecil':'123456'}
# print(phonebook['Alice'])

# l1 = list(range(5))
# # d = dict(l1)
# # print(d)
# # 问题是l1是一个序列，但不是二元组。
# d = dict(enumerate(l1))
# print(d)

# e = enumerate(l1)
# print(type(e))
# for x in e:
#     print(x)

# f = dict(e)
# print(f)

# e = enumerate(l1)
# f = dict(e)
# print(f)

# g = {('a',1)}
# print(g)

# h = dict(((1,'a'),))
# print(h)

# items = [('name','gumby'),('age',32)]
# a = dict(items)
# print(a)
# print(a['name'])
# # 调用字典对象的方法的时候，键一定要有单引号？

# l = dict(name='abc',age=21)
# print(l['name'])

# **循环遍历所有的key**
dict = {'k1':'v1','k2':'v2','k3':'v3'}
for k in dict:
    print(k)

for k in dict.keys():
    print(k)

# **循环遍历所有value**
for k in dict:
    print(dict[k])

for k in dict.keys():
    print(dict.get(k))

for v in dict.values():
    print(v)

# **循环遍历出所有的key和value**
for k in dict:
    print(k,dict[k])

for k,v in dict.items():
    print(k,v)

for item in dict.items():
    print(item)

for item in dict.items():
    print(item[0],item[1])

for k,_ in dict.items():
    print(k)

for _,v in dict.items():
    print(v)

# 请在字典中增加一个键值对,"k4":"v4"，输出添加后的字典
dict['k4'] = 'v4'
print(dict)

# 请删除字典中键值对"k1":"v1",并输出删除后的结果
dict.pop("k1")
# key存在，移除它，并返回它的value;key不存在，返回给定的default;default未设置，key不存在则抛出KeyError异常
print(dict)

del dict['k2']
print(dict)
# del dict['k2']看着像删除了一个对象，本质上减少了一个对象的引用，del实际上删除的是名称，而不是对象

# 请删除字典中键"k5"对应的键值对，如果字典中不存在键"k5",则不报错，返回None
w = dict.pop('k5',None)
print(w)

print("删除不存在的k5,不报错，返回值: ",dict.pop("k5",None))

# 请获取字典中"k3"对应的值
print(dict['k3'])

# 请获取字典中"k6"对应的值,如果不存在，则不报错，并且让其返回None。
print(dict.get('k6',None))

# 现有dict2 = {"k1":"v11","a":"b"},通过一行操作使dict2 = {"k1":"v1","k2":"v2","k3":"v3","a":"b"}
dict = {"k1":"v1","k2":"v2","k3":"v3"}
dict2 = {"k1":"v11","a":"b"}
dict2.update(dict)
print("dict: ",dict)
print("dict2: ",dict2)

# 组合嵌套题。写代码，有如下列表，按照要求实现每一个功能
lis = [["k",["qwe",20,{"k1":["tt",3,"1"]},89],"ab"]]
# 10.1、将列表中的"tt"改为大写(用两种方法)
# 10.2、将列表中的字符串"1"变成数字101(用两种方法)
# 10.3、将数字3变成字符串'100'(用两种方法)

# 10.1 方法1:
print(lis[0][1][2].get("k1")[0].upper())
# 10.1 方法2:
print(lis[0][1][2].get("k1")[0].swapcase())

# 10.2 方法1:
lis[0][1][2]["k1"][2] = 101
print(lis)
# 10.2 方法2:
lis[0][1][2].get("k1")[2]=101
print(lis)

# 10.3 方法1：
lis[0][1][2].get('k1')[1] = '100'
print(lis)
# 10.3 方法2：
lis[0][1][2]['k1'][1] = '100'
print(lis)

# 20191015
# 字典是可变的，无序的，key不重复。item指kv对。字典是唯一的内置映射类型

phonebook = {'Alie':123,'Beth':'1238','Cecil':10923}
print(phonebook['Cecil'])

del(dict)
# 如果不加入此行，下面执行时会报TypeError: 'dict' object is not callable。网上有人说原因是dict()是python的一个内建函数，
# 如果将dict自定义为一个python字典，在之后想调用dict()函数是会报出“TypeError: 'dict' object is not callable”的错误
# 在jupeter中执行下面的代码并没有问题，在这里单独执行下面代码也没有问题。应该是上面定义过dict，所以这里再次定义会报错
d = dict(enumerate(list(range(5))))
print(d)
