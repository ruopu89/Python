# import time
# import functools
# @functools.lru_cache()
# def add(x,y):
#     time.sleep(3)
#     return x + y
#
# # print(add(4,5))
# # print(add(4,y=5))
# print(add(y=4,x=5))
# print(add(x=5,y=4))
# print(add(x=5,y=4))
# ==========================================
# from functools import wraps
# import inspect
#
# def mag_cache(fn):
#     local_cache = {}
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#
#         param_names = [key for key in params.keys()]
#         params_dict = {}
#
#         for i,v in enumerate(args):
#             k = param_names[i]
#             params_dict[k] = v
#         params_dict.update(kwargs)
#
#         for k,v in params.items():
#             if k not in params_dict.keys():
#                 params_dict[k] = v.default
#         key = tuple(sorted(params_dict.items()))
#
#         ret = fn(*args, **kwargs)
#         return ret,key
#     return wrapper
#
# @mag_cache
# def add(x,z,y=6):
#     return x+y+z
#
# result = []
# result.append(add(3,4))
#
# print(add(4,5))

# print(result)
# ===============================================================
# 使用缓存
# import time
# from functools import wraps
# import inspect
#
# def mag_cache(fn):
#     local_cache = {}
#
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#
#         param_names = [key for key in params.keys()]
#         params_dict = {}
#
#         for i,v in enumerate(args):
#             k = param_names[i]
#             params_dict[k] = v
#
#         params_dict.update(kwargs)
#
#         for k,v in params.items():
#             if k not in params_dict.keys():
#                 params_dict[k] = v.default
#
#         key = tuple(sorted(params_dict.items()))
#
#         if key not in local_cache.keys():
#             local_cache[key] = fn(*args,**kwargs)
#             print('sss', local_cache)
#
#         return key,local_cache[key]
#     return wrapper
#
# @mag_cache
# def add(x,z,y=6):
#     time.sleep(3)
#     return x+y+z
#
# result = []
# result.append(add(4,5))
# result.append(add(4,z=5))
# result.append(add(4,y=6,z=5))
# result.append(add(y=6,z=5,x=4))
# result.append(add(4,5,6))
# for x in result:
#     print(x)
# =====================================================
# 增加logger装饰器查看/打印执行时间
# import time
# from functools import wraps
# import inspect
# import datetime
#
# def mag_cache(fn):
#     local_cache = {}
#
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#
#         param_names = [key for key in params.keys()]
#         params_dict = {}
#
#         for i,v in enumerate(args):
#             k = param_names[i]
#             params_dict[k] = v
#
#         params_dict.update(kwargs)
#
#         for k,v in params.items():
#             if k not in params_dict.keys():
#                 params_dict[k] = v.default
#
#         key = tuple(sorted(params_dict.items()))
#
#         if key not in local_cache.keys():
#             local_cache[key] = fn(*args,**kwargs)
#         return key,local_cache[key]
#     return wrapper
#
# def logger(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args,**kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print(fn.__name__, delta)
#         return ret
#     return wrapper
#
# @logger
# @mag_cache
# def add(x,z,y=6):
#     time.sleep(3)
#     return x + y + z
#
# result = []
# result.append(add(4,5))
# result.append(add(4,z=5))
# result.append(add(4,y=6,z=5))
# result.append(add(y=6,z=5,x=4))
# result.append(add(4,5,6))
# for x in result:
#     print(x)
# =========================================================
# 过期功能
# import time
# from functools import wraps
# import datetime
# import inspect
#
# def mag_cache(duration):
#     def _cache(fn):
#         local_cache = {}
#
#         @wraps(fn)
#         def wrapper(*args,**kwargs):
#             def clear_expire(cache):
#                 expire_keys = []
#                 for k,(_,stamp) in local_cache.items():
#                     now = datetime.datetime.now().timestamp()
#                     if now - stamp > duration:
#                         expire_keys.append(k)
#                 for k in expire_keys:
#                     local_cache.pop(k)
#
#                 clear_expire(local_cache)
#
#             def make_key():
#                 sig = inspect.signature(fn)
#                 params = sig.parameters
#
#                 param_names = [key for key in params.keys()]
#                 params_dict = {}
#
#                 for i,v in enumerate(args):
#                     k = param_names[i]
#                     params_dict[k] = v
#
#                 params_dict.update(kwargs)
#
#                 for k,v in params.items():
#                     if k not in params_dict.keys():
#                         params_dict[k] = v.default
#
#                 return tuple(sorted(params_dict.items()))
#
#             key = make_key()
#
#             if key not in local_cache.keys():
#                 local_cache[key] = (fn(*args,**kwargs),datetime.datetime.now().timestamp())
#                 print(1, local_cache)
#                 print(2, local_cache[key])
#                 print(3, local_cache.keys())
#                 print(4, local_cache.values())
#             return key,local_cache[key]
#         return wrapper
#     return _cache
#
# def logger(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print(fn.__name__, delta)
#         return ret
#     return wrapper
#
# @logger
# @mag_cache(9)
# def add(x, z, y=6):
#     time.sleep(3)
#     return x+y+z
#
#
# result = []
# result.append(add(4, 5))
# result.append(add(4, z=5))
# result.append(add(4, y=6, z=5))
# result.append(add(y=6, z=5, x=4))
# result.append(add(4, 5, 6))
# result.append(add(4, 6))
#
# for x in result:
#     print(x)
#
# time.sleep(10)
# result = []
# result.append(add(4, 5))
# result.append(add(4, z=5))
# result.append(add(4, y=6, z=5))
# result.append(add(4, 6))
# ===========================================================
# 如果使用OrderedDict，要注意，顺序要以签名声明的顺序为准。
# import time
# from functools import wraps
# import datetime
# import inspect
#
# def m_cache(duration):
#     def _cache(fn):
#         local_cache = {}
#
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             expire_keys = []
#             for k,(_,ts) in local_cache.items():
#                 print(1, ts)
#                 print(2, duration)
#                 if datetime.datetime.now().timestamp() - ts > duration:
#                     expire_keys.append(k)
#                     local_cache.pop(k)
#             for k in expire_keys:
#                 local_cache.pop(k)
#
#             key_dict = {}
#             sig = inspect.signature(fn)
#             params = sig.parameters
#
#             param_list = list(params.keys())
#
#             for i,v in enumerate(args):
#                 print(i,v)
#                 k = param_list[i]
#                 key_dict[k] = v
#
#             key_dict.update(kwargs)
#
#             for k in params.keys():
#                 if k not in key_dict.keys():
#                     key_dict[k] = params[k].default
#
#             key = tuple(sorted(key_dict.items()))
#
#             if key not in local_cache.keys():
#                 ret = fn(*args, **kwargs)
#                 local_cache[key] = (ret, datetime.datetime.now().timestamp())
#
#             return local_cache[key]
#         return wrapper
#     return _cache
#
# def logger(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args,**kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print(delta)
#         return ret
#     return wrapper
#
# @logger
# @m_cache(6)
# def add(x,y=5):
#     time.sleep(3)
#     ret = x + y
#     print(ret)
#     return ret
#
#
# print(add(4))
# print(add(4, 5))
# print(add(4, y=5))
# print(add(x=4, y=5))
# print(add(y=5, x=4))
#
# time.sleep(6)
#
# print(add(4))
# print(add(4, 5))
# print(add(4, y=5))
# print(add(x=4, y=5))
# print(add(y=5, x=4))
# ================================================
# 把上面的代码重新封装一下
from functools import wraps
import inspect
import time
import datetime

def m_cache(duration):
    def _cache(fn):
        local_cache = {}

        @wraps(fn)
        def wrapper(*args, **kwargs):
            def clear_expire(cache):
                expire_keys = []
                for k,(_,ts) in local_cache.items():
                    if datetime.datetime.now().timestamp() - ts > duration:
                        expire_keys.append(k)
                for k in expire_keys:
                    local_cache.pop(k)
            clear_expire(local_cache)

            def make_key():
                key_dict = {}
                sig = inspect.signature(fn)
                params = sig.parameters

                param_list = list(params.keys())

                for i,v in enumerate(args):
                    print(i,v)
                    k = param_list[i]
                    key_dict[k] = v

                key_dict.update(kwargs)

                for k in params.keys():
                    if k not in key_dict.keys():
                        key_dict[k] = params[k].default

                return tuple(sorted(key_dict.items()))

            key = make_key()
            print('key: {}'.format(key))

            if key not in local_cache.keys():
                ret = fn(*args, **kwargs)
                local_cache[key] = (ret, datetime.datetime.now().timestamp())
            return local_cache[key]
        return wrapper
    return _cache

def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(delta)
        return ret
    return wrapper

@logger
@m_cache(6)
def add(x,y=5):
    time.sleep(3)
    ret = x + y
    print(ret)
    return ret

print(12345, add(4))
print(add(4,5))
print(add(4,y=5))
print(add(x=4,y=5))
print(add(y=5,x=4))

time.sleep(6)

print(add(4))
print(add(4,5))
print(add(4,y=5))
print(add(x=4,y=5))
print(add(y=5,x=4))





















