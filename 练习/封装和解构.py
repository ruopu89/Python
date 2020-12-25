# t1 = (1,2)
# t2 = 1,2
# print(type(t1))
# print(type(t2))
#
# a = 4
# b = 5
# temp = a
# a = b
# b = temp
# print(a, b, temp)
#
# lst = [3, 5]
# first, second = lst
# print(first, second)
#
# a,b = 1,2
# a,b = (1,2)
# a,b = [1,2]
# a,b = [10,20]
# a,b = {10,20}
# a,b = {'a':10,'b':20} # 非线性结构也可以解构
# # a,b = {10,20,30}  # 报错：ValueError: too many values to unpack (expected 2)
# a,*b = {10,20,30}
# [a,b] = (1,2)
# [a,b] = 10,20
# (a,b) = {30,40}
#
# lst = list(range(1, 101, 2))
# head, *mid, tail = lst
# *lst2 = lst
# *body, tail = lst
# head, *tail = lst
# # head, *m1, *m2, tail = lst
# head, *mid, tail = "abcdefghijklmn"
# type(mid)
lst = list(range(10))
one, two, three, four, *_, Mtwo, Mone = lst
print(two, four, Mtwo)

lst = [1,(2,3,4),5]
_,(*_,a),_ = lst
print(a)

s = 'JAVA_HOME=/usr/bin'
name,_,path = s.partition('=')
print(name, path)
print(type(name), type(path))
print(s.split('='))
print(s.partition('='))

blun = 0
dlun = 0
lst = [1,9,8,6,3,4,5,2,7]
for i in range(9):  # 0-8
    dlun += 1
    print("大循环，{}".format(dlun))
    for j in range(8-i):  # 0-7, 0-6, 0-5
# 如果j > j+1，就是下面的对调情况，如果j <= j+1，
        if lst[j] > lst[j+1]:
            print("小循环 {}".format(blun), 1, lst)
            lst[j],lst[j+1] = lst[j+1],lst[j]
            print("小循环 {}".format(blun), 2, lst)
            blun += 1
print(lst)

for i in range(len(lst)):
    for j in range(8, 0, -1):
        if lst[j] > lst[j-1]:
            lst[j],lst[j-1] = lst[j-1],lst[j]
print(lst)