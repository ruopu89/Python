# def add1(x,y):
#     return x + y
#
# def add2(x,y,z):
#     return x+y+z
#
# def add3(x,y,*args,z):
#     return x+y+z
#
# def logger(fn,*args,**kwargs):
#     print('before')
#     ret = fn(*args,**kwargs)
#     print('after')
#     return ret
#
# print(logger(add2,4,y=5,z=6))
# print(logger(add3, 4,z=5,y=6))
# =============================================
# def copy_properties(src):
#     def _copy(dst):
#         dst.__name__ = src.__name__
#         dst.__doc__ = src.__doc__
#         dst.__qualname__ = src.__qualname__
#         return dst
#     return _copy
#
# def logger(fn):
#     # @copy_properties(fn)
#     def wrapper(*args,**kwargs):
#         '''this is a wrapper'''
#         print('before')
#         ret = fn(*args, **kwargs)
#         print('after')
#         return ret
#     return wrapper
#
# @logger
# def add(x,y):
#     '''this is a function'''
#     ret = x+y
#     return ret
#
# # s = add(4,100)
# # print(s)
# print(add.__name__,add.__doc__,add.__qualname__,sep='\n')
# print("name={},doc={}".format(add.__name__,add.__doc__))
# =============================================================
# import datetime
# import time
#
# def copy_properties(src):
#     def _copy(dst):
#         dst.__name__ = src.__name__
#         dst.__doc__ = src.__doc__
#         dst.__qualname__ = src.__qualname__
#         return dst
#     return _copy
#
# def logger(duration):
#     def _logger(fn):
#         @copy_properties(fn)
#         def wrapper(*args,**kwargs):
#             start = datetime.datetime.now()
#             ret = fn(*args,**kwargs)
#             delta = (datetime.datetime.now()-start).total_seconds()
#             print('so slow') if delta > duration else print('so fast')
#             return ret
#         return wrapper
#     return _logger
#
# @logger(1)
# def add(x,y):
#     time.sleep(3)
#     return x+y
#
# print(add(4,5))
# ========================================================
# import datetime
# import time
#
# def copy_properties(src):
#     def _copy(dst):
#         dst.__name__ = src.__name__
#         dst.__doc__ = src.__doc__
#         dst.__qualname__ = src.__qualname__
#         return dst
#     return _copy
#
# def logger(duration,func=lambda name,duration:print('{} to ok {}s'.format(name,duration))):
#     def _logger(fn):
#         @copy_properties(fn)
#         def wrapper(*args,**kwargs):
#             start = datetime.datetime.now()
#             ret = fn(*args,**kwargs)
#             delta = (datetime.datetime.now()-start).total_seconds()
#             if delta > duration:
#                 func(fn.__name__,delta)
#             return ret
#         return wrapper
#     return _logger
#
# @logger(3)
# def add(x,y):
#     time.sleep(3)
#     return x+y
#
# print(add(5,6))
# ================================================================
# import datetime
# import time
#
# def logger(t):
#     def _logger(fn):
#         def wrap(*args,**kwargs):
#             start = datetime.datetime.now()
#             ret = fn(*args,**kwargs)
#             duration = (datetime.datetime.now()-start).total_seconds()
#             if duration > t:
#                 print('function {} to ok {}s'.format(fn.__name__,duration))
#             return ret
#         return wrap
#     return _logger
#
# @logger(3)
# def add(x,y):
#     print('===========call add==============')
#     time.sleep(5)
#     return x+y
#
# print(add(5,6))
# ====================================================
# import datetime
# import time
#
# def logger(t1,t2):
#     def _logger(fn):
#         def wrap(*args,**kwargs):
#             start = datetime.datetime.now()
#             ret = fn(*args,**kwargs)
#             duration = (datetime.datetime.now()-start).total_seconds()
#             if duration > t1 and duration < t2:
#                 print('function {} to ok {}s'.format(fn.__name__,duration))
#             return ret
#         return wrap
#     return _logger
#
# @logger(3,5)
# def add(x,y):
#     print('============call add================')
#     time.sleep(3)
#     return x+y
#
# print(add(5,6))
# --------------------------------------------------------
# import datetime,time,functools
#
# def logger(duration,func=lambda name,duration:print('{} to ok {}s.'.format(name,duration))):
#     def _logger(fn):
#         def wrapper(*args,**kwargs):
#             start = datetime.datetime.now()
#             ret = fn(*args,**kwargs)
#             delta = (datetime.datetime.now()-start).total_seconds()
#             if delta>duration:
#                 func(fn.__name__,duration)
#             return ret
#         return functools.update_wrapper(wrapper,fn)
#     return _logger
#
# @logger(5)
# def add(x,y):
#     time.sleep(1)
#     return x+y
#
# print(add(5,6),add.__name__,add.__wrapped__,add.__dict__,sep='\n')
# ==================================================
import datetime,time,functools

def logger(duration,func=lambda name,duration:print('{} to ok {}s.'.format(name,duration))):
    def _logger(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            delta = (datetime.datetime.now()-start).total_seconds()
            if delta>duration:
                func(fn.__name__,duration)
            return ret
        return wrapper
    return _logger

@logger(5)
def add(x,y):
    time.sleep(1)
    return x+y

print(add(5,6),add.__name__,'~~~~~~~~~~~~',add.__wrapped__,add.__dict__,sep='\n')