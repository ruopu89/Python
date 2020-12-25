# import multiprocessing
# import datetime
#
# def calc(i):
#     sum = 0
#     for _ in range(100000000):
#         sum += 1
#     print(i, sum)
#
# if __name__ == "__main__":
#     start = datetime.datetime.now()
#
#     ps = []
#     for i in range(5):
#         p = multiprocessing.Process(target=calc, args=(i,), name="calc-{}".format(i))
#         ps.append(p)
#         p.start()
#     for p in ps:
#         p.join()
#
# delta = (datetime.datetime.now() - start).total_seconds()
# print(delta)
# print('end===')
# ========================================================
# 多进程举例
# import logging
# import datetime
# import multiprocessing
#
# logging.basicConfig(level=logging.INFO, format="%(process)d %(processName)s %(thread)d %(message)s")
#
# def calc(i):
#     sum = 0
#     for _ in range(10000):
#         sum += 1
#     logging.info('{}.in function'.format(sum))
#     return sum
#
# if __name__ == "__main__":
#     start = datetime.datetime.now()
#     pool = multiprocessing.Pool(5)
#     for i in range(5):
#         pool.apply_async(calc, args=(i,), callback=lambda x:logging.info('{}.in callback'.format(x)))
#     pool.close()
#     pool.join()
#
#     delta = (datetime.datetime.now() - start).total_seconds()
#     print(delta)
#     print('end===')
# =====================================++#
