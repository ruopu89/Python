########### 容器相关方法 #############
# class A(dict):
#     def __missing__(self, key):
#         print('Missing key :', key)
#
# a = A()
# print(a['k'])

########### 可调用对象 #############
# def foo():
#     print(foo.__module__, foo.__name__)
#
# foo()
# foo.__call__()

# 例1：
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, *args, **kwargs):
#         return "<Point {}:{}>".format(self.x, self.y)
#
# p = Point(4, 5)
# print(p)
# print(p())

# 例2：
# class Adder:
#     def __call__(self, *args, **kwargs):
#         ret = 0
#         for x in args:
#             ret += x
#         self.ret = ret
#         return ret
#
# adder = Adder()
# print(adder(4, 5, 6))
# print(adder.ret)

############### 上下文管理 ###################
# with open('test') as f:
#     pass

# class Point:
#     pass
#
# with Point() as p:  #  提示属性错误，没有`__exit__`，看来需要这个属性
#     pass

# *** 当一个对象同时实现了`__enter__()`和`__exit__()`方法，它就属于上下文管理的对象 ***
# __enter__ 进入与此对象相关的上下文。如果存在该方法，with语法会把该方法的返回值作为绑定到as子句中指定的变量上
# __exit__ 退出与此对象相关的上下文
# class Point:
#     def __init__(self):
#         print('init')
#     def __enter__(self):
#         print('enter')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
# with Point() as f:
#     print('do sth.')
#################### 上下文管理的安全性 ###################
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
#     raise Exception('error')
#     print('do sth.')

#### 极端的例子
# import sys
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

############# with 语句 ################
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
# p = Point()
# with p as f:
#     print(p == f)
#     print('do sth.')
# 上面p与f不相等的原因在__enter__方法上，它将自己的返回值赋给f。修改如下
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

# class Point:
#     def __init__(self):
#         print('init')
#
#     def __enter__(self):
#         print('enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         print('exit')
#         return  "abc"
#
# p = Point()
# with p as f:
#     raise Exception('New Error')
#     print('do sth.')
#
# print('outer')
# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __sub__(self, other):
#         self.x = self.x - other.x
#         return self
#
#     def __str__(self):
#         return str(self.x)
#
#     __repr__ = __str__
#
# p = A(9)
# p1 = A(4)
# print(p, p1)
# print(p - p1)

def logger(fn):
    def wrapper(*args,**kwargs):
        print('begin')
        x = str(fn(*args,**kwargs))

        print('end')
        return x
    return wrapper

@logger  # 等价于add = logger(add)
def add(x,y):
    # print(1, add.__dict__, dir(add))
    print(2, type(add))
    return x + y

print(add(45,40), type(add(1,2)))
# print(2, add.__dict__, dir(add))