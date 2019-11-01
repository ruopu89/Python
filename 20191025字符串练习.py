# 字符串定义-初始化
s1 = 'string'
s2 = "string2"
s3 = '''this's a "string"'''
s4 = 'hello \n magedu.com'
s5 = r"hello \n magedu.com"
s6 = 'c:\windows\nt'
s7 = R"c:\windows\\nt"
s8 = 'c:\windows\\nt'
sql = """select * from user where name='tom'"""
print(s1,s2,s3,s4,s5,s6,s7,s8,sql)
# 输出：
string string2 this's a "string" hello 
 magedu.com hello \n magedu.com c:\windows
t c:\windows\\nt c:\windows\nt select * from user where name='tom'

# 字符串元素访问-下标
sql = "select * from user where name='tom'"
sql[4]
# 输出：
'c'

sql[4] = 'o'
# 错误输出：
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-fe3590bf222f> in <module>
----> 1 sql[4] = 'o'

TypeError: 'str' object does not support item assignment

sql = "select * from user where name='tom'"
for c in sql:
    print(c)
    print(type(c))
# 输出：可迭代
s
<class 'str'>
e
<class 'str'>
l
<class 'str'>
e
<class 'str'>
c
<class 'str'>
t
<class 'str'>
 
<class 'str'>
*
<class 'str'>

sql = "select * from user where name='tom'"
lst = list(sql)
print(lst)
# 输出：
['s', 'e', 'l', 'e', 'c', 't', ' ', '*', ' ', 'f', 'r', 'o', 'm', ' ', 'u', 's', 'e', 'r', ' ', 'w', 'h', 'e', 'r', 'e', ' ', 'n', 'a', 'm', 'e', '=', "'", 't', 'o', 'm', "'"]

website = 'http://www.python.org'
website[-3:] = 'com'
# 输出：
# 所有标准序列操作(索引、切片、乘法、成员资格检查、长度、最小值和最大值)都适用于字符串，但字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的。
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-3e219c690972> in <module>
      1 website = 'http://www.python.org'
----> 2 website[-3:] = 'com'

TypeError: 'str' object does not support item assignment

# 字符串join连接
# "string".join(iterable) -> str
# 将可迭代对象连接起来，使用string作为分隔符
# 可迭代对象本身元素都是字符串
# 返回一个新字符串

lst = ['1','2','3']
print("\"".join(lst))
输出：1"2"3
# 分隔符是双引号。\是转义符
