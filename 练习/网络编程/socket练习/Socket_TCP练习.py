# accept和recv是阻塞的，主线程经常被阻塞住而不能工作。怎么办
# import socket
#
# s = socket.socket()
# s.bind(('10.0.30.50',9999))
# s.listen()
#
# s1, info = s.accept()
#
# data = s1.recv(1024)
# print(data, info)
# s1.send(b'magedu.com ack')
#
# s2, _ = s.accept()
#
# data = s2.recv(1024)
# s2.send(b'hello python')
#
# s.close
# =================================
# #### 练习 -- 写一个群聊程序
# 需求分析
# 聊天工具是CS程序，C是每一个客户端，S是服务器端
# 服务器应该具有的功能：
# 启动服务，包括绑定地址和端口，监听
# 建立连接，能和多个客户端建立连接
# 接收不同用户的信息
# 分发，将接收的某个用户的信息转发到已连接的所有客户端
# 停止服务
# 记录连接的客户端
# import logging
# import socket
# import threading
# import datetime
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s %(thread)d %(message)s")
#
# class ChatServer:
#     def __init__(self, ip='10.0.30.50', port=9999):
#         self.sock = socket.socket()
#         self.addr = (ip, port)
#         self.clients = {}
#
#     def start(self):
#         self.sock.bind(self.addr)
#         self.sock.listen()
#         threading.Thread(target=self.accept).start()
#
#     def accept(self):
#         while True:
#             sock, client = self.sock.accept()   # 生成新的socket用于传输消息
#             self.clients[client] = sock
#             # logging.info("self.clients: {}".format(self.clients))
#             threading.Thread(target=self.recv, args=(sock, client)).start()
#
#     def recv(self, sock:socket.socket, client):
#         while True:
#             data = sock.recv(1024)
#             msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *client, data.decode())
#             logging.info(msg)
#             msg = msg.encode()
#             for s in self.clients.values():
#                 s.send(msg)
#
#     def stop(self):
#         for s in self.clients.values():
#             s.close()
#         self.sock.close()
#
# cs = ChatServer()
# cs.start()
# =============================================================
# import threading
# import time
# import socket
# import logging
#
# logging.basicConfig(format='%(thread)s %(threadName)s %(message)s', level=logging.INFO)
#
# sock = socket.socket()
# ip = '10.0.30.50'
# port = 9999
# addr = (ip, port)
# sock.bind(addr)
# sock.listen()
#
# # time.sleep(3)
# logging.info(sock)
#
# conn, _ = sock.accept()
# sock.close()
# ======================================
# import threading
# import time
# import socket
# import logging
#
# logging.basicConfig(format='%(thread)s %(threadName)s %(message)s', level=logging.INFO)
#
# sock = socket.socket()
# ip = '10.0.30.50'
# port = 9999
# addr = (ip, port)
# sock.bind(addr)
# sock.listen()
#
# time.sleep(3)
#
# conn, addrinfo = sock.accept()
# logging.info(conn)
# logging.info(addrinfo)
#
# data = conn.recv(1024)
# logging.info('data.decode {}'.format(data.decode))
# msg = "ack {}".format(data.decode())
# conn.send(msg.encode())
# logging.info(sock)
#
# conn.close()
# sock.close()
# ========================================
# 群聊软件
# import threading
# import time
# import socket
# import logging
#
# logging.basicConfig(format='%(thread)s %(threadName)s %(message)s', level=logging.INFO)
#
# class ChatServer:
#     def __init__(self, ip = '10.0.30.50', port = 9999):
#         self.sock = socket.socket()
#         self.addr = (ip, port)
#         self.event = threading.Event()
#         self.clients = {}
#
#     def start(self):
#         self.sock.bind(self.addr)
#         self.sock.listen()
#
#         threading.Thread(target=self._accept, name='accept').start()
#
#     def stop(self):
#         for c in self.clients.values():
#             c.close
#         self.sock.close()
#         self.event.wait(3)
#         self.event.set()
#
#     def _accept(self):
#         while not self.event.is_set():
#             conn, client = self.sock.accept()
#             self.clients[client] = conn
#
#             threading.Thread(target=self._recv, args=(conn, client), name="recv").start()
#
#     def _recv(self, conn, client):
#         while not self.event.is_set():
#             try:
#                 data = conn.recv(1024)
#             except Exception as e:
#                 logging.info(e)
#                 data = b"quit"
#             data = data.decode()
#             logging.info(data)
#
#             if data == "quit":
#                 logging.info('quit!')
#                 self.clients.pop(client)
#                 conn.close()
#                 break
#             msg = "ack {}".format(data)
#             for c in self.clients.values():
#                 c.send(msg.encode())
#
# cs = ChatServer()
# cs.start()
#
# e = threading.Event()
#
# def showthread():
#     while not e.wait(3):
#         logging.info(threading.enumerate())
#
# # threading.Thread(target=showthread, daemon=True).start()
#
# while True:
#     cmd = input(">>>").strip()
#     if cmd == "quit":
#         cs.stop()
#         break
# ==============================================================
# makefile test
# import threading
# import time
# import socket
# import logging
#
# logging.basicConfig(format='%(thread)s %(threadName)s %(message)s', level=logging.INFO)
#
# ip = '10.0.30.50'
# port = 9999
# sock = socket.socket()
# addr = (ip, port)
# event = threading.Event()
#
# sock.bind(addr)
# sock.listen()
#
# def accept(sock:socket.socket):
#     s, addrinfo = sock.accept()
#     f = s.makefile(mode='rw')
#
#     while True:
#         line = f.readline()
#         logging.info(line)
#
#         if line.strip() == "quit":
#             break
#
#         msg = "Your msg = {} ack".format(line)
#         f.write(msg)
#         f.flush()
#     f.close()
#     sock.close()
#
# threading.Thread(target=accept, args=(sock,)).start()
# while not event.wait(2):
#     print(sock)
# ===========================================================
# 将上面的群聊代码改用makefile
# import threading
# import time
# import socket
# import logging
#
# logging.basicConfig(format='%(thread)s %(threadName)s %(message)s', level=logging.INFO)
#
# class ChatServer:
#     def __init__(self, ip='10.0.30.50', port=9999):
#         self.sock = socket.socket()
#         self.addr = (ip, port)
#         self.event = threading.Event()
#         self.clients = {}
#
#     def start(self):
#         self.sock.bind(self.addr)
#         self.sock.listen()
#
#         threading.Thread(target=self._accept, name='accept').start()
#
#     def stop(self):
#         for c in self.clients.values():
#             c.close
#         self.sock.close()
#         self.event.wait(3)
#         self.event.set()
#
#     def _accept(self):
#         while not self.event.is_set():
#             conn, client = self.sock.accept()
#             f = conn.makefile(mode='rw')
#             self.clients[client] = f
#             threading.Thread(target=self._recv, args=(f, client), name="recv").start()
#
#     def _recv(self, f, client):
#         while not self.event.is_set():
#             try:
#                 data = f.readline()
#             except Exception as e:
#                 logging.info(e)
#                 data = b"quit"
#             logging.info(data)
#
#             if data == "quit":
#                 logging.info('quit!')
#                 self.clients.pop(client)
#                 f.close()
#                 break
#             msg = "ack {}".format(data)
#             for c in self.clients.values():
#                 c.write(msg)
#                 c.flush()
#
# cs = ChatServer()
# cs.start()
#
# e = threading.Event()
# def showthreads():
#     while not e.wait(3):
#         logging.info(threading.enumerate())
#
# # threading.Thread(target=showthreads, daemon=True).start()
#
# while True:
#     cmd = input(">>>").strip()
#     if cmd == "quit":
#         cs.stop()
#         break


