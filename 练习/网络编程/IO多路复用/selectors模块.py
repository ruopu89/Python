# import selectors
# import threading
# import socket
# import logging
# FORMAT = "%(asctime)s %(threadName)s %(thread)s %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# selector = selectors.DefaultSelector()
#
# def accept(sock:socket.socket, mask):
#     """mask: 事件掩码的或值"""
#     conn, raddr = sock.accept()
#     conn.setblocking(False)
#     key = selector.register(conn, selectors.EVENT_READ, read)
#
# def read(conn:socket.socket, mask):
#     data = conn.recv(1024)
#     msg = "Your msg is {}.".format(data.decode())
#     conn.send(msg.encode())
#
# sock = socket.socket()
# addr = ('0.0.0.0', 9999)
# sock.bind(addr)
# sock.listen()
# logging.info(sock)
# sock.setblocking(False)
# key = selector.register(sock, selectors.EVENT_READ, accept)
# logging.info(key)
# e = threading.Event()
#
# def select(e):
#     while not e.is_set():
#         events = selector.select()
#         print('-' * 30)
#         for key, mask in events:
#             logging.info(key)
#             logging.info(mask)
#             callback = key.data
#             callback(key.fileobj, mask)
# threading.Thread(target=select, args=(e,), name='select').start()
#
# def main():
#     while not e.is_set():
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             e.set()
#             fobjs = []
#             logging.info('{}'.format(list(selector.get_map().items())))
#             for fd, key in selector.get_map().items():
#                 print(fd, key)
#                 print(key.fileobj)
#                 fobjs.append(key.fileobj)
#             for fobj in fobjs:
#                 selector.unregister(fobj)
#                 fobj.close()
#             selector.close()
#
# if __name__ == '__main__':
#     main()
# =======================================================
# 课上练习
# import selectors
# import socket
# import threading
# selector = selectors.DefaultSelector()
#
# def accept(sock:socket.socket):
#     conn, _ = sock.accept()
#     print('sock: {}'.format(sock))
#     conn.setblocking(False)
#     selector.register(conn, selectors.EVENT_READ, recv)
# print(accept)
#
# def recv(conn:socket.socket):
#     data = conn.recv(1024).strip().decode()
#     print(data)
#     msg = "Your msg = {}".format(data)
#     conn.send(msg.encode())
#
# sock = socket.socket()
# ip = '127.0.0.1'
# port = 9999
# addr = (ip, port)
# sock.bind(addr)
# sock.listen()
# print('sock: {}'.format(sock))
# sock.setblocking(False)
# e = threading.Event()
#
# key = selector.register(sock, selectors.EVENT_READ, accept)
# print(key)
#
# while not e.is_set():
#     events = selector.select()
#     if events:
#         print(events)
#     for key, mask in events:
#         print(key, mask)
#         callback = key.data
#         callback(key.fileobj)
# ======================================================
# 网络上的练习：https://blog.csdn.net/weixin_30877181/article/details/96812329
# selector模块使用
from socket import *
import selectors

sel = selectors.DefaultSelector()
def accept(server_fileobj, mask)