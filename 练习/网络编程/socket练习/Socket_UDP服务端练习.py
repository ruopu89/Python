# import socket
# import threading
# import datetime
# import logging
#
# FORMAT = "%(asctime)s %(threadName)s %(thread)s %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# class ChatUDPServer:
#     def __init__(self, ip='10.0.30.50', port=9999, interval=10):
#         self.addr = (ip, port)
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.clients = {}
#         self.event = threading.Event()
#         self.interval = interval
#
#     def start(self):
#         self.sock.bind(self.addr)
#         threading.Thread(target=self.recv, name='recv').start()
#
#     def recv(self):
#         while not self.event.is_set():
#             localset = set()
#             data, raddr = self.sock.recvfrom(1024)
#
#             current = datetime.datetime.now().timestamp()
#             if data.strip() == b'^hb^':
#                 print('^^^^^^^^^^^^^^hb', raddr)
#                 self.clients[raddr] = current
#                 continue
#             elif data.strip() == b'quit':
#                 self.clients.pop(raddr, None)
#                 logging.info('{} leaving'.format(raddr))
#                 continue
#
#             self.clients[raddr] = current
#
#             msg = '{}. from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#             msg = msg.encode()
#
#             for c, stamp in self.clients.items():
#                 if current - stamp > self.interval:
#                     localset.add(c)
#                 else:
#                     self.sock.sendto(msg, c)
#             for c in localset:
#                 self.clients.pop(c)
#
#     def stop(self):
#         print(self.clients)
#         if self.clients:
#             for c in self.clients:
#                 self.sock.sendto(b'bye', c)
#         print(1, 'bye')
#         self.sock.close()
#         print(2, 'bye')
#         self.event.set()
#         print(3, 'bye')
#         exit()
#
# def main():
#     cs = ChatUDPServer()
#     cs.start()
#
#     while True:
#         cmd = input(">>>")
#         if cmd.strip() == 'quit':
#             print('quit!!!!!!')
#             cs.stop()
#             print(4, 'byby')
#             break
#         print(cmd)
#         logging.info(threading.enumerate())
#         logging.info(cs.clients)
#
# if __name__ == '__main__':
#     main()
# ===================================
from socket import *
from time import ctime

HOST = ''
PORT = 8888
BUFSIZ = 1024
ADDRESS = (HOST, PORT)

udpServerSocket = socket(AF_INET, SOCK_DGRAM)
udpServerSocket.bind(ADDRESS)      # 绑定客户端口和地址

while True:
    print("waiting for message...")
    data, addr = udpServerSocket.recvfrom(BUFSIZ)
    print("接收到数据：", data.decode('utf-8'))

    content = '[%s] %s' % (bytes(ctime(), 'utf-8'), data.decode('utf-8'))
    udpServerSocket.sendto(content.encode('utf-8'), addr)
    print('...received from and returned to:', addr)

udpServerSocket.close()