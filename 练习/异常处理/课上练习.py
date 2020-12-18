# with open('testabc') as f:
#     pass
# 异常
# Traceback (most recent call last):
#   File "/home/shouyu/PycharmProjects/test/练习/异常处理/课上练习.py", line 1, in <module>
#     with open('testabc') as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'testabc'

# def 0A():
#     pass
# 错误
# File "/home/shouyu/PycharmProjects/test/练习/异常处理/课上练习.py", line 9
#     def 0A():
#         ^
# SyntaxError: invalid syntax

# def foo():
#     print('before')
#     def bar():
#         print(1/0)
#     bar()
#     print('after')
# foo()

# def bar():
#     print('before')
#     raise TypeError()
#     print('after')
# bar()
# ============================================
# 异常的捕获
# try:
#     print('begin')
#     c = 1/0
#     print('end')
# except:
#     print('catch the exception')
# print('outer')
# ========================================
# 捕获指定类型的异常
# try:
#     print('begin')
#     c = 1/0
#     print('end')
# except ArithmeticError:
#     print('catch the ArithmeticError')
# print('outer')
# ===========================================
# SystemExit
# import sys
# print('before')
# sys.exit(1)
# print('SysExit')
# print('outer')
#
# import sys
# try:
#     sys.exit(1)
# except SystemExit:
#     print('SysExit')
# print('outer')
# =======================================
# KeyboardIterrupt
# try:
#     import time
#     while True:
#         time.sleep(0.5)
#         print('aaa')
# except KeyboardInterrupt:
#     print('ctrl + c')
# print('outer')
# ======================================
# SyntaxError
# def a():
#     try:
#         0a = 5
#     except:
#         pass
# =====================================
# class MyException(Exception):
#     pass
#
# try:
#     raise MyException()
# except MyException:
#     print('catch the exception')
# ==========================================
# 异常的捕获
# class MyException(Exception):
#     pass
#
# try:
#     # a = 1/0
#     # raise MyException()
#     open('a1.txt')
# except MyException:
#     print('catch the MyException')
# except ZeroDivisionError:
#     print('1/0')
# except Exception:
#     print('Exception')
# ==============================================
# as子句
# class MyException(Exception):
#     def __init__(self, code, message):
#         self.code = code
#         self.message = message
#
# try:
#     raise MyException(200,'ok')
# except MyException as e:
#     print('Myexception = {} {}'.format(e.code, e.message))
# except Exception as e:
#     print('Exception = {}'.format(e))
# ================================================================
# finally 子句
# try:
#     # f = open('/home/shouyu/PycharmProjects/test/练习/异常处理.py')
#     f = open('test.txt')
# except FileExistsError as e:
#     print('{} {} {}'.format(e.__class__, e.errno, e.strerror))
# finally:
#     print('清理工作')
#     f.close()
#
# f = None
# try:
#     f = open('/home/shouyu/PycharmProjects/test/练习/异常处理/课上练习.py')
# except Exception as e:
#     print('{}'.format(e))
# finally:
#     print('清理工作')
#     if f:
#         f.close()
#
# try:
#     f = open('test.txt')
# except Exception as e:
#     print('{}'.format(e))
# finally:
#     print('清理工作')
#     try:
#         f.close()
#     except NameError as e:
#         print(e)
#
# def foo():
#     try:
#         return 3
#     finally:
#         print('finally')
#     print('==')
# print(foo())
#
# def foo():
#     # return 1
#     try:
#         return 3
#     finally:
#         return 5
#     print('==')
# print(foo())
# ==============================================
# 异常的传递
# def foo1():
#     return 1/0
#
# def foo2():
#     print('foo2 start')
#     foo1()
#     print('foo2 stop')
# foo2()
#
# import threading
# import time
#
# def foo1():
#     return 1/0
#
# def foo2():
#     time.sleep(3)
#     print('foo2 start')
#     foo1()
#     print('foo2 stop')
#
# t = threading.Thread(target=foo2)
# t.start()
#
# while True:
#     time.sleep(1)
#     print('Everything ok')
#     if t.is_alive():
#         print('alive')
#     else:
#         print('dead')
# =================================================
# try 嵌套
# try:
#     try:
#         ret = 1/0
#     except KeyError as e:
#         print(e)
#     else:
#         print('inner ok')
#     finally:
#         print('inner fin')
# except:
#     print('outer catch')
# finally:
#     print('outer fin')
#
# def foo():
#     try:
#         ret = 1/0
#     except KeyError as e:
#         print(e)
#     finally:
#         print('inner fin')
#         return
#
# try:
#     foo()
# except:
#     print('outer catch')
# finally:
#     print('outer fin')
# ==========================================
# 立即捕获
# def parse_int(s):
#     try:
#         return int(s)
#     except:
#         return 0
# print(parse_int('s'))
# ==========================================
# else 子句
try:
    ret = 1 * 0
except ArithmeticError as e:
    print(e)
else:
    print('ok')
finally:
    print('fin')