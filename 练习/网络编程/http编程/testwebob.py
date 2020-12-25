from wsgiref.simple_server import make_server
import webob
from webob.dec import wsgify
import urlli

@wsgify
def app(request:webob.Request) -> webob.Response:
    res = webob.Response('<h1>马哥教育欢迎你. magedu.com</h1>')
    return '<h1>马哥教育欢迎你. </h1>'

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()