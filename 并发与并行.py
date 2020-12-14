# import threading
# import time
#
# class MyThread(threading.Thread):  # 继承
# # 使用pycharm中右键里的Generate中的override重写下面两个方法，这两个方法是 threading.Thread的
#     def start(self) -> None:
#         print('start')  # 因为执行时什么都看不到，所以这里打印一个run
#         super().start()
#
#     def run(self) -> None:
#         print('run')   # 这里也一样是为了看执行效果
#         super().run()
#
#
# def worker(n=5):
#     print(threading.current_thread())
#     for _ in range(n):
#         time.sleep(0.5)
#         print('welcome magedu')
#     print('thread over')
#
#
# t = MyThread(target=worker, name='w1', args=(5,))
# # Thread是一个类，我们要给这个类实例化并传一个参数，这里不需要给worker函数传参，就不需要写
# t.start()
# # t.run()

# import threading
# import logging
# logging.basicConfig(level=logging.INFO)
# import time
#
# def worker():
#     for x in range(10):
#         msg = "{} is running".format(threading.current_thread())
#         logging.info(msg)
#         print(threading.enumerate())
#         threading.Thread(target=worker1, name="worker-{}".format(x), daemon=False).start()
#
# def worker1():
#     for x in range(100):
#         msg = "$$$$$$$$${} is running".format(threading.current_thread())
#         logging.info(msg)
#
# t = threading.Thread(target=worker, daemon=True, name="worker-{}".format(0))
# t.start()
# t.join()

# print('ending')
# print(threading.enumerate())

import threading
import time

# class a:
#     def __init__(self, x):
#         a.x = x

# a = threading.local()
# # a = threading.local()
# def worker():
#     a.x = 0
#     for i in range(100):
#         time.sleep(0.0001)
#         a.x += 1
#     print(threading.current_thread(), a.x)
#
# for i in range(10):
#     threading.Thread(target=worker).start()

import threading
import time
import logging
FORMAT = "%(asctime)s %(thread)d %(message)s %(schoolname)s"  # 这里只能用C风格
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%d-%H:%M:%S")
# 一般日志级别定到INFO，比这个级别低的就不打印了
d = {"schoolname":'magedu.com'}

def add(x, y):
    log = logging.getLogger('a')
    # log = logging.getLogger('')
    # log = logging.getLogger()
    print(log.name)
    print(log, type(log))

    log.warning("{} {}".format(threading.enumerate(), x+y),  extra=d)
# 从输出结果可以看出是INFO级别，之后是用户名。默认格式就是级别：用户：打印的信息
    log.info("%s %s", x, y, extra=d)
# 这与logging.info输出的内容是关不多的
t = threading.Timer(1, add, args=(3, 4))
t.start()
