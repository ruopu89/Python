# *基础，定义列表
In [2]: lst = list()                                                                                           
In [3]: lst = []                                                                                               
In [4]: lst = [2,6,9,'ab']
In [7]: print(lst)
In [9]: lst = list(range(4))
In [10]: print(lst)
[0, 1, 2, 3]
In [12]: edware = ['Edware Gumby',42]
In [13]: edware
Out[13]: ['Edware Gumby', 42]
In [14]: john = ['John Smith',50]
In [16]: database = [edware,john]
In [17]: database
Out[17]: [['Edware Gumby', 42], ['John Smith', 50]]

# *类型判断
In [20]: a = []                                                                                                
In [21]: type(a) == str                                                                                        
Out[21]: False  
# 这是类型比较的方式
In [23]: type('abc')
Out[23]: str
# 返回类型，而不是字符串
In [24]: type(123)
Out[24]: int

In [25]: isinstance(4,str)
Out[25]: False
# 返回布尔值
In [26]: isinstance(4,(str,bool,int))
Out[26]: True

In [27]: type(1+True)
Out[27]: int

In [28]: type(1+True+2.0)
Out[28]: float

# *索引
In [29]: greeting = 'Hello'                                                                                    
In [30]: greeting[0]
Out[30]: 'H'

In [31]: greeting[-1]
Out[31]: 'o'

In [32]: 'Hello'[1]
Out[32]: 'e'

In [33]: fourth = input('Year:')[3]
Year:1992
In [34]: fourth
Out[34]: '2'
# 只取input的年份的第4位数字

In [35]: months = [ 'January','February','March','April','May','June','July','August','September','October','November','Decemb
    ...: er' ]                                                  
In [36]: endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']                       
In [37]: year = input('Year: ')                                    Year: 2019
In [39]: month = input('Month(1-12): ')                            Month(1-12): 10
In [40]: day = input('Day(1-31): ')
Day(1-31): 18
In [41]: month_number = int(month)
In [42]: day_number = int(day)
In [43]: month_name = months[month_number - 1]
In [43]: month_name = months[month_number - 1]
In [44]: ordinal = day + endings[day_number - 1]
In [45]: print(month_name + ' ' + ordinal + ', ' + year)
October 18th, 2019

# 切片
In [46]: tag = '<a href="http://www.python.org">Python web site</a>'                                                          
In [47]: tag[9:30]                                                 Out[47]: 'http://www.python.org'                                   

In [48]: numbers = [1,2,3,4,5,6,7,8,9,10]                          In [49]: numbers[3:6]                                              Out[49]: [4, 5, 6]                                                                                                      
In [50]: numbers[0:1]                                              
Out[50]: [1]

In [51]: numbers[7:10]                                             
Out[51]: [8, 9, 10]                                                                                            
In [52]: numbers[-3:-1]
Out[52]: [8, 9]

In [53]: numbers[-3:0]
Out[53]: []

In [54]: numbers[-3:]
Out[54]: [8, 9, 10]

In [55]: numbers[:3]
Out[55]: [1, 2, 3]

In [56]: numbers[:]
Out[56]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [57]: numbers[-3:0:-1]
Out[57]: [8, 7, 6, 5, 4, 3, 2]

In [58]: url = input('Please enter the URL: ')
Please enter the URL: http://www.python.org
In [59]: domain = url[11:-4]
In [60]: print("Domain name: " + domain)
Domain name: python

In [62]: numbers[0:10:2]                                           Out[62]: [1, 3, 5, 7, 9]                                                                                                  
In [63]: numbers[3:6:3]                                            
Out[63]: [4]

In [64]: numbers[::4]
Out[64]: [1, 5, 9]

In [65]: numbers[8:3:-1]
Out[65]: [9, 8, 7, 6, 5]

In [66]: numbers[10:0:-2]
Out[66]: [10, 8, 6, 4, 2]

In [67]: numbers[::-2]
Out[67]: [10, 8, 6, 4, 2]

In [68]: numbers[5::-2]
Out[68]: [6, 4, 2]

In [69]: numbers[:5:-2]
Out[69]: [10, 8]

# *序列相加
# 连接操作，将两个列表连接起来；产生新的列表，原列表不变；本质上调用的是__add__()方法
In [70]: [1,2,3] + [4,5,6]
Out[70]: [1, 2, 3, 4, 5, 6]

In [72]: 'Hello,' + 'world!'
Out[72]: 'Hello,world!'

In [73]: [1,2,3] + 'world!'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-73-af07b3753bc6> in <module>
----> 1 [1,2,3] + 'world!'

TypeError: can only concatenate list (not "str") to list
# 不能拼接不同类型的序列。

sentence = input("Sentence: ")
# 这里是要求输入要在框中显示的内容的
screen_width = 80
# screen_width：屏幕宽度
text_width = len(sentence)
# 文本宽度，len用于取字符串宽度
box_width = text_width + 4
# 框的宽度，这里加的数需要自行调整，示例中加了6，但测试打印出的内容没有达到效果
left_margin = (screen_width - box_width) // 2
# 左边缘的宽度，等于屏幕宽度减去框的宽度最后除以2,这是为了使最后的内容居中
print()
# 打印一个空行
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
# ' ' * left_margin是整个内容左边空出来的距离，然后输出一个加号，之后输出"-"，输出的数量是外框的长度减2,因为两侧都有一个加号所以要减2.最后输出一个加号。
print(' ' * left_margin + '| ' + ' ' * text_width  + ' |')
# 实际打印每一行时只要注意左侧的空格数量就可以了。
print(' ' * left_margin + '| ' +       sentence + ' |')
# 通过'| '和' |'使内容与边缘间多出一个空格
print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print()
输出结果如下：
Sentence: He's a very naughty boy!
                          +---------------------------------+
                          |                                 |
                          |    He's a very naughty boy!     |
                          |                                 |
                          +---------------------------------+

# *成员资格
permissions = 'rw'
print('w' in permissions)
print('x' in permissions)

users = ['mlh','foo','bar']
input('Enter your user name: ') in users
Enter your user name: mlh
输出：
True

subject = '$$$ Get rich now!!! $$$'
'$$$' in subject
输出：
True

database = [
['albert', '1234'],
['dilbert',  '4242'],
['smith',  '7524'],
['jones',  '9843']
]
username = input('User name: ')
pin = input('PIN code: ')
if [username, pin] in database: print('Access granted')
输出：
User name: jones
PIN code: 9843
Access granted

numbers = [100,34,678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(max(2,3))
print(min(9,3,2,5))
输出：
3
678
34
3
2

# *随机数
# random模块
# randint(a,b)返回[a,b]之间的整数
# choice(seq)从非空序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。random.choice([1,3,5,7])
# randrange([start,]stop[,step])从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1.random.randrange(1,7,2)
# random.shuffle(list) -> None，就地打乱列表元素
# sample(population,k)从样本空间或总体（序列或者集合类型）中随机取出k个不同的元素，返回一个新的列表
import random
random.sample(['a','b','c','d'],2)
random.sample(['a','a'],2)

# *基本操作
    # 赋值
x = [1,1,1]
x[1] = 2
print(x)
# 输出：
[1, 2, 1]

    # 删除
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)
# 输出：
['Alice', 'Beth', 'Dee-Dee', 'Earl']

    # 给切片赋值
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)
# 输出：
['P', 'e', 'r', 'l']
['P', 'e', 'a', 'r']


name = list('Perl')
name[1:] = list('ython')
print(name)
# 输出：
['P', 'y', 't', 'h', 'o', 'n']

numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers)
numbers[1:4] = []
print(numbers)
# 输出：
[1, 2, 3, 4, 5]
[1, 5]

# *列表方法
    # append
lst = [1, 2, 3]
lst.append(4)
print(lst)
# 输出：
[1, 2, 3, 4]

    # clear
lst = [1,2,3]
lst.clear()
print(lst)
# 输出：
[]

    # copy
a = [1, 2, 3]
b = a
b[1] = 4
print(a)
# 输出：
[1, 4, 3]

a = [1,2,3]
b = a.copy()
b[1] = 4
print(a)
# 输出：
[1, 2, 3]

lst0 = list(range(4))
print(id(lst0))
# hash(lst0)
print(hash(id(lst0)))
lst1 = list(range(4))
print(id(lst1))
print(lst0 == lst1)
print(lst0 is lst1)
lst1 = lst0
# 这里是将lst0的内存地址给了lst1，这时两个列表都指向了同一个内存地址，所以下面修改lst1的内容时，lst0也会改变
print(id(lst1))
lst1[2] = 10
print(lst0)
lst0 = list(range(4))
lst5 = lst0.copy()
print(lst5)
print(lst5 == lst0)
print(lst5 is lst0)
print(id(lst0))
print(id(lst5))
lst0 = [1,[2,3,4],5]
lst5 = lst0.copy()
print(lst5 == lst0)
lst5[2] = 10
print(lst5 == lst0)
print(lst0)
lst5[2] = 5
print(lst5 == lst0)
lst5[1][1] = 20
print(lst5 == lst0)
# 因为是浅拷贝，所以列表中的列表复制的是内存地址，所以会都改变。返回True。复杂列表复制内存地址
print(lst0)
print(lst5)
# 输出：
140651023266184
140651023266184
140651023269512
True
False
140651023266184
[0, 1, 10, 3]
[0, 1, 2, 3]
True
False
140651019149576
140651024414472
True
False
[1, [2, 3, 4], 5]
True
True
[1, [2, 20, 4], 5]
[1, [2, 20, 4], 5]

import copy
lst0 = [1,[2,3,4],5]
lst5 = copy.deepcopy(lst0)
lst5[1][1] = 20
print(lst5 == lst0)
# 深拷贝复制的是值，而不像浅拷贝一样复杂列表复制内存地址

    # count
['to', 'be', 'or', 'not', 'to', 'be'].count('to')
# 输出：
2

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))
print(x.count([1, 2]))
# 输出：
2
1

    # extend
    # extend(iteratable) -> None；将可迭代对象的元素追加进来，返回None；就地修改

