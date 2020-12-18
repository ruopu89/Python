# 连接池是连接的容器，用于管理连接。有总容量，最大最小值
import threading
import logging
logging.basicConfig(level=logging.INFO, format="%(thread)d %(threadName)s %(message)s")
import time

class Conn:
    def __init__(self, name):
        self.name = name

class Pool:
    def __init__(self, count=3):
        self.count = count
        self.sema = threading.BoundedSemaphore(count)
        self.pool = [ Conn("conn-{}".format(i)) for i in range(count) ]

    def get_conn(self):
        self.sema.acquire()
        data = self.pool.pop()
        return data

    def return_conn(self, conn:Conn):
        self.pool.append(conn)
        self.sema.release()

pool = Pool(3)
# conn = pool.get_conn()
# conn = pool.get_conn()
# conn = pool.get_conn()
# conn = pool.get_conn()
for i in range(10):
    conn = pool.get_conn()
    logging.info(conn.name)
    pool.return_conn(conn)


print('end main')
