from webob import Response, Request, dec
from wsgiref.simple_server import make_server, demo_app


class Application:
    # 用__init__实现调用不合适，因为参数写死了
    def notfound(self, request:Request):  # 这个方法是客户不关心的，出问题才会使用这个函数，这是一个共用的，所以写在框架内
        res = Response()
        res.status_code = 404
        res.body = "not Found".encode()
        return res

    # 路由表
    ROUTETABLE = {}

    @classmethod
    def register(cls, path, handler):
        cls.ROUTETABLE[path] = handler

    @dec.wsgify  # 这个装饰器一定保证下面的函数转化成接收两个参数，environ和start_response，这样才是make_server要看到的东西。这个装饰器就是把下面函数变成标准接口的东西
    def __call__(self, request:Request) -> Response:
        print(self.ROUTETABLE)
        return self.ROUTETABLE.get(request.path, self.notfound)(request)  # 装饰器会把返回值变成可迭代对象，这里用self.ROUTETABLE没有问题，因为实例变量是每一个实例自己的变量，是自己独有的；类变量是类的变量，是类的所有实例共享的属性和方法

def index(request:Request):
    res = Response()
    res.body = "<h1>马哥教育欢迎你们大家</h1>".encode()
    return res

def showpython(request:Request):
    res = Response()
    res.body = "<h1>马哥教育python</h1>".encode()
    return res
# 如果是一个框架的话，上面两个方法应该是用户写好的

# 注册
Application.register('/',index)
Application.register('/python', showpython)

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 9999
    app = Application()
    print('appdict: {}'.format(app.__dict__))
    server = make_server(ip, port, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()