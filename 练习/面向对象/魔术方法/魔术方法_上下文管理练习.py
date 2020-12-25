# 为加法函数计时
# 方法1，使用装饰器显示该函数的执行时长
# 方法2，使用上下文管理方法来显示该函数的执行时长
# import time
# def add(x, y):
#     time.sleep(2)
#     return x + y
#
# print(add(2, 3))
##### 装饰器实现
# import time
# import datetime
# from functools import wraps
#
# def timeit(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print('{} took {}s'.format(fn.__name__, delta))
#         return ret
#     return wrapper
#
# @timeit
# def add(x, y):
#     time.sleep(2)
#     return x + y
#
# print(add(4, 5))
##### 上下文管理
# import time
# import datetime
# from functools import wraps
#
# def add(x, y):
#     time.sleep(2)
#     return x + y
#
#
# class Timeit:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self.fn
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print("{} took {}s".format(self.fn.__name__, delta))
#
#
# with Timeit(add) as fn:
#     # print(fn(4, 6))
#     print(add(4, 7))

# class Timeit:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print("{} took {}s".format(self.fn.__name__, delta))
#
#     def __call__(self, x, y):
#         print(x, y)
#         return self.fn(x, y)
#
# with Timeit(add) as timeitobj:
#     print(timeitobj(5, 6))
# ===============================================================================================================
# 根据上面的代码，能不能把类当做装饰器用？
# import time
# import  datetime
# from functools import wraps
#
# class TimeIt:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self
#
#     def __exit__(self, *args, **kwargs):
#         self.delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('{} took {}s. context'.format(self.fn.__name__, self.delta))
#         pass
#
#     def __call__(self, *args, **kwargs):
#         self.start = datetime.datetime.now()
#         ret = self.fn(*args, **kwargs)
#         self.delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('{} took {}s. call'.format(self.fn.__name__, self.delta))
#         return ret
#
# @TimeIt
# def add(x, y):
#     """This is add function."""
#     time.sleep(2)
#     return  x + y
#
# add(4, 5)
# print(add.__doc__)
# =============================================================================================
# 使用 functools.wraps函数解决文档字符串问题
# import time
# import datetime
# from functools import wraps, update_wrapper
#
# class Timeit:
#     """This is A Class"""
#     def __init__(self, fn):
#         self.fn = fn
#         wraps(fn)(self)
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print("{} took {}s. context".format(self.fn.__name__, delta))
#
#     def __call__(self, *args, **kwargs):
#         self.start = datetime.datetime.now()
#         ret = self.fn(*args, **kwargs)
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print("{} took {}s. call".format(self.fn.__name__, delta))
#         return ret
#
# @Timeit
# def add(x, y):
#     """This is add function."""
#     time.sleep(2)
#     return x + y
#
# print(add(10, 5))
# print(add.__doc__)
#
# print(Timeit(add).__doc__)
# ====================================================================================================
# contextlib.contextmanager
import contextlib

@contextlib.contextmanager
def foo():
    print('enter')
    yield
    print('exit')

with foo() as f:
    print(f)