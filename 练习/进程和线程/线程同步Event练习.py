# Event
# 老板雇佣了一个工人，让他生产杯子，老板一直等着这个工人，直到生产了10个杯子
from threading import Event,Thread
import logging
import time
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# def boss(event:Event):
#     logging.info("I'm boss, waiting for U.")
#     # event.set()
#     logging.info("event.wait(): {}".format(event.wait()))
#     event.wait()
#     logging.info("Good Job.")
#
# def worker(event:Event, count=10):
#     logging.info("I'm working for U.")
#     cups = []
#     while True:
#         logging.info('make 1')
#         # time.sleep(0.5)
#         cups.append(1)
#         logging.info("event status {}".format(event.is_set()))
#         if len(cups) > count:
#             event.set()
#             # logging.info("event status {}".format(event.is_set()))
#             break
#     logging.info('I finished my job. cups={}'.format(cups))
#
# event = Event()
# w = Thread(target=worker, args=(event,))
# b = Thread(target=boss, args=(event,))
# w.start()
# b.start()
# =========================================
# event = Event()
# print(1, event.wait(0.5))
# event.set()
# logging.basicConfig(format='%(message)s',level=logging.INFO)
# logging.info("event.wait: {}".format(event.wait()))
# print(2, event.wait())
# 如果直接在主线程中打印wait()方法的值时，要设置时长，默认返回False。
# ============================================================
# wait的使用
from threading import Event,Thread
import logging
logging.basicConfig(level=logging.INFO)

e = Event()

def do(event:Event, interval:int):
    while not event.wait(interval):
        logging.info('do sth.')

Thread(target=do, args=(e,3)).start()
e.wait(10)  # 也可以使用time.sleep(10)
e.set()
print('main exit')
# Event的wait优于time.sleep，它会更快的切换到其它线程，提高并发效率
# ===========================================================
# Event练习
# 实现Timer，延时执行的线程。延时计算`add(x, y)`
# 思路
# Timer的构造函数中参数得有哪些？如何实现start启动一个线程执行函数，如何cancel取消待执行任务
# from threading import Event,Thread
# import datetime
# import logging
# logging.basicConfig(level=logging.INFO)
#
# def add(x:int, y:int):
#     logging.info(x + y)
#
# class Timer:
#     def __init__(self, interval, fn, *args, **kwargs):
#         self.interval = interval
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs
#         self.event = Event()
#
#     def start(self):
#         Thread(target=self.__run).start()
#
#     def cancel(self):
#         self.event.set()
#
#     def __run(self):
#         start = datetime.datetime.now()
#         logging.info('waiting')
#
#         # self.event.wait(self.interval)
#         # if not self.event.is_set():
#         if not self.event.wait(self.interval):  # 这一行代替上面两行
#             logging.info('chuan can')
#             self.fn(*self.args, **self.kwargs)
#         else:
#             logging.info('tiao guo chuan can')
#         delta = (datetime.datetime.now() - start).total_seconds()
#         logging.info(('finished {}.'.format(delta)))
#         self.event.set()
#
# t = Timer(10, add, 4, 50)
# t.start()
# e = Event()
# e.wait(4)
# t.cancel()
# print('=========================')
# ====================================================
# 网上找到的练习
# 有10个单身狗，对面100米有10个美女，同时起跑，一人一个，自由选择，先到先得
# import threading
#
# eEvent = threading.Event()
#
# def get_girl_friend(id):
#     print("单身狗{}都准备完毕，内置Flag状态：{}.....".format(id,eEvent.isSet()))
#     eEvent.wait(3)
#     print("单身狗%s告别单身....."%id)
#
# if __name__ == "__main__":
#     thread_list = list()
#
#     for i in range(1,11):
#         t = threading.Thread(target=get_girl_friend,args=(i,))
#         t.start()
#     thread_list.append(t)
#
#     eEvent.set()
#
#     for t in thread_list:
#         t.join()
#     print("程序结束！")
#======================================
# from threading import Event, Thread
# import logging
# import datetime
# logging.basicConfig(level=logging.INFO)
#
# def add(x:int, y:int):
#     logging.info(x+y)
#
# class Timer:
#     def __init__(self, interval, fn, *args, **kwargs):
#         self.interval = interval
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs
#         self.event = Event()
#
#     def start(self):
#         Thread(target=self.__run).start()
#
#     def cancel(self):
#         self.event.set()
#
#     def __run(self):
#         start = datetime.datetime.now()
#         logging.info('waiting')
#
#         self.event.wait(self.interval)
#         if not self.event.is_set():
#             logging.info('chuan can')
#             self.fn(*self.args, **self.kwargs)
#         else:
#             logging.info('tiao guo chuan can')
#         delta = (datetime.datetime.now() - start).total_seconds()
#         logging.info('finished {}'.format(delta))
#         self.event.set()
#
# t = Timer(10, add, 4, 50)
# t.start()
# e = Event()
# # e.wait(4)
# t.cancel()