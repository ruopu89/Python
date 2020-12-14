# # 老坂等工厂做好10个杯子
#
# import threading
# import logging
# import time
# logging.basicConfig(level=logging.INFO)
#
# # 第一步先把框架搭出来。有一个老板，一个工人，他们是两个个体。我们关注的是他们以后能干什么事，关心的是动作，动作就是函数
#
# # cups = []
# #
# # def boss():
# #     pass
# #
# # def worker(n):  # n表示工人要完成的杯子量
# #     pass
# #
# # ================================================
# cups = []
#
# def boss():
#     pass
#
# def worker(n):  # n表示工人要完成的杯子量
#     while True:
#         time.sleep(0.5)
#         cups.append(1)  # 完成1个加1个
#         logging.info('make 1')  # 生产1个杯子就打印一下
#         if len(cups) >= n:  # 判断是否做够了指定的数量
#             logging.info('I finished my job. {}'.format(len(cups)))
#             break
#
# b = threading.Thread(target=boss)  # 这里把老板放在这里，监督工人是否工作
# w = threading.Thread(target=worker, args=(10,))  # 这里是工人，参数是10个杯子
# w.start()
#
# b.start()
# logging.info(len(cups))  # 打印一下杯子的数目

# import threading
# import time
# lock = threading.Lock()
#
# def work():
#     time.sleep(5)
#     lock.release()  # 测试在不同的线程间能否加锁或解锁
#
#
# lock.acquire()  # 这里是一定要拿到锁的，不然就是阻塞状态。当拿第二次锁时，就会卡在第一次不动，所以这个锁不该在主线程，放到一个子线程中会更好
# print('get locker 1')
#
# threading.Thread(target=work).start()
# # 可以用其他线程解锁
#
# time.sleep(3)
# lock.acquire()
# print('get locker 2')
#
# lock.release()  # 这是释放锁
# print('release locker')  #



#
# import logging
# import threading
#
# logging.basicConfig(level=logging.INFO)
#
# # 10 -> 100cups
#
# cups = []
#
# lock = threading.Lock()
#
# def worker(lock:threading.Lock, task=100):
#     while True:
#         lock.acquire()
#         count = len(cups)
#         # lock.release()
#         logging.info(count)
#         if count >= task:
#             lock.release()
#             break
#         # lock.acquire()
#         cups.append(1)
#         lock.release()
#         logging.info("{} make 1".format(threading.current_thread().name))
#     logging.info("{}".format(len(cups)))
#
# for x in range(10):
#     threading.Thread(target=worker, args=(lock,100)).start()
#
# # 阻塞状态锁
# # 10个线程，当第一个线程执行到78行的lock.acquire()时就拿到了锁，然后再去拿杯子数，正要拿的时候线程切换了，另一个线程可能执行到了if判断，这个锁和这个线程没有关系，因为if判断与锁没有关系，所以还是可以执行的，之后第二个线程就会执行到if判断下面的lock.acquire()，这时第二个线程就会等待第一个线程拿到的锁了，这时第三个线程如果从while True向下执行，就会卡在第一个lock.acquire()，不管lock.acquire()在哪一行，只要线程碰到这句都会停下来看一下是否阻塞，之后第一个线程执行到lock.release()后继续向下执行，到了if判断下面的lock.acquire()发现锁是开的状态，这时第一个线程又拿到了锁并锁住（第一个线程可以又拿到锁是因为CPU没有切换线程），如果第一个线程执行到if判断时CPU切换了线程，就要释放第二或第三个线程，这时第二或第三个线程就会拿到锁，谁拿到锁没法确定，因为这个锁是争抢机制。这会带来死锁问题，所有线程都会卡住，线程间都在等待别的线程释放。没人释放，互相等待，解不开的锁，就是死锁。

class Counter:
    def __init__(self):
        self.__val = 0

    def inc(self):
        self.__val += 1

    def dec(self):
        self.__val -= 1

