# # import wsgiref
# from wsgiref.simple_server import make_server,demo_app
#
# def application(environ:dict, start_response):
#     # print(type(environ))
#     html = "<h1>Hello Python</h1>"
#     start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])
#     return [html.encode()]
#
# ip = '127.0.0.1'
# port = 9999
# server = make_server(ip, port, application)
# server.serve_forever()
# server.server_close()
# ======================================
from wsgiref.simple_server import make_server
import psutil

def application(environ, start_response):
    status = '200 ok'
    headers = [('Content-Type', 'text/html;charset=utf-8')]
    start_response(status, headers)
    # 返回可迭代对象
    html = '<h1>马哥教育欢迎你</h1>'.encode("utf-8")
    return [html]

ip = '127.0.0.1'
port = 9999
server = make_server(ip, port, application)
print(server.base_environ)
print(server.setup_environ())
server.serve_forever()

