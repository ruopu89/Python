# Condition用于生产者、消费者模型，为了解决生产者消费者速度匹配问题。
# 先看一个例子，消费者消费速度大于生产者生产速度
# 这个例子采用了消费者主动消费，消费者浪费了大量时间，原因是消费者会主动来查看有没有数据，这是浪费CPU时间。能否换成一种通知机制，有数据通知消费者来消费呢
# from threading import Thread,Event
# import logging
# import random
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# class Disptcher:
#     def __init__(self):
#         self.data = None
#         self.event = Event()
#
#     def produce(self, total):
#         for _ in range(total):
#             data = random.randint(0,100)
#             logging.info(data)
#             self.data = data
#             self.event.wait(1)
#         self.event.set()
#
#     def consume(self):
#         while not self.event.is_set():
#             data = self.data
#             logging.info("recieved {}".format(data))
#             self.data = None
#             self.event.wait(1)
#
# d = Disptcher()
# p = Thread(target=d.produce, args=(10,), name='producer')
# c = Thread(target=d.consume, name='consumer')
# c.start()
# p.start()
# =====================================================
# 使用Condition对象
# from threading import Thread,Event,Condition
# import logging
# import random
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# class Dispatcher:
#     def __init__(self):
#         self.data = None
#         self.event = Event()
#         self.cond = Condition()
#
#     def produce(self, total):
#         for _ in range(total):
#             data = random.randint(0, 100)
#             with self.cond:
#                 logging.info(data)
#                 self.data = data
#                 not self.cond.notify_all()
#             self.event.wait(1)
#         self.event.wait(1)
#
#     def consume(self):
#         while not self.event.is_set():
#             with self.cond:
#                 self.cond.wait()  # 阻塞等通知
#                 logging.info("received {}".format(self.data))
#                 self.data = None
#             self.event.wait(0.5)
#
# d = Dispatcher()
# p = Thread(target=d.produce, args=(10,), name='producer')
# c = Thread(target=d.consume, name='consumer')
# c.start()
# p.start()
# 上例中，消费者等待数据等待，如果生产者准备好了会通知消费者消费，省得消费者反复来查看数据是否就绪。
# 如果是一个生产者，多个消费者怎么改？
# from threading import Thread, Event, Condition
# import logging
# import random
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# class Dispatcher:
#     def __init__(self):
#         self.data = None
#         self.event = Event()
#         self.cond = Condition()
#
#     def produce(self, total):
#         for _ in range(total):
#             data = random.randint(0, 100)
#             with self.cond:
#                 logging.info(data)
#                 self.data = data
#                 self.cond.notify(2)
#             self.event.wait(1)
#         self.event.set()
#
#     def consume(self):
#         while not self.event.is_set():
#             with self.cond:
#                 self.cond.wait()
#                 logging.info("received {}".format(self.data))
#                 self.data = None
#             self.event.wait(0.5)
#
# d = Dispatcher()
# p = Thread(target=d.produce, args=(10,), name='producer')
#
# for i in range(5):
#     c = Thread(target=d.consume, name='consumer')
#     c.start()
# p.start()
# c.join()
# p.join()
# =============================================================
# import threading
# import random
# import logging
# logging.basicConfig(level=logging.INFO)
#
# class Dispatcher:
#     def __init__(self):
#         self.data = 0
#         self.event = threading.Event()
#         self.cond = threading.Condition()
#
#     def produce(self):
#         for i in range(100):
#             data = random.randint(1,100)
#             with self.cond:   # 进入进加锁，退出时解锁，保证线程安全
#                 self.data = data
#                 self.cond.notify_all()
#             self.event.wait(1)
#
#     def custom(self):
#         while True:
#             with self.cond:
#                 self.cond.wait()
#                 logging.info("custom: {}".format(self.data))
#             self.event.wait(1)
#
# d = Dispatcher()
# p = threading.Thread(target=d.produce)
# c = threading.Thread(target=d.custom)
# c1 = threading.Thread(target=d.custom)
#
# c.start()
# c1.start()
# p.start()
# p.start()
# e = threading.Event()
# e.wait(3)
#
# c.start()
# c1.start()
# ==================================================
import threading
import random
import logging

logging.basicConfig(level=logging.INFO, format="%(thread)d %(threadName)s %(message)s")


class Dispatcher:
    def __init__(self):
        self.data = 0

        self.event = threading.Event()
        self.cond = threading.Condition()

    def produce(self):  # 生产者一直在循环
        for i in range(10):
            data = random.randint(1, 100)
            logging.info(data)
            with self.cond:
                self.data = data  # 赋值
                self.cond.notify(2)  # 通知所有人
            self.event.wait(1)  # 借助event，等待1秒

    def custom(self):
        while True:
            with self.cond:  # 没收到通知就会阻塞，这是消费者被迫匹配生产者，消费者的能力应该比生产者略大一点。
                self.cond.wait()  # 第二个线程进来后，在这里还要等待，没有通知就会等在这
                logging.info(self.data)
            # self.event.wait(0.5)  # 消费比生产要快一点，上面永久等待时，这里没什么意义


d = Dispatcher()
p = threading.Thread(target=d.produce)  # 启动线程
for i in range(5):
    threading.Thread(target=d.custom, name="c-{}".format(i)).start()

p.start()  # 这里让生产者先执行
