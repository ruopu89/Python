# 订单要求生产1000个杯子，组织10个工人生产
# 下面的例子没有加锁，导致多生产了杯子
# import threading
# from threading import Thread,Lock
# import logging
# import time
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
# cups = []
#
# def worker(count=10):
#     logging.info("I'm working for U.")
#     while len(cups) < count:
#         time.sleep(0.0001)
#         cups.append(1)
#     logging.info('I finished. cups = {}'.format(len(cups)))
#
# for _ in range(10):
#     Thread(target=worker, args=(1000,)).start()
# ===========================================================
# 下面的例子加了Lock锁
# import threading
# from threading import Thread,Lock
# import logging
# import time
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT,level=logging.INFO)
#
# cups = []
# lock = Lock()
#
# def worker(count=10):
#     logging.info("I'm working for U.")
#     flag = False
#     while True:
#         lock.acquire()
#
#         if len(cups) >= count:
#             flag = True
#         time.sleep(0.0001)
#         if not flag:
#             cups.append(1)
#         lock.release()
#         if flag:
#             break
#     logging.info('I finished. cups = {}'.format(len(cups)))
# for _ in range(10):
#     Thread(target=worker, args=(1000,)).start()
# ==============================================================
# 计数器类，可以加、可以减
# 下面的例子依然没有加锁，执行会有问题
# import threading
# import time
#
# class Counter:
#     def __init__(self):
#         self._val = 0
#
#     @property
#     def value(self):
#         return self._val
#
#     def inc(self):
#         self._val += 1
#
#     def dec(self):
#         self._val -= 1
#
# def run(c:Counter, count=100):
#     for _ in range(count):
#         for i in range(-50, 50):
#             if i < 0:
#                 c.dec()
#             else:
#                 c.inc()

# c = Counter()
# c1 = 10
# c2 = 230
# for i in range(c1):
#     threading.Thread(target=run, args=(c,c2)).start()
#
# print(c.value)  # 因为执行太快，执行显示的0是主线程打印出的0，但子线程可能还没有执行完。不会如此平衡的。
# =============================================================
# 加锁与解锁
# 还是上面的例子
# import threading
# import time
#
# class Counter:
#     def __init__(self):
#         self._val = 0
#         self.__lock = threading.Lock()
#
#     @property
#     def value(self):
#         with self.__lock:
#             return self._val
#
#     def inc(self):
#         try:
#             self.__lock.acquire()
#             self._val += 1
#         finally:
#             self.__lock.release()
#
#     def dec(self):
#         with self.__lock:
#             self._val -= 1
#
# def run(c:Counter, count=100):
#     for _ in range(count):
#         for i in range(-50, 50):
#             if i < 0:
#                 c.dec()
#             else:
#                 c.inc()
#
# c = Counter()
# c1 = 10
# c2 = 1000
# for i in range(c1):
#     threading.Thread(target=run, args=(c, c2)).start()
#
# # print(c.value)
# while True:
#     time.sleep(1)
#     if threading.active_count() == 1:
#         print('Main thread: {}'.format(threading.enumerate()))
#         print(c.value)
#         break
#     else:
#         print('threading.enumerate: {}'.format(threading.enumerate()))
# ========================================
# 网络上找到的练习
# 对全局变量累加1000000次，因为没加锁，导致结果异常
# import threading
#
# g_num = 0
#
# def my_thread1():
#     global g_num
#     for i in range(0, 1000000):
#         g_num = g_num + 1
#
# def my_thread2():
#     global g_num
#     for i in range(0, 1000000):
#         g_num = g_num + 1
#
# def main(i):
#     global g_num
#     g_num = 0
#     t1 = threading.Thread(target=my_thread1)
#     t2 = threading.Thread(target=my_thread2)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print(("第%d次计算结果：%d"%(i,g_num)))
#
# if __name__ == '__main__':
#     for i in range(1,5):
#         main(i)
# 加锁解决
# import threading
#
# g_num = 0
# mutex = threading.Lock()
#
# def my_thread1():
#     global g_num
#     for i in range(0,1000000):
#         mutex.acquire()
#         g_num = g_num + 1
#         mutex.release()
#
# def my_thread2():
#     global g_num
#     for i in range(0,1000000):
#         mutex.acquire()
#         g_num = g_num + 1
#         mutex.release()
#
# def main(i):
#     global g_num
#     g_num = 0
#     t1 = threading.Thread(target=my_thread1)
#     t2 = threading.Thread(target=my_thread2)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("第%d次计算结果：%d"%(i,g_num))
#
# if __name__ == "__main__":
#     for i in range(1,5):
#         main(i)
#
# 线程死锁
# 1.单个互斥锁的死锁：acquire()/release() 是成对出现的，互斥锁对资源锁定之后就一定要解锁，否则资源会一直处于锁定状态，其他线程无法修改；就好比上面的代码，任何一个线程没有释放资源release()，程序就会一直处于阻塞状态(在等待资源被释放)，不信你可以试一试~
#
# 2.多个互斥锁的死锁：在同时操作多个互斥锁的时候一定要格外小心，因为一不小心就容易进入死循环，假如有这样一个场景：boss让程序员一实现功能一的开发，让程序员二实现功能二的开发，功能开发完成之后一起整合代码！

# import threading
# import time
#
# mutex_one = threading.Lock()
# mutex_two = threading.Lock()
#
# def programmer_thread1():
#     mutex_one.acquire()
#     print("我是程序员1，module1开发正式开始，谁也别动我的代码")
#     time.sleep(2)
#
#     mutex_two.acquire()
#     print("等待程序员2通知我合并代码")
#     mutex_two.release()
#
#     mutex_one.release()
#
# def programmer_thread2():
#     mutex_two.acquire()
#     print("我是程序员2，module2开发正式开始，谁也别动我的代码")
#     time.sleep(2)
#
#     mutex_one.acquire()
#     print("等待程序员1通知我合并代码")
#     mutex_one.release()
#
#     mutex_two.release()
#
# def main():
#     t1 = threading.Thread(target=programmer_thread1)
#     t2 = threading.Thread(target=programmer_thread2)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("整合代码结束 ")
#
# if __name__ == "__main__":
#     main()
# =============================================
# 10个人生产100个杯子
# import logging
# import threading
#
# logging.basicConfig(level=logging.INFO)
#
# cups = []
#
# def worker(task=100):
#     while True:
#         count = len(cups)
#         logging.info(count)
#         if count >= task:
#             break
#         cups.append(1)
#         logging.info("{}".format(threading.current_thread().name))
#     logging.info("{}".format(len(cups)))
#
# for x in range(10):
#     threading.Thread(target=worker, args=(100,)).start()
# ==========================================================
import logging
import threading

logging.basicConfig(level=logging.INFO)

cups = []

lock = threading.Lock()

def worker(task=100):
    # lock = threading.Lock()
    while True:
        lock.acquire()
        count = len(cups)
        # lock.release()
        logging.info(count)
        if count >= task:
            lock.release()
            break
        # lock.acquire()
        cups.append(1)
        lock.release()
        logging.info("{}".format(threading.current_thread().name))
    logging.info("{}".format(len(cups)))

for x in range(10):
    threading.Thread(target=worker, args=(100,)).start()