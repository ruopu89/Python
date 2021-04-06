# 模板
# import re
# from io import StringIO, BytesIO

# d = {'id':5, 'name':'tom', 'age':20}

# class Template:
#     _pattern = '{{([a-zA-Z0-9_]+)}}'
#     regex = re.compile(_pattern)

#     @classmethod
#     def render(cls, template, data:dict):
#         html = StringIO()

#         with open(template, encoding='utf-8') as f:
#             for line in f:
#                 start = 0
#                 newline = ''
#                 for matcher in cls.regex.finditer(line):
#                     newline += line[start:matcher.start()]
#                     print(matcher, matcher.group(1))
#                     key = matcher.group(1)
#                     tmp = data.get(key, '')
#                     newline += str(tmp)
#                     start = matcher.end()
#                 else:
#                     newline += line[start:]
#                 html.write(newline)
#             print(html.getvalue())
#         html.close()

# filename = 'index.html'
# Template.render('E:\\QnapSync\\Python\\练习\\网络编程\\http编程\\template', d)
# print(Template)
# ============================================================================
# jinjia2 模板
# from jinja2 import Template

# template = Template('Hello {{ name }} !')
# test = template.render(name='John Doe')
# print(test)
# # 通过创建一个 Template 的实例，你会得到一个新的模板对象，提供一 个名为 render() 的方法，该方法在有字典或关键字参数时调用 扩充模板。字典或关键字参数会被传递到模板，即模板“上下文”。
# # 如你所见， Jinja2 内部使用 unicode 并且返回值也是 unicode 字符串。所以确 保你的应用里也确实使用 unicode 。
# =====================================================================
# from jinja2 import Environment, PackageLoader, FileSystemLoader

# env = Environment(loader=FileSystemLoader('webarch\\templates'))

# template = env.get_template('index.html')

# userlist = [
#     (3, 'tom', 20),
#     (5, 'jerry', 16),
#     (6, 'sam', 23),
#     (8, 'kevin', 18)
# ]

# d = {'userlist':userlist, 'usercount':len(userlist)}

# print(template.render(**d))
# ===========================================================
# cd8299ce-ddfe-4b44-a205-3be351e13d97
