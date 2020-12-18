import re
# 方法
# re.compile(pattern,flags=0)
# ==================================================================
# m = re.match(r"(\w+) (\w+)","Isaac Newton, physicist")
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(1,2))
# print(m.group())
# ==============================================================
# n = re.match(r"(..)+","a1b2c3")
# print(n.group(0))
# print(n.group(1))
# print(n.group(2))
# ==============================================================
# w = re.match(r"(\d+)\.(\d+)","24.1632")
# print(w.groups())
# =================================================================
# s = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# print(s.groupdict())
# ==================================================================
# 单次匹配
# s = '''bottle\nbag\nbig\napple'''
# for i,c in enumerate(s):
#     print((i,c),end='\n' if i%8==0 else ' ')
## match方法
# print('--match--')
# result = re.match('b',s)
# print(1,result)
# result = re.match('a',s)
# print(2,result)
# result = re.match('^a',s,re.M)
# print(3,result)
# result = re.match('^a',s)
# print(4,result)
# regex = re.compile('a')
# result = regex.match(s)
# print(5,result)
# result = regex.match(s,15)
# print(6,result)
# print()
# print('--search--')
# result = re.search('a',s)
# print(7,result)
# regex = re.compile('b')
# result = regex.search(s,1)
# print(8,result)
# regex = re.compile('^b',re.M)
# result = regex.search(s)
# print(8.5,result)
# result = regex.search(s,8)
# print(9,result)
# # fullmatch方法
# print('--fullmatch--')
# result = re.fullmatch('bag',s)
# print(10,result)
# regex = re.compile('bag')
# result = regex.fullmatch(s)
# print(11,result)
# result = regex.fullmatch(s,7)
# print(12,result)
# result = regex.fullmatch(s,7,10)
# print(13,result)
# ==============================================
# 全文搜索
import re
# s = '''bottle\nbag\nbig\nable'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')

# findall方法
# print('--findall--')
# result = re.findall('b',s)
# print()
# print(1,result)
# regex = re.compile('^b')
# result = regex.findall(s)
# print(2,result)
# regex = re.compile('^b',re.M)
# result = regex.findall(s,7)
# print(3,result)
# regex = re.compile('^b',re.S)
# result = regex.findall(s)
# print(4,result)
# regex = re.compile('^b',re.M)
# result = regex.findall(s,7,10)
# print(5, result)
# # finditer
# print('--finditer--')
# result = regex.finditer(s)
# print(type(result))
# print(next(result))
# print(next(result))
# result = re.finditer('b',s)
# print(6,result)
# print(next(result))
# print(next(result))
# ====================================================
# 匹配替换
# import re
# s = '''bottle\nbag\nbig\napple'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')
# ## 替换方法
# print()
# regex = re.compile('b\wg')
# result = regex.sub('magedu',s)
# print(1,result)
# result = regex.sub('magedu',s,1)
# print(2,result)
#
# regex = re.compile('\s+')
# result = regex.subn('\t',s)
# print(3,result)
# ## 分割字符串
# import re
# s = '''01 bottle
# 02 bag
# 03      big1
# 100         able'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')
# print()
#
# print(s.split())
# result = re.split('[\s\d]+',s)
# print(1,result)
# regex = re.compile('^[\s\d]+')
# result = regex.split(s)
# print(2,result)
# regex = re.compile('^[\s\d]+',re.M)
# result = regex.split(s)
# print(3,result)
# regex = re.compile('\s+\d+\s+')
# result = regex.split(' ' + s)
# print(4,result)
# result = regex.split(s)
# print(5,result)
# =================================================
# 分组
import re
s = '''bottle\nbag\nbig\napple'''
for i,c in enumerate(s,1):
    print((i-1,c),end='\n' if i%8==0 else ' ')

regex = re.compile('(b\w+)')
result = regex.match(s)
print()
print(type(result))
print(1,'match',result.groups())

result = regex.search(s,1)
print(2,'search',result.groups())

regex = re.compile('(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)')
result = regex.match(s)
print(3,'match',result)
print(4,result.group(3),result.group(2),result.group(1))
print(5,result.group(0).encode())
print(6, result.group('name2'),result.group('name3'))
print(6.5, result.groups())
print(7,result.groupdict())

result = regex.findall(s)
for x in result:
    print(type(x),x)

regex = re.compile('(?P<head>b\w+)')
result = regex.finditer(s)
for x in result:
    print(type(x),x,x.group(),x.group('head'))

