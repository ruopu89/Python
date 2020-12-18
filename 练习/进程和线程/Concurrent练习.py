# ThreadPoolExecutor
# import threading
# from concurrent import futures
# import logging
# import time
#
# FORMAT = '%(asctime)-15s\t [%(processName)s:%(threadName)s, %(process)d:%(thread)8d] %(message)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT)
#
# def worker(n):
#     logging.info('begin to work {}'.format(n))
#     time.sleep(5)
#     logging.info('finished {}'.format(n))
#
# executor = futures.ThreadPoolExecutor(max_workers=3)
#
# fs = []
# for i in range(3):
#     future = executor.submit(worker, i)
#     fs.append(future)
#
# for i in range(3,6):
#     future = executor.submit(worker, i)
#     fs.append(future)
#
# while True:
#     time.sleep(2)
#     logging.info(threading.enumerate())
#     flag = True
#     for f in fs:
#         logging.info(f.done())
#         flag = flag and f.done()
#         if not flag:
#             break
#     print('-' * 30)
#
#     if flag:
#         exector.shutdown()
#         logging.info(threading.enumerate())
#         break
# ====================================================
# ProcessPoolExecutor对象
# import threading
# from concurrent import futures
# import logging
# import time
#
# # 输出格式定义
# FORMAT = '%(asctime)-15s\t [%(processName)s:%(threadName)s, %(process)d:%(thread)8d] %(message)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT)
#
# def worker(n):
#     logging.info('begin to work{}'.format(n))
#     time.sleep(5)
#     logging.info('finished{}'.format(n))
#
# if __name__ == '__main__':
#     executor = futures.ProcessPoolExecutor(max_workers=3)
#     fs = []
#     for i in range(3):
#         future = executor.submit(worker,i)
#         fs.append(future)
#
#     for i in range(3,6):
#         future = executor.submit(worker, i)
#         fs.append(future)
#
#     while True:
#         time.sleep(2)
#         logging.info(threading.enumerate())
#
#         flag = True
#         for f in fs:
#             logging.info(f.done())
#             flag = flag and f.done()
#             if not flag:
#                 break
#         print('-' * 30)
#
#         if flag:
#             executor.shutdown()
#             logging.info(threading.enumerate())
#             break
# =================================================
# 改造成上下文管理
# import threading
# from concurrent import futures
#
# import logging
# import time
#
# # 输出格式定义
# FORMAT = '%(asctime)-15s\t [%(processName)s:%(threadName)s, %(process)d:%(thread)8d] %(message)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT)
#
# def worker(n):
#     logging.info('begin to work {}'.format(n))
#     time.sleep(5)
#     logging.info('finished {}'.format(n))
#     return n + 100
#
# if __name__ == '__main__':
#     executor = futures.ProcessPoolExecutor(max_workers=3)
#
#     with executor:
#         fs = []
#         for i in range(3):
#             future = executor.submit(worker, i)
#             fs.append(future)
#
#         for i in range(3,6):
#             future = executor.submit(worker,i)
#             fs.append(future)
#
#         while True:
#             time.sleep(2)
#             logging.info(threading.enumerate())
#             flag = True
#             for f in fs:
#                 logging.info(f.done())
#                 flag = flag and f.done()
#                 if f.done():
#                     logging.info("result = {}".format(f.result()))
#                 if not flag:
#                     break
#             print('-' * 30)
#             if flag:
#                 break
#
#     logging.info('=====end======')
#     logging.info(threading.enumerate())
# ========================================================
# 网上找的练习：https://blog.csdn.net/qq_33961117/article/details/82587873?utm_medium=distribute.wap_relevant.none-task-blog-BlogCommendFromBaidu-2.wap_blog_relevant_pic&depth_1-utm_source=distribute.wap_relevant.none-task-blog-BlogCommendFromBaidu-2.wap_blog_relevant_pic
# 同步&异步调用方式
# from concurrent import futures
# import time, random, os
#
# def task(name):
#     print('%s %s is running' % (name, os.getpid()))
#     time.sleep(random.randint(1, 3))
#     return os.getpid()
#
# if __name__ == '__main__':
#     p = futures.ProcessPoolExecutor(4)
#     for i in range(10):
#         obj = p.submit(task, '进程id: ')
#         res = obj.result()
#         print('res: {}'.format(res))
#     p.shutdown(wait=True)
#     print('main')
# ==============================================
# 进程池的同步调用方式
# from concurrent.futures import ProcessPoolExecutor
# import time, os
# import requests
#
# def get(url):
#     print('%s GET %s' %(os.getpid(), url))
#     # time.sleep(3)
#     response = requests.get(url)
#     if response.status_code == 200:
#         res = response.text
#     else:
#         res = '下载失败'
#     return res
#
# def parse(res):
#     time.sleep(1)
#     print('%s 解析结果为 %s' % (os.getpid(), len(res)))
#
# if __name__ == '__main__':
#     urls = [
#         'https://www.baidu.com',
#         'https://www.sina.com.cn',
#         'https://www.tmall.com',
#         'https://www.jd.com',
#         'https://www.python.org',
#         'https://www.openstack.org',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#     ]
#
#     p = ProcessPoolExecutor(9)
#     l = []
#     start = time.time()
#     for url in urls:
#         future = p.submit(get, url)
#         l.append(future)
#     p.shutdown(wait=True)
#
#     for future in l:
#         parse(future.result())
#
#     print('完成时间', time.time() - start)
# ============================================
# 进程池的异步调用方式
# from concurrent.futures import ProcessPoolExecutor
# import time, os
# import requests
#
#
# def get(url):
#     print('%s GET %s' % (os.getpid(), url))
#     time.sleep(3)
#     response = requests.get(url)
#     if response.status_code == 200:
#         res = response.text
#     else:
#         res = '下载失败'
#     parse(res)
#
# def parse(res):
#     time.sleep(1)
#     print('%s 解析结果为%s' % (os.getpid(), len(res)))
#
#
# if __name__ == '__main__':
#     urls = [
#         'https://www.baidu.com',
#         'https://www.sina.com.cn',
#         'https://www.tmall.com',
#         'https://www.jd.com',
#         'https://www.python.org',
#         'https://www.openstack.org',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#
#     ]
#
#     p = ProcessPoolExecutor(9)
#     start = time.time()
#     for url in urls:
#         future = p.submit(get, url)
#     p.shutdown(wait=True)
#
#     print('完成时间', time.time() - start)
# ============================================
# 异步调用，回调函数
# from concurrent.futures import ProcessPoolExecutor
# import time, os
# import requests
#
#
# def get(url):
#     print('%s GET %s' % (os.getpid(), url))
#     time.sleep(3)
#     response = requests.get(url)
#     if response.status_code == 200:
#         res = response.text
#     else:
#         res = '下载失败'
#     return res
#
#
# def parse(future):
#     time.sleep(1)
#     # 传入的是个对象，获取返回值 需要进行result操作
#     res = future.result()
#     print('%s 解析结果为%s' % (os.getpid(), len(res)))
#
#
# if __name__ == '__main__':
#     urls = [
#         'https://www.baidu.com',
#         'https://www.sina.com.cn',
#         'https://www.tmall.com',
#         'https://www.jd.com',
#         'https://www.python.org',
#         'https://www.openstack.org',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#
#     ]
#
#     p = ProcessPoolExecutor(9)
#     start = time.time()
#     for url in urls:
#         future = p.submit(get, url)
#         # 模块内的回调函数方法，parse会使用future对象的返回值，对象返回值是执行任务的返回值
#         future.add_done_callback(parse)
#     p.shutdown(wait=True)
#
#     print('完成时间', time.time() - start)
# ============================================
# 线程池：异步+回调 ---- IO密集型主要使用方式
'''线程池:执行操作为谁有空谁执行'''
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time
import requests


def get(url):
    print('%s GET %s' % (current_thread().name, url))
    time.sleep(3)
    response = requests.get(url)
    if response.status_code == 200:
        res = response.text
    else:
        res = '下载失败'
    return res


def parse(future):
    time.sleep(1)
    res = future.result()
    print('%s 解析结果为%s' % (current_thread().name, len(res)))


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.sina.com.cn',
        'https://www.tmall.com',
        'https://www.jd.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',

    ]
    # 线程池内线程数
    p = ThreadPoolExecutor(4)
    start = time.time()
    for url in urls:
        future = p.submit(get, url)
        future.add_done_callback(parse)

    p.shutdown(wait=True)

    print('主', current_thread().name)
    print('完成时间', time.time() - start)