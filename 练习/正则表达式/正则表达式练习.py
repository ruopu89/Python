# 匹配邮箱地址
# import re
#
# s = '''
# test@hot-mail.com
# v-ip@magedu.com
# web.manager@magedu.com.cn
# super.user@google.com
# a@w-a-com
# '''
#
# regex = re.compile('\w+[-.\w]*@[\w-]+(\.[\w-]+)+')
# result = regex.finditer(s)
# print(type(result),result)
# for i in result:
#     print(i)
# ========================================================
# 匹配html标记内的内容
import re

s = "<a href='http://www.magedu.com/index.html' target='_blank'>马哥教育</a>"

regex = re.compile('<[^<>]+>(.*)<[^<>]+>')
result = regex.search(s)
print(result)
regex = re.compile('<(\w+)\s+[^<>]+>(.*)(</\1>)')
result = regex.finditer(s)
for i in result:
    print(i)
# print(result,type(result))