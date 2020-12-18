# import threading
# import logging
# import time
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# # def worker(s:threading.Semaphore):
# #     logging.info('in sub thread')
# #     logging.info(s.acquire())
# #     logging.info('sub thread over')
# #
# s = threading.Semaphore(3)
# # print(s._value)
# logging.info(s.acquire())
# # print(s._value)
# # # print(s.__dict__)
# logging.info(s.acquire())
# # print(s._value)
# logging.info(s.acquire())
# # print(s._value)
# #
# # threading.Thread(target=worker, args=(s,)).start()
# #
# # time.sleep(2)
#
# logging.info(s.acquire(False))
# logging.info(s.acquire(timeout=3))
#
# logging.info('released')
# s.release()
# logging.info(s.acquire())
# logging.info(s.acquire(False))
# =========================================================
# 连接池测试
# import threading
# import logging
# import time
# import random
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# class Conn:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name
#
# class Pool:
#     def __init__(self, count:int):
#         self.count = count
#         self.pool = [self._connect("conn-{}".format(x)) for x in range(self.count)]
#         self.semaphore = threading.Semaphore(count)
#
#     def _connect(self, conn_name):
#         return Conn(conn_name)
#
#     def get_conn(self):
#         print('-------------------------------')
#         self.semaphore.acquire()
#         print('================================')
#         conn = self.pool.pop()
#         return conn
#         # if len(self.pool) > 0:
#         #     return self.pool.pop()
#
#     def return_conn(self, conn:Conn):
#         self.pool.append(conn)
#         self.semaphore.release()
#
# pool = Pool(3)
#
# def worker(pool:Pool):
#     conn = pool.get_conn()
#     logging.info('conn:{}'.format(conn))
#     threading.Event().wait(random.randint(1,4))
#     pool.return_conn(conn)
#
# for i in range(6):
#     threading.Thread(target=worker, name="worker-{}".format(i), args=(pool,)).start()
    # threading.Thread(target=worker, args=(pool,)).start()
# =======================================================
# ### 问题
# `self.conns.append(conn)`这一句要不要加锁？
# #### 1. 从程序逻辑上分析
# ##### 1.1 假设如果还没有使用信号量，就release，会怎么样？
# import logging
# import threading
#
# sema = threading.Semaphore(3)
# logging.warning(sema.__dict__)
# for i in range(3):
#     sema.acquire()
# logging.warning('~~~~~~~~~~~~~~~~~~~')
# logging.warning(sema.__dict__)
#
# for i in range(4):
#     sema.release()
# logging.warning('release:{}'.format(sema.__dict__))
#
# for i in range(3):
#     sema.acquire()
# logging.warning('~~~~~~~~~~~~~~~~~~~')
# logging.warning(sema.__dict__)
# sema.acquire()
# logging.warning('~~~~~~~~~~~~~~~~~~~~~')
# logging.warning(sema.__dict__)
# ==============================================
# import queue
#
# q = queue.Queue(9)
#
# if q.qsize() == 8:
#     q.put()
#
# if q.qsize() == 1:
#     q.get()
# =================================
import threading
import logging
logging.basicConfig(level=logging.INFO, format="%(thread)d %(threadName)s %(message)s")
import time

def work(s:threading.Semaphore):
    logging.info("in sub")
    s.acquire()
    logging.info("end sub")

s = threading.Semaphore(3)
logging.info(s.acquire())
logging.info(s.acquire())
logging.info(s.acquire())

threading.Thread(target=work, args=(s,)).start()
print("===============================")
time.sleep(2)

logging.info(s.acquire(False))
logging.info(s.acquire(timeout=3))

s.release()
print('end main')