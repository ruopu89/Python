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
    # append(object) -> None；列表尾部追加元素，返回None；返回None就意味着没有新的列表产生，就地修改；时间复杂度是O(1)
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
    # extend(iteratable) -> None；将可迭代对象的元素追加进来，返回None；就地修改，extend与其他拼接方法的不同就是就地修改，其他方法是返回一个新的列表。
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
# 输出：
[1, 2, 3, 4, 5, 6]

    # index
    # index(value,[start,[stop]]);通过值value，从指定区间查找列表内的元素是否匹配;匹配第一个就立即返回索引;匹配不到，抛出异常ValueError
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))
print(knights.index('herring'))
print(knights[4])
# 输出：
4
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-9-da6a439e3aff> in <module>
      1 knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
      2 print(knights.index('who'))
----> 3 print(knights.index('herring'))
      4 print(knights[4])

ValueError: 'herring' is not in list

'who'

    # insert(index,object) -> None；在指定的索引index处插入元素object
    # 返回None就意味着没有新的列表产生，就地修改；时间复杂度是O(n)；索引超越上界，尾部追加；索引超越下界，头部追加
numbers = [1,2,3,5,6,7]
numbers.insert(3,'four')
print(numbers)
numbers = [1,2,3,5,6,7]
numbers[3:3] = ['foru']
print(numbers)
# 输出：
[1, 2, 3, 'four', 5, 6, 7]
[1, 2, 3, 'foru', 5, 6, 7]


    # pop([index]) -> item
    # 不指定索引index，就从列表尾部弹出一个元素
    # 指定索引index，就从索引处弹出一个元素，索引超界抛出IndexError错误
x = [1,2,3]
print(x.pop())
print(x)
print(x.pop(0))
print(x)
x = [1,2,3]
print(x.append(x.pop()))
print(x)
x.append(x.pop(0))
print(x)
x.append(x.pop(0))
print(x)
# 使用append代替push方法，因为python中没有提供push。此将刚弹出的值压入(或附加)后，得到的栈将与原来相同。要创建先进先出(FIFO)的队列，可使用insert(0, ...)代替append。另外，也可继续使用append，但用 pop(0)替代 pop() 。
# 输出：
3
[1, 2]
1
[2]
None
[1, 2, 3]
[2, 3, 1]
[3, 1, 2]

    # remove(value) -> None；从左至右查找第一个匹配value的值，移除该元素，返回None；就地修改
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)
x.remove('bee')
# 输入
['to', 'or', 'not', 'to', 'be']
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-30-4e925bfb4b14> in <module>
      2 x.remove('be')
      3 print(x)
----> 4 x.remove('bee')

ValueError: list.remove(x): x not in list

    # reverse() -> None；将列表元素反转，返回None；就地修改
x = [1,2,3]
x.reverse()
print(x)
x = [1,2,3]
print(list(reversed(x)))
# reverse按相反的顺序排列列表中的元素。但不返回任何值(与remove和sort等方法一样) 。如果要按相反的顺序迭代序列，可使用函数reversed 。这个函数不返回列表，而是返回一个迭代器 。你可使用list将返回的对象转换为列表。
# 输出：
[3, 2, 1]
[3, 2, 1]

    # sort(key=None,reverse=False) -> None；对列表元素进行排序，就地修改，默认升序；reverse为True，反转，降序；key一个函数，指定key如何排序； lst.sort(key=functionname)
x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
x = [4, 6, 2, 1, 7, 9]
y = x.sort()
print(y)
x = [4, 6, 2, 1, 7, 9]
y = x.copy()
y.sort()
print(x)
print(y)
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print(x)
print(y)
sorted('Python')
# 输出：
[1, 2, 4, 6, 7, 9]
None
[4, 6, 2, 1, 7, 9]
[1, 2, 4, 6, 7, 9]
[4, 6, 2, 1, 7, 9]
[1, 2, 4, 6, 7, 9]
['P', 'h', 'n', 'o', 't', 'y']

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print(x)
# 方法sort接受两个可选参数：key 和reverse。这两个参数通常是按名称指定的，称为关键字参数，参数 key类似于参数cmp：你将其设置为一个用于排序的函数。然而，不会直接使用这个函数来判断一个元素是否比另一个元素小，而是使用它来为每个元素创建一个键，再根据这些键对元素进行排序。因此，要根据长度对元素进行排序，可将参数 key 设置为函数len。
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)
# 对于另一个关键字参数reverse，只需将其指定为一个真值（True或False），以指出是否要按相反的顺序对列表进行排序。
# 函数sorted也接受参数key和reverse。在很多情况下，将参数key设置为一个自定义函数很有用。

pop index count copy # 这四个方法不会就地修改并返回None
append clear extend insert remove reverse sort # 这些方法会就地修改并返回None

# 练习
===============================================
   示例，最笨拙的方法。从小到大排列，i1最小，i3最大
===============================================
nums = []
# 需要先定义出nums这个变量，不然会提示"nums not deni"
for i in range(3):
    nums.append(int(input('{}:'.format(i))))
# '{}:'是取其后面format()中变量的值，这时format中是i，'{}:'是显示的提示信息，
# 输入的值会被int处理后追加到nums列表中。结果如下：
# 0:1   第0次，输入的是1
# 0   这里打印了一次i
# [1]   这里打印一次nums
# 1:3   第1次输入的是3
# 1
# [1, 3]   nums现在就是两个数字了
# 2:4
# 2
# [1, 3, 4]
if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        i3 = nums[0]   # 上面先比较索引0是否大于索引1和2，如果大于，就把索引0的数字给i3。
        if nums[1] > nums[2]:
            i2 = nums[1]
            i1 = nums[2]    
# 继续判断，这时已判断完索引0了，再判断索引1是否大于索引2，如果大于，就把索引1给i2，索引2给i1。否则，就把
# 索引2给i2，索引1给i1。
        else:
            i2 = nums[2]
            i1 = nums[1]
    else:
        i2 = nums[0]
        i3 = nums[2]
        i1 = nums[1]
# 如果上面判断索引0不大于索引2，就表示索引2最大，给i3，索引1最小，给i1。
else:  # 0<1
    if nums[0] > nums[2]:
        i3 = nums[1]
        i2 = nums[0]
        i1 = nums[2]
# 如果最开始判断的索引0小于索引1，再判断索引 0是否大于索引2，如果大于，就表示索引2最小，索引1最大。
# 下面的判断道理是一样的
    else: # 0<2
        if nums[1] < nums[2]: # 1<2
            i1 = nums[0]
            i2 = nums[1]
            i3 = nums[2]
        else: # 1 > 2
            i1 = nums[0]
            i2 = nums[2]
            i3 = nums[1]
print(i1,i2,i3)
# 这里主要看六种变化，1. 索引0大于索引1和索引2，索引1大于索引2；2. 索引0大于索引1和索引2，索引2大于索引1；
# 3. 索引2大于索引0和索引1，索引0大于索引1；4. 索引2大于索引0和索引1，索引1大于索引0；5. 索引1大于索引0和索引2，索引0大于索引2；6. 索引1大于索引0和索引2，索引2大于索引0

===================
   改进，从大到小排列
===================
nums = []
out = None   # 定义空列表，将None改为[]也可以。
for i in range(3):
    nums.append(int(input('{}:'.format(i))))
    
if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        if nums[1] > nums[2]:
            out = [2,1,0]   # 这里的[2,1,0]指的是索引，保存在out变量中
# out是为了保存索引的顺序
        else:
            out = [1,2,0]
    else:
        out = [1,0,2]
else: # 0<1
    if nums[0] > nums[2]:
        out = [2,0,1]
    else:  # 0<2
        if nums[1] < nums[2]:   # 1<2
            out = [0,1,2]
        else: # 1>2
            out = [0,2,1]
out.reverse()
# reverse()是为了将out列表中的元素整个反过来，原本是从小到大排列，变成从大到小排列。
for i in out:
    print(nums[i],end=', ')
# 最后将out中的三个数字依次传给i，i中保存的实际就是索引编号，再把i带入到nums列表，
# 这样就从小到大打印出结果了

================
  max min的实现
================
nums = []
out = None
for i in range(3):
    nums.append(int(input('{}:'.format(i))))
    
while True:
    cur = min(nums)
# 死循环，用min把列表中最小的数字选出
    print(cur)
# 打印最小的数字
    nums.remove(cur)
# 将最小的数字删除，因为上面for循环定义了循环3次，所以这里while循环可以循环两次，最后一次用下面的代码执行
    if len(nums) == 1:
# 判断nums列表中是否只有1个元素，如果不是，就继续上面的循环
        print(nums[0])
        break
# 打印出最后一个元素后就退出循环

==============
  列表sort实现
==============
nums = []

for i in range(3):
    nums.append(int(input('{}:'.format(i))))
    
nums.sort()
# sort() 函数用于对原列表进行排序
print(nums)