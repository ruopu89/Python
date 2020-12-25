# class Point:
#     def __init__(self):
#         print('init')
#
#     def __enter__(self):
#         print('enter')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
# with Point() as f:
#     print('do sth')
# ===========================================================
# class Point:
#     def __init__(self):
#         print('init')
#
#     def __enter__(self):
#         print('enter')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
# with Point() as f:
#     # raise Exception('error')
#     print('do sth.')
# ============================================================
# 极端的例子
# import sys
#
# class Point:
#     def __init__(self):
#         print('init')
#
#     def __enter__(self):
#         print('enter')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
# with Point() as f:
#     sys.exit(-100)
#     print('do sth.')
#
# print('outer')
# ================================================
# with 语句
# class Point:
#     def __init__(self):
#         print('init')
#
#     def __enter__(self):
#         print('enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
# p = Point()
# with p as f:
#     print(p == f)
#     print('do sth.')
# ======================================================
# __enter__方法和__exit__方法的参数
# class Point:
#     def __init__(self):
#         print('init')
#
#     def __enter__(self):
#         print('enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(1, exc_type)
#         print(2, exc_val)
#         print(3, exc_tb)
#         print('exit')
#         return "abc"
#
# p = Point()
# with p as f:
#     # raise Exception('New Error')
#     print('do sth.')
#     print(1111, f)
#
# print('outer')
# ============================================================
# contextlib.contextmanager
# import contextlib
#
# @contextlib.contextmanager
# def foo():
#     print('enter')
#     try:
#         yield 5
#     finally:
#         print('exit')
#
# with foo() as f:
#     raise Exception()
#     print(f)
# ============================================================
# import contextlib
# import datetime
# import time
#
# @contextlib.contextmanager
# def add(x,y):
#     start = datetime.datetime.now()
#     try:
#         yield x + y
#     finally:
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print(delta)
#
# with add(4,5) as f:
#     raise Exception()
#     time.sleep(2)
#     print(f)
# ==============================================================
class Point:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter' + self.__class__.__name__)
        # return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit' + self.__class__.__name__)
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return 1

p = Point()
import sys

with p as f:
    # sys.exit()
    print(1, f == p)
    print(f is p)
    print(p)
    print(f)

print('outer')