# UDP版群聊服务端代码
# import socket
# import threading
# import datetime
# import logging
#
# FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# class ChatUDPServer:
#     def __init__(self, ip='10.0.30.50', port=9999):
#         self.addr = (ip, port)
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.clients = set()
#         self.event = threading.Event()
#
#     def start(self):
#         self.sock.bind(self.addr)
#         threading.Thread(target=self.recv, name='recv').start()
#
#     def recv(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)
#
#             if data.strip() == b'quit':
#                 if raddr in self.clients:
#                     self.clients.remove(raddr)
#                 logging.info('{} leaving'.format(raddr))
#                 continue
#
#             self.clients.add(raddr)
#
#             msg = '{} from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#             msg = msg.encode()
#             for c in self.clients:
#                 self.sock.sendto(msg, c)
#
#     def stop(self):
#         for c in self.clients:
#             self.sock.sendto(b'bye', c)
#         self.sock.close()
#         self.event.set()
#
# def main():
#     cs = ChatUDPServer()
#     cs.start()
#
#     while True:
#         cmd = input(">>>")
#         if cmd.strip() == 'quit':
#             logging.info('quit!!!!!')
#             cs.stop()
#             break
#         logging.info(threading.enumerate())
#         logging.info(cs.clients)
#
# if __name__ == '__main__':
#     main()
# =========================================================
# UDP群聊客户端代码
# import threading
# import socket
# import logging
#
# FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# class ChatUdpClient:
#     def __init__(self, rip='127.0.0.1', rport=9999):
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.raddr = (rip, rport)
#         self.event = threading.Event()
#
#     def start(self):
#         self.sock.connect(self.raddr)
#
#         threading.Thread(target=self.recv, name='recv').start()
#
#     def recv(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)
#
#             msg = '{} from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#
#     def send(self, msg:str):
#         self.sock.sendto(msg.encode(), self.raddr)
#
#     def stop(self):
#         self.sock.close()
#         self.event.set()
#
# def main():
#     cc1 = ChatUdpClient()
#     cc2 = ChatUdpClient()
#     cc1.start()
#     cc2.start()
#     print(cc1.sock)
#     print(cc2.sock)
#
#     while True:
#         cmd = input("Input your words >>>")
#         if cmd.strip() == 'quit':
#             cc1.stop()
#             cc2.stop()
#             break
#         cc1.send(cmd)
#         cc2.send(cmd)
#
# if __name__ == '__main__':
#     main()
#==================================================
# 客户端增加心跳数据
# import threading
# import socket
# import logging
#
# FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatUdpClient:
#     def __init__(self, rip='127.0.0.1', rport=9999):
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.raddr = (rip, rport)
#         self.event = threading.Event()
#
#     def start(self):
#         self.sock.connect(self.raddr)  # 占用本地地址和端口，设置远端地址和端口
#         threading.Thread(target=self.recv, name='recv').start()
#
#     def _sendhb(self):  # 心跳
#         while not self.event.wait(5):
#             self.send('^hb^')
#
#     def recv(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)
#
#             msg = '{}. from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#
#     def send(self, msg: str):
#         self.sock.sendto(msg.encode(), self.raddr)
#
#     def stop(self):
#         self.send('quit')  # 通知服务端退出
#
#         self.sock.close()
#         self.event.set()
#
#
# def main():
#     cc1 = ChatUdpClient()
#     cc2 = ChatUdpClient()
#     cc1.start()
#     cc2.start()
#     print(cc1.sock)
#     print(cc2.sock)
#
#     while True:
#         cmd = input("Input your words >>>")
#         if cmd.strip() == 'quit':
#             cc1.stop()
#             cc2.stop()
#             break
#         cc1.send(cmd)
#         cc2.send(cmd)
#
#
# if __name__ == '__main__':
#     main()
# ======================
# import threading
# import socket
# import logging
#
# class ChatUdpClient:
#     def __init__(self, rip='10.0.30.50', rport=9999):
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.raddr = (rip, rport)
#         self.event = threading.Event()
#         # self.clients = set()
#
#     def start(self):
#         self.sock.connect(self.raddr)
#         threading.Thread(target=self._sendhb, name='heartbeat', daemon=True).start()
#         threading.Thread(target=self.recv, name='recvfrom').start()
#
#     def _sendhb(self):
#         while not self.event.wait(5):
#             self.send('^hb^')
#
#     def recv(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)
#             msg = "{}. from {}:{}".format(data.decode(), *raddr)
#             logging.info(msg)
#
#     def send(self, msg:str):
#         self.sock.sendto(msg.encode(), self.raddr)
#
#     def stop(self):
#         self.send('quit')
#         self.sock.close()
#         self.event.set()
#         return


# def main():
#     cc1 = ChatUdpClient()
#     cc2 = ChatUdpClient()
#     cc1.start()
#     cc2.start()
#     print(cc1.sock)
#     print(cc2.sock)
#
#     while True:
#         cmd = input("Input your words >>>")
#         if cmd == 'quit':
#             cc1.stop()
#             cc2.stop()
#             break
#         cc1.send(cmd)
#         cc2.send(cmd)
#
# if __name__ == '__main__':
#     main()
# =====================================
# from socket import *
#
# HOST = '127.0.0.1'
# PORT = 8888
# BUFSIZ = 1024
# ADDRESS = (HOST, PORT)
#
# udpClientSocket = socket(AF_INET, SOCK_DGRAM)
#
# while True:
#     data = input('>')
#     if not data:
#         break
#
#     # 发送数据
#     udpClientSocket.sendto(data.encode('utf-8'), ADDRESS)
#     # 接收数据
#     data, ADDR = udpClientSocket.recvfrom(BUFSIZ)
#     if not data:
#         break
#     print("服务器端响应：", data.decode('utf-8'))
#
# udpClientSocket.close()
# =================================
# import threading
# import logging
# import socket
# logging.basicConfig(format='%(thread)s %(threadName)s %(message)s', level=logging.INFO)
#
# sock = socket.socket(type=socket.SOCK_DGRAM)
# ip = '127.0.0.1'
# port = 8888
# addr = (ip, port)
#
# data = 'Udp1'.encode()
# sock.sendto(data, addr)
# data, caddr = sock.recvfrom(1024)
# logging.info('data: {}, caddr: {}'.format(data, caddr))

# ==========================
import socket
import threading

a = 1
b = socket.socket()
c = threading.Event()
c.set()
print(c.wait(a))
