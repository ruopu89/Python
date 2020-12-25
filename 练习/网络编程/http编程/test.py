# class test:
#     def __init__(self):
#         self.a = 'a'
#         self.b = 'b'
#     abc = {}
#
#     def __call__(self, *args, **kwargs):
#         self.abc['c'] = args
#         # print(self.abc)
#         return self.abc
#
# t = test()
# t('h')
# print(t.abc, t.__dict__)
# 实例变量是每一个实例自己的变量，是自己独有的；类变量是类的变量，是类的所有实例共享的属性和方法
#
# route = []
# def register(pa, *method):
#     route.append((method, pa))
#
# register('a','b','ccc')
#
# print(route)
# =========================================
import re

s = '''bottle\nbag\nbig\napple'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0 else ' ')
# print()

regex = re.compile('(b\w+)')
# print(regex)
# result = regex.findall(s)
# print()
# print(type(result))
# print(1, 'match', result.)
# result = regex.match(s)
# print(type(result))
# print(1, 'match', result)
# result = regex.search(s)
# print(type(result))
# print(result.groups())
# result = regex.fullmatch(s)
# if result:
#     print('OK', type(result), result.groups())
# else:
#     print('fuck', type(result))
# print('==match==')
# result = regex.match(s,15)
# print(1, type(result), result.group())
result = regex.search(s,9)
print(2, 'search', result.groups())

regex = re.compile('(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)')
result = regex.match(s)
print(3, 'match', result)
print(4, result.group(3), result.group(2), result.group(1))
print(5, result.group(0).encode())
print(6, result.group('name2'), result.group('name3'))
print(6.5, result.groups())
print(7, result.groupdict())

result = regex.findall(s)
print(result)
for x in result:
    print(type(x),x)

regex = re.compile('(?P<head>b\w+)')
result = regex.finditer(s)
print(result)
for x in result:
    print(type(x), x, x.group(), x.group('head'))