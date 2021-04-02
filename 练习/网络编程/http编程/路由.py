# from webob import Response, Request, dec
# from wsgiref.simple_server import make_server, demo_app


# class Application:
#     # 用__init__实现调用不合适，因为参数写死了
#     def notfound(self, request:Request):  # 这个方法是客户不关心的，出问题才会使用这个函数，这是一个共用的，所以写在框架内
#         res = Response()
#         res.status_code = 404
#         res.body = "not Found".encode()
#         return res

#     # 路由表
#     ROUTETABLE = {}

#     @classmethod
#     def register(cls, path, handler):
#         cls.ROUTETABLE[path] = handler

#     @dec.wsgify  # 这个装饰器一定保证下面的函数转化成接收两个参数，environ和start_response，这样才是make_server要看到的东西。这个装饰器就是把下面函数变成标准接口的东西
#     def __call__(self, request:Request) -> Response:
#         print(self.ROUTETABLE)
#         return self.ROUTETABLE.get(request.path, self.notfound)(request)  # 装饰器会把返回值变成可迭代对象，这里用self.ROUTETABLE没有问题，因为实例变量是每一个实例自己的变量，是自己独有的；类变量是类的变量，是类的所有实例共享的属性和方法

# def index(request:Request):
#     res = Response()
#     res.body = "<h1>马哥教育欢迎你们大家</h1>".encode()
#     return res

# def showpython(request:Request):
#     res = Response()
#     res.body = "<h1>马哥教育python</h1>".encode()
#     return res
# # 如果是一个框架的话，上面两个方法应该是用户写好的

# # 注册
# Application.register('/',index)
# Application.register('/python', showpython)

# if __name__ == "__main__":
#     ip = "127.0.0.1"
#     port = 9999
#     app = Application()
#     print('appdict: {}'.format(app.__dict__))
#     server = make_server(ip, port, app)
#     try:
#         server.serve_forever()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         server.server_close()
# =============================================
# 路由分组
# from webob import Response, Request
# from webob.dec import wsgify
# from wsgiref.simple_server import make_server
# from webob.exc import HTTPNotFound
# import re
# from cyberbrain import trace

# class Router:
#     def __init__(self, prefix:str=''):
#         self.__prefix = prefix.rstrip('/\\')
# # rstrip() 删除 string 字符串末尾的指定字符（默认为空格）。
#         self.__routetable = []

#     def route(self, pattern, *methods):
#         def wrapper(handler):
#             self.__routetable.append((tuple(map(lambda x:x.upper(), methods)), re.compile(pattern), handler))
#             return handler
#         return wrapper

#     def get(self, pattern):
#         return self.route(pattern, 'GET')

#     def post(self, pattern):
#         return self.route(pattern, 'POST')

#     def head(self, pattern):
#         return self.route(pattern, 'HEAD')

#     def match(self, request:Request):
#         if not request.path.startswith(self.__prefix):
#             return None
#         for methods, pattern, handler in self.__routetable:
#             if not methods or request.method.upper() in methods:
#                 matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
#                 if matcher:
#                     request.groups = matcher.groups()
#                     request.groupdict = matcher.groupdict()
#                     print(f"request groups: {request.groups}, groupdict: {request.groupdict}, matcher: {matcher}")
#                     return handler(request)

# class App:
#     _ROUTERS = []

#     @classmethod
#     def register(cls, *routers:Router):
#         for router in routers:
#             cls._ROUTERS.append(router)

#     @wsgify
#     def __call__(self, request:Request):
#         for router in self._ROUTERS:
#             response = router.match(request)
#             if response:
#                 return response
#         raise HTTPNotFound('<h1>你访问的页面被外星人劫持了</h1>')

# idx = Router()
# py = Router('/python')

# App.register(idx, py)

# @idx.get(r'^/$')
# @idx.route(r'^/(?P<id>\d+)$')
# def indexhandler(request):
#     print(f"indexhandler request.groups: {request.groups}")
#     print(f"indexhandler request.groupdict: {request.groupdict}")
#     return '<h1>马哥教育欢迎你. magedu.com</h1>'

# @py.post('^/(\w+)$')
# def pythonhandler(request):
#     print(f"pythonhandler request.groups: {request.groups}")
#     print(f"pythonhandler request.groupdict: {request.groupdict}")
#     res = Response()
#     res.charset = 'utf-8'
#     res.body = '<h1>Welcome to Magedu Python</h1>'.encode()
#     return res

# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     port = 9999
#     server = make_server(ip, port, App())
#     try:
#         server.serve_forever()
#     except KeyboardInterrupt:
#         server.shutdown()
#         server.server_close()
# ==============================================================
# 路由分组
# from webob import Response, Request
# from webob.dec import wsgify
# from wsgiref.simple_server import make_server
# from webob.exc import HTTPNotFound
# import re

# class AttrDict:
#     def __init__(self, d:dict):
#         self.__dict__.update(d if isinstance(d, dict) else {})

#     def __setattr__(self, key, value):
#         raise NotImplementedError

#     def __repr__(self):
#         return "<AttrDict {}>".format(self.__dict__)

#     def __len__(self):
#         return len(self.__dict__)

# class Router:
#     __regex = re.compile(r'/{([^{}:]+):?([^{}:]*)}')

#     TYPEPATTERNS = {
#         'str': r'[^/]+',
#         'word': r'\w+',
#         'int': r'[+-]?\d+',
#         'float': r'[+-]?\d+\.\d+',  # 严苛的要求必须是 15.6这样的形式
#         'any': r'.+'
#     }

#     TYPECAST = {
#         'str': str,
#         'word': str,
#         'int': int,
#         'float': float,
#         'any': str
#     }

#     def __parse(self, src:str):
#         start = 0
#         repl = ''
#         types = {}

#         matchers = self.__regex.finditer(src)
#         for i, matcher in enumerate(matchers):
#             name = matcher.group(1)
#             t = matcher.group(2)

#             types[name] = self.TYPECAST.get(matcher.group(2), str)

#             repl += src[start:matcher.start()]
#             tmp = '/(?P<{}>{})'.format(
#                 matcher.group(1),
#                 self.TYPEPATTERNS.get(matcher.group(2), self.TYPEPATTERNS['str'])
#             )
#             repl += tmp

#             start = matcher.end()
#         else:
#             repl += src[start:]
#         return repl, types

#     def __init__(self, prefix:str=''):
#         self.__prefix = prefix.rstrip('/\\')
#         self.__routetable = []

#     def route(self, rule, *methods):
#         def wrapper(handler):
#             pattern, trans = self.__parse(rule)
#             self.__routetable.append(
#                 (tuple(map(lambda x:x.upper(), methods)),
#                 re.compile(pattern),
#                 trans,
#                 handler
#                 )
#             )
#             return handler
#         return wrapper

#     def get(self, pattern):
#         return self.route(pattern, 'GET')

#     def post(self, pattern):
#         return self.route(pattern, 'POST')

#     def head(self, pattern):
#         return self.route(pattern, 'HEAD')

#     def match(self, request:Request):
#         if not request.path.startswith(self.__prefix):
#             return None
#         for methods, pattern, trans, handler in self.__routetable:
#             if not methods or request.method.upper() in methods:
#                 matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
#                 if matcher:
#                     newdict = {}
#                     for k,v in matcher.groupdict().items():
#                         newdict[k] = trans[k](v)
#                         request.vars = AttrDict(newdict)
#                         return handler(request)

# class App:
#     _ROUTERS = []

#     @classmethod
#     def register(cls, *routers:Router):
#         for router in routers:
#             cls._ROUTERS.append(router)

#     @wsgify
#     def __call__(self, request:Request):
#         for router in self._ROUTERS:
#             response = router.match(request)
#             if response:
#                 return response
#         raise HTTPNotFound('<h1>你访问的页面被外星人劫持了</h1>')

# idx = Router()
# py = Router('/python')

# App.register(idx, py)

# @idx.get(r'^/$')
# @idx.route(r'^/{id:int}$')
# def indexhandler(request):
#     id = ''
#     if request.vars:
#         id = request.vars.id
#         print(type(id))
#     return '<h1>马哥教育欢迎你{}. magedu.com</h1>'.format(id)

# @py.get('^/{id}$')
# def pythonhandler(request):
#     if request.vars:
#         print(type(request.vars.id))
#     res = Response()
#     res.charset = 'utf-8'
#     res.body = '<h1>Welcome to Magedu Python</h1>'.encode()
#     return res

# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     port = 9999
#     server = make_server(ip, port, App())
#     try:
#         server.serve_forever()
#     except KeyboardInterrupt:
#         server.shutdown()
#         server.server_close()
# ============================================================
# 正则替换 sub 函数使用实例
# import re

# # pattern = r'\d+'
# # repl = ''
# # src = 'welcome 123 to 456 magedu.com'

# # regex = re.compile(pattern)
# # dest = regex.sub(repl, src)
# # dest1 = regex.search(src)

# # print(regex, dest, end='-----------------------------\n')
# # print(dest1)
# pattern = r'/{([^{}:]+):?([^{}:]*)}'
# 匹配 /{} 这样的格式，大括号中分为两部分，分为两个组，第一个分组不要匹配 {}:，+号表示匹配1个或多个，之后配置0个或1个冒号(:)，之后是第二个分组，不要匹配 {}: 0个或多个
# re*：匹配0个或多个的表达式。
# re+：匹配1个或多个的表达式。
# re?：匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式

# src = '/student/{name}/xxx/{id:int}'
# print(src)

# def repl(matcher):
#     print(f"matcher: {matcher}")
#     print("matcher.group 0", matcher.group(0)) # 这是匹配到的全部，如 {id:int}
#     print("matcher.group 1", matcher.group(1)) # 这是匹配到的内容的前半部分，如 id
#     print("matcher.group 2", matcher.group(2)) # 这是匹配到的内容的后半部分，如 int，如果匹配到的全部内容是 {name}，那么就没有 group(2) 了，或者说这部分就是空。因为 pattern 中没有使用命名分组，所以这里使用 group(0) 这种方式
#     return '/(?P<{}>{})'.format(matcher.group(1), 'T' if matcher.group(2) else 'F')

# regex = re.compile(pattern)
# dest = regex.sub(repl, src)
# # 用 repl 替换 src 中的 r'/{([^{}:]+):?([^{}:]*)}' 部分
# # 如果 repl 是一个函数，那它会对每个非重复的 pattern 的情况调用。repl 这个函数只能有一个 匹配对象 参数，并返回一个替换后的字符串。
# print(dest)
# ==============================================================================
# 转换例程
# import re

# regex = re.compile('/{([^{}:]+):?([^{}:]*)}')

# s = [
#     '/student/{name:str}/xxx/{id:int}',
#     '/student/xxx/{id:int}/yyy',
#     '/student/xxx/5134324',
#     '/student/{name:}/xxx/{id}',
#     '/student/{name:}/xxx/{id:aaa}'
# ]

# TYPEPATTERNS = {
#     'str': r'[^/]+',
#     'word': r'\w+',
#     'int': r'[+-]?\d+',
#     'float': r'[+-]?\d+\.\d+',
#     # 严苛的要求必须是 15.6这样的形式
#     'any': r'.+'
# }

# def repl(matcher):
#     print(f"matcher: {matcher}")
#     print("matcher.group 0", matcher.group(0)) # 这是匹配到的全部，如 {id:int}
#     print("matcher.group 1", matcher.group(1)) # 这是匹配到的内容的前半部分，如 id
#     print("matcher.group 2", matcher.group(2))
#     return '/(?P<{}>{})'.format(matcher.group(1),TYPEPATTERNS.get(matcher.group(2),TYPEPATTERNS['str']))

# def parse(src:str):
#     return regex.sub(repl, src)

# for x in s:
#     print(parse(x))
# ==========================================================
# 重新整理的分组代码
from webob import Response, Request
from webob.dec import wsgify
from wsgiref.simple_server import make_server
from webob.exc import HTTPNotFound
import re

class AttrDict:
    def __init__(self, d:dict):
        self.__dict__.update(d if isinstance(d, dict) else {})

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __repr__(self):
        return "<AttrDict {}>".format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

class Router:
    __regex = re.compile(r'/{([^{}:]+):?([^{}:]*)}')

    TYPEPATTERNS = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[+-]?\d+',
        'float': r'[+-]?\d+\.\d+',  # 严苛的要求必须是 15.6这样的形式
        'any': r'.+'
    }

    TYPECAST = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }

    def __parse(self, src:str):
        start = 0
        repl = ''
        types = {}

        matchers = self.__regex.finditer(src)

        for i, matcher in enumerate(matchers):
            name = matcher.group(1)
            t = matcher.group(2)
            print(i,t)

            types[name] = self.TYPECAST.get(t, str)

            repl += src[start:matcher.start()]
            tmp = '/(?P<{}>{})'.format(matcher.group(1),self.TYPEPATTERNS.get(t, self.TYPECAST['str']))
            repl += tmp
            start = matcher.end()
        else:
            repl += src[start:]
        return repl, types

    def __init__(self, prefix:str=''):
        self.__prefix = prefix.rstrip('/\\')
        self.__routetable = []

    def route(self, rule, *methods):
        def wrapper(handler):
            pattern, trans = self.__parse(rule)
            self.__routetable.append(
                (tuple(map(lambda x:x.upper, methods)),
                re.compile(pattern),
                trans,
                handler
                )
            )
            return handler
        return wrapper

    def get(self, pattern):
        return self.route(pattern, 'GET')

    def post(self, pattern):
        return self.route(pattern, 'POST')

    def head(self, pattern):
        return self.route(pattern, 'HEAD')

    def match(self, request:Request):
        if not request.path.startswith(self.__prefix):
            return None
        for methods, pattern, trans, handler in self.__routetable:
            if not methods or request.method.upper() in methods:
                matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
                if matcher:
                    newdict = {}
                    for k,v in matcher.groupdict().items():
                        newdict[k] = trans[k](v)
                        request.vars = AttrDict(newdict)
                        return handler(request)

class App:
    _ROUTERS = []

    @classmethod
    def register(cls, *routers:Router):
        for router in routers:
            cls._ROUTERS.append(router)

    @wsgify
    def __call__(self, request:Request):
        for router in self._ROUTERS:
            response = router.match(request)
            if response:
                return response
        raise HTTPNotFound('<h1>你访问的页面被外星人劫持了</h1>')

idx = Router()
py = Router('/python')

App.register(idx, py)

@idx.get(r'^/$')
@idx.route(r'^/{id:int}$')
def indexhandler(request):
    id = ''
    if request.vars:
        id = request.vars.id
        print(type(id))
    return '<h1>马哥教育欢迎你{}. magedu.com</h1>'.format(id)

@py.get('^/{id}$')
def pythonhandler(request):
    if request.vars:
        print(type(request.vars.id))
    res = Response()
    res.charset = 'utf-8'
    res.body = '<h1>Welcome to Magedu Python</h1>'.encode()
    return res

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    
    server = make_server(ip, port, App())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()