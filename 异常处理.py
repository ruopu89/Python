# with open('test') as f:
#     pass
# def 0a():
#     pass
# try:  # 尝试观察下面的语句，如果发现下面的某一条语句在执行的过程中产生了一个异常，就会把它抓住并交给except语句处理
#     f = open('test1', 'r')
#     print('after')
#     # 0a = 6
# except:
#     print('exception')
#
# print('outer')
# def div(x, y):
#     return x / y
#
# try:
#     div(1, 0)
# except:
#     pass
# def foo():
#     print('before')
#     def bar():
#         print(1/0)
#
#     bar()
#     print('after')
# foo()
#
# def bar():
#     print('before')
#     raise Exception('my exception')
#     print('after')
# bar()
# try:
#     1/0  # 执行到这里一定会抛异常
#     print('1/0') # 因为上面抛出了异常，所以这里不会打印
# except:
#     try:
#         raise   # 为了借用上面抛出的异常，所以这里用了raise，这不能写在try中，因为try中捕获到异常就会中断并转到except语句处理，所以写在try中也不会执行
#     except Exception as e:  # 这里是期待一个Exception异常来并给e，最后打印出来
#         print(e)
# try:
#     1/0
# except ArithmeticError:  # Exception是类，是BaseException的子类
#     print('catch U')
# import sys
#
# try:
#     sys.exit()
# except Exception:
#     print('catch U')
# import sys
# import time
#
# class MyException(Exception):
#     pass

# try:
#     raise MyException()
# except Exception:
#     print(MyException.mro())

# try:
#     # 1/0
#     # raise MyException
#     f = None
#     f = open('test1')
#
# # except MyException as e:
# #     print('~~~~~~~~~~~~~~~~~')
# #     print(e, type(e))
# # except OSError as e:
# #     print('InterruptedError')
# # except Exception as e:
# #     print(e, type(e))
# except:
#     pass
#
# finally:
#     # print('fin')
#     if f is not None:
#         f.close()
#
# print('outer')
# print(dir())
# def foo():
#     try:
#         # 1/0
#         return 123
#
#     except:
#         pass
#
#     finally:
#         return 567
#         print('fin')
#
# # print("result = " + foo())
# print("result = {}".format(foo()))
# print('outer')
# import sys
# import threading
# import time
#
# def foo1():
#     try:
#         1/0
#
#     finally:
#         print('foo1 fin')
#
# def foo2():
#     time.sleep(4)
#     try:
#         foo1()
#     finally:
#         print('foo2 fin')
#         open('abcde')
#     while True:  # 如果foo2函数中的上面的语句不出问题，就会执行这一句，执行到这一句就进入一个死循环状态，死循环状态下这个函数就不会退出，那么下面的t线程也就不会退出，t.is_alive也就一直是活着的
#         time.sleep(1)
#
# t = threading.Thread(target=foo2)  # 创建一个foo2线程
# t.start()  # 启动线程
# # 主线程一直在跑，t线程是一个分支。这段代码是为了测试当异常产生时，是结束了t线程，还是把主线程也一起结束了。当前线程是下面写的死循环
#
# while True:
#     time.sleep(1)
#     print('~~~~~~~~~~~~~~~~~~')
#     if t.is_alive():
#         print('alive')
#     else:
#         print('dead')
# 这段代码表示当前线程是一个死循环，每隔一秒查看一下t线程是否还活着。如果上面的foo2函数抛出异常，那么t线程也会结束

# 从执行的结果可以看出，对于一个异常来说，它是怎样进行传递的。它的异常是从它的产生地向外抛，如果没人管，继续向外抛，直至线程这一级，当它到了线程就是到了天花板了，如果没有代码管，当前线程就会结束，主线程不会有问题。也就是如果异常抛出后一路都没人管，会到当前线程，使当前线程中止，如果这个线程是主线程，那么主线程就会被中止，这会使到整个程序崩溃。
# 如果注释掉t线程，只用最外层的while True循环调用foo2()的话，是不会进入死循环的，会提示Process finished with exit code 1，表示当前解释器退出了
# try:
#     foo2()
# except Exception as e:
#     print("outer", e)
# finally:
#     print('outer fin')
#
# print('outer')
# import sys
# import threading
# import time
#
# def foo():
#     try:
#         1/0
#     finally:
#         print('foo1 fin')
#         return   # 这里return就会抛弃异常，直接退出了
#
# try:
#     foo()
#
# except Exception as e:  # 因为上面抛弃了异常，所以不会执行到这里
#     print('outer except', e)
# finally:
#     print('outer fin')
# print('outer')
def getaint(data):
    try:
        res = int(data)
    except Exception:
        res = 0
    return res

