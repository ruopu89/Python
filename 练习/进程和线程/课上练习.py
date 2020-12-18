# 线程启动
# import threading
# import time
# def worker():
#     while True:
#         time.sleep(1)
#         print("I'm working")
#     print('Fineshed')
#
# t = threading.Thread(target=worker, name='worker')
# t.start()
# =============================================================
# import threading
# import time
#
# def worker():
#     count = 0
#     while True:
#         if (count > 5):
#             break
#         time.sleep(1)
#         print("I'm working")
#         count += 1
#
# t = threading.Thread(target=worker, name='worker')
# t.start()
# t.join()  # 加入此行，就会使子线程都结束后，再执行主线程最后的print('=====end=====')
#
# print('=====end=====')
#
# import threading
# import time
#
# def test(p):
#     time.sleep(0.001)
#     print(p)
#
# ts = []
#
# for i in range(15):
#     th = threading.Thread(target=test, args=[i])
#     ts.append(th)
#
# for i in ts:
#     i.start()
#     i.join()
#
# print("it is end !")
# ===================================================================
# import threading
#
# def worker():
#     print('welcome magedu')
#     print('thread over')
#
#
#
# t = threading.Thread(target=worker)
# t.start()
# t.join()
# print('=======end========', end='')
# ================================================
# import threading
# import time
#
# def worker():
#     for _ in range(10):
#         time.sleep(0.5)
#         print('welcome magedu')
#         print('thread over')
#
# t = threading.Thread(target=worker)
# t.start()
# ==============================================================================
# import threading
# import time
#
# def worker():
#     for _ in range(10):
#         time.sleep(0.5)
#         print('welcome magedu')
#     print('thread over')
#
# def worker1():
#     for _ in range(10):
#         time.sleep(0.5)
#         print('welcome magedu ......')
#     print('thread over ......')
#
# t = threading.Thread(target=worker, name='w1')
# t.start()
# t = threading.Thread(target=worker1, name='w1')
# t.start()
# ============================================================
# import threading
# import time
#
# def worker():
#     for _ in range(10):
#         time.sleep(0.5)
#         print('welcome magedu 123123123')
#     print('thread over 123123123')
#
# def worker1():
#     count = 0
#     while True:
#         time.sleep(0.5)
#         print('welcome magedu ... ...')
#         count += 1
#         if count > 3:
#             raise Exception('New exception')
#     print('thread over ... ...')
#
# t = threading.Thread(target=worker, name='w')
# t.start()
#
# t = threading.Thread(target=worker1, name='w1')
# t.start()
# ===============================================================
# import threading
# import time
#
# def worker(n):
#     for _ in range(n):
#         time.sleep(0.5)
#         print('welcome magedu')
#     print('thread over')
#
# t = threading.Thread(target=worker, name='w1', args=(5,))
# t.start()
# ==================================================================
# import threading
# import time
#
# def worker(n=5):
#     print("current_thread:{}".format(threading.current_thread().__dict__))  # 返回当前线程对象
#     print("main_thread:{}".format(threading.main_thread()))  # 返回主线程对象
#     print("active_thread:{}".format(threading.active_count()))  # 当前处于alive状态的线程个数
#     print("enumerate:{}".format(threading.enumerate()))  # 返回所有活着的线程的列表，不包括已经终止的线程和未开始的线程
#     for _ in range(n):
#         time.sleep(0.5)
#         print('welcome magedu')
#     print('thread over')
#
# print(2, "current_thread:{}".format(threading.current_thread()))
#
# t = threading.Thread(target=worker, name='w1', args=(5,))
#
# t.start()
#
# print(2222, "enumerate:{}".format(threading.enumerate()))
# =========================================
# import threading
# import time
#
# def worker(n=5):
#     print(threading.current_thread().name)
#     print(threading.main_thread().name)
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread().is_alive())
#     print("in worker {}".format(threading.main_thread().is_alive()))
#     for _ in range(n):
#         time.sleep(0.5)
#         print('welcome magedu')
#     print('thread over')
#
# print(threading.current_thread())
#
# t = threading.Thread(target=worker, name='w1', args=(5,))
# t.start()
# t1 = threading.Thread(target=worker, name='w1', args=(5,))
# print(threading.enumerate())
# print(1, threading.current_thread().is_alive())
# ================================================================
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def start(self) -> None:
#         print('start')
#         super().start()
#
#     def run(self) -> None:
#         print('run')
#         super().run()
#
# def worker(n=5):
#     print(threading.current_thread())
#     for _ in range(n):
#         time.sleep(0.5)
#         print('welcome magedu')
#     print('thread over')

# print(threading.current_thread())
# print('===================================')
# t = MyThread(target=worker, name='w1')
# t.start()
#
# t.run()
# print('===================================')

# t1 = MyThread(target=worker, name='w2')
# t1.run()
# t1.start()
# ===========================================================
# import threading
# import time
#
# def test(p):
#     time.sleep(0.001)
#     print(threading.current_thread())
#     print(p)
#
# ts = []
#
# for i in range(15):
#     th = threading.Thread(target=test, args=[i])
#
#     ts.append(th)
#
# for i in ts:
#     i.start()
#     i.join()
#
#
# print("it is end !")
# =====================================================
# import threading
# import logging
# logging.basicConfig(level=logging.INFO)
#
# def worker():
#     for x in range(100):
#         msg = "{} is running".format(threading.current_thread())
#         logging.info(msg)
#
# def worker1():
#     for x in range(10):
#         msg = "{} is running".format(threading.current_thread())
#         logging.info(msg)
#
# threading.Thread(target=worker, name="$$$$worker-{}".format(0),daemon=True).start()
#
# threading.Thread(target=worker1, name="^^^^worker1-{}".format(0)).start()
#
# print('ending')
#
# print(threading.enumerate())
# ====================================================================================
# import threading
# import logging
# logging.basicConfig(level=logging.INFO)
#
# def worker():
#     threading.Thread(target=worker1, name="worker1-{}".format(0)).start()
#     for x in range(100):
#         msg = "{}, {} is running".format(x, threading.current_thread())
#         logging.info(msg)
#
# def worker1():
#     for x in range(1000):
#         msg = "{} is running".format(threading.current_thread())
#         logging.info(msg)
#
# threading.Thread(target=worker, name="$$$$worker-{}".format(0), daemon=True).start()
#
# print('ending')
# print(threading.enumerate())

# import threading
# import time
# a = threading.local()
#
# def worker():
#     a.x = 0
#     for i in range(100):
#         time.sleep(0.001)
#         a.x += 1
#     print(threading.current_thread(), a.x)
#     print(a.__dict__)
#
# for i in range(10):
#     threading.Thread(target=worker).start()
# =====================================================================
# import threading
#
# X = 'abc'
# ctx = threading.local()
# ctx.x = 123
#
# print(ctx, type(ctx), ctx.x)
#
#
# def work():
#     print(X)
#     print(ctx)
#     # ctx.x = 878
#     # ctx.y = 222
#     print(ctx.x)  # 如果上面不定义ctx.x = 878，这里就会报错
#     print('Good job')
#     print(ctx.__dict__)
#
#
# threading.Thread(target=work).start()
# ======================================================================
# （日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）
# import threading
# import time
# import logging
#
# FORMAT = "%(asctime)s %(thread)d %(message)s %(schoolname)s"
# logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%d-%H:%M:%S",filename='/home/shouyu/下载/logtest.log')
# # 2020-09-09 16:13:05,308 140073435166464 [<_MainThread(MainThread, stopped 140073447057216)>, <Timer(Thread-1, started 140073435166464)>],7
# # logging.basicConfig(level=logging.INFO)
# # INFO:root:[<_MainThread(MainThread, stopped 140416444733248)>, <Timer(Thread-1, started 140416432842496)>],7
# # 默认只显示message信息，前面是日志级别和logger。message信息是在logging.info中定义的
# d = {"schoolname":"magedu.com"}
#
# def add(x,y):
#     logging.warning("{},{}".format(threading.enumerate(),x+y),extra=d)
#     logging.info("%s %s",x,y,extra=d)
#
# t = threading.Timer(1, add, args=(3,4))
# t.start()
# ==============================================================
# import logging
#
# FORMAT = '%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'
# logging.basicConfig(level=logging.INFO,format=FORMAT)
#
# logging.info('I am {}'.format(20))
# logging.info('I am %d %s', 20, 'years old.')
# ========================================================
# import logging
#
# FORMAT = '%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'
# logging.basicConfig(format=FORMAT)
#
# logging.info('I am {}'.format(20))
# logging.warning('I am %s %s',20,'years old')
# =================================================
# import logging
#
# FORMAT = '%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s %(school)s'
# logging.basicConfig(format=FORMAT, level=logging.WARNING)
# d = {'school':'magedu.com'}
# logging.info('I am %s %s', 20, 'years old', extra=d)
# logging.warning('I am %s %s', 20, 'years old.', extra=d)
# ===========================================================
# 修改日期格式
# import logging
#
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y%m%d %I:%M:%S')
# logging.warning('this event was logged.')
# =====================================================
# 输出到文件
# import logging
#
# logging.basicConfig(format='%(asctime)s %(message)s', filename='/tmp/test20200910.txt')
#
# for _ in range(5):
#     logging.warning('this event was logged.')
# =========================================================
# 层次关系
# import logging
#
# root = logging.getLogger()
# print(root.name, type(root), root.parent, id(root))
#
# logger = logging.getLogger(__name__)
# print(logger.name, type(logger), id(logger.parent), id(logger))
#
# loggerchild = logging.getLogger(__name__ + 'child')
# print(loggerchild.name, type(loggerchild), id(loggerchild.parent), id(loggerchild))
# =================================================================
# Level级别设置
# import logging
#
# FORMAT = '%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# logger = logging.getLogger(__name__)
# print(logger.name, type(logger))
# print(logger.getEffectiveLevel())
#
# logger.info('hello1')
# logger.setLevel(28)
# #
# print(logger.getEffectiveLevel())
# logger.info('hello2')
# logger.warning('hello3 warning')
#
# root = logging.getLogger()
# print(root)
# root.info('hello4 info root')
# ============================================
# Handler
# import logging
#
# FORMAT = '%(asctime)s %(name)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# logger = logging.getLogger('test')
# print(logger.name, type(logger))
# logger.info('line 1')
#
# handler = logging.FileHandler('/tmp/test0910.log','w')
# logger.addHandler(handler)
#
# logger.info('line 2')
# ==========================================================
# 日志流，level的继承
# import logging
#
# FORMAT = '%(asctime)s %(name)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
# root = logging.getLogger()
#
# log1 = logging.getLogger("s")
# log1.setLevel(logging.WARNING)
# log1.error('log1 error')
#
# log2 = logging.getLogger('s.s1')
# log2.critical('log2 warning')
# ====================================================
# import logging
#
# logging.basicConfig(format='%(name)s %(asctime)s %(message)s',level=logging.INFO)
#
# root = logging.getLogger()
# root.setLevel(logging.ERROR)
# print('root', root.handlers)
# h0 = logging.StreamHandler()
# h0.setLevel(logging.WARNING)
# root.addHandler(h0)
# print('root', root.handlers)
# for h in root.handlers:
#     print("root handler = {}, formatter = {}".format(h, h.formatter))
#
# log1 = logging.getLogger('s')
# log1.setLevel(logging.ERROR)
# h1 = logging.FileHandler('/tmp/test0910.log')
# h1.setLevel(logging.WARNING)
# print('log1 formatter',h1.formatter)
# log1.addHandler(h1)
# print('log1', log1.handlers)
#
# log2 = logging.getLogger('s.s1')
# log2.setLevel(logging.INFO)
# h2 = logging.FileHandler('/tmp/test0910.log')
# h2.setLevel(logging.WARNING)
# # print('log2 formatter', h2.formatter)
# f2 = logging.Formatter("%(asctime)s %(message)s",datefmt="%Y/%m%d %X")
# h2.setFormatter(f2)
# # print('log2 formatter', h2.formatter)
# log2.addHandler(h2)
# # print('log2', log2.handlers)
# log2.error('test handler format')

# log3 = logging.getLogger('s.s1.s2')
# log3.setLevel(logging.INFO)
# print(log3.getEffectiveLevel())
# log3.warning('log3')
# print('log3', log3.handlers)
# ================================================
# import logging
# def log():
#     #创建logger，如果参数为空则返回root logger
#     logger = logging.getLogger("nick")
#     logger.setLevel(logging.DEBUG)  #设置logger日志等级
#     #这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
#     if not logger.handlers:
#         #创建handler
#         fh = logging.FileHandler("test.log",encoding="utf-8")
#         ch = logging.StreamHandler()
#
#         #设置输出日志格式
#         formatter = logging.Formatter(
#             fmt="%(asctime)s %(name)s %(filename)s %(message)s",
#             datefmt="%Y/%m/%d %X"
#             )
#
#         #为handler指定输出格式
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#
#         #为logger添加的日志处理器
#         logger.addHandler(fh)
#         logger.addHandler(ch)
#
#     return logger #直接返回logger
#
# logger = log()
# logger.warning("泰拳警告")
# logger.info("提示")
# logger.error("错误")
# logger.debug("查错")