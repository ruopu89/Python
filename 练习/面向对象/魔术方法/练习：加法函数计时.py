# import time
#
# def add(x, y):
#     time.sleep(2)
#     return x+y
#
# print(add(2,3))
# =============================
# 装饰器实现
# import time
# import datetime
# from functools import wraps
#
# def timeit(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.datetime.now()-start).total_seconds()
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
# ===================================================================
# 上下文实现
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
# # @timeit
# def add(x,y):
#     time.sleep(2)
#     return x + y
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
# with Timeit(add) as fn:
#     print(fn(4, 7))
# =================================================================
# 另一种实现，使用可调用对象实现
# import time
# import datetime
# from functools import wraps

# def timeit(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.datetime.now()-start).total_seconds()
#         print('{} took {}s'.format(fn.__name__, delta))
#         return ret
#     return wrapper

# def add(x,y):
#     time.sleep(2)
#     return x + y
#
# class Timeit:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __enter__(self):
#         # print(self.__dict__)
#         self.start = datetime.datetime.now()
#         # print(self.__dict__,self)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now()-self.start).total_seconds()
#         print("{} took {}s".format(self.fn.__name__, delta))
#
#     def __call__(self, x, y):
#         # print(self.fn(x,y))
#         return self.fn(x, y)
#
# with Timeit(add) as timeitobj:
#     print(timeitobj.__dict__)
# abc = Timeit(add)
# print(abc.__dict__)
# =============================================================================
# 根据上面的代码，能不能把类当做装饰器用？
# import time
# import datetime
# from functools import wraps, update_wrapper
#
# class TimeIt:
#     def __init__(self, fn):
#         self.fn = fn
#         # self.__doc__ = fn.__doc__  # 这是第一种保存被装饰函数的说明文档的方法
#         # update_wrapper(self, fn)  # 这是第二种保存被装饰函数的说明文档的方法
#         wraps(fn)(self)
#
#     def __enter__(self):
#         print('enter')
#         self.start = datetime.datetime.now()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('{} took {}s. context'.format(self.fn.__name__, self.delta))
#
#     def __call__(self, *args, **kwargs):
#         self.start = datetime.datetime.now()
#         ret = self.fn(*args, **kwargs)
#         self.delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('{} took {}s. call'.format(self.fn.__name__, self.delta))
#         # print(self.__dict__)
#         return ret
#
#
# @TimeIt
# def add(x, y):
#     """This is a add function."""
#     time.sleep(2)
#     return x + y
#
# add(4,5)
# # with TimeIt(add) as timeitobj:
# #     print(timeitobj(5,6))
# print(add.__doc__)
# # 没有保存下来add函数中的说明文档
# =====================================================================================
# 让函数在上下文管理之间执行
# import time
# import datetime
#
# class TimeIt:
#     def __enter__(self):
#         print('enter')
#         self.start = datetime.datetime.now()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print(1, delta)
#         return
#
# def add(x, y):
#     time.sleep(2)
#     return x + y
#
# with TimeIt() as f:
#     add(5, 6)
# ===========================================================================
import time
import datetime
from functools import wraps

class TimeIt:
    def __init__(self, fn):
        self._fn = fn
        wraps(fn)(self)

    def __enter__(self):
        print('enter')
        self.start = datetime.datetime.now()
        return self._fn

    def __call__(self, *args, **kwargs):
        print('__call__')
        start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("dec {} took {}".format(self._fn.__name__, delta))
        return ret

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print("context {} took {}".format(self._fn.__name__, delta))
        return

@TimeIt  # add = TimeIt()
def add(x, y):
    time.sleep(2)
    # print(x + y)
    return x + y

# print(add(10, 11))
# print(add.__doc__)
# print(add.__name__)
# print(type(add))

# with TimeIt(add) as f:
#     # add(5, 6)

with TimeIt(add) as foo:
    foo(5, 6)