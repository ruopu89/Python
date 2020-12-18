# import functools
#
# def add(x, y) -> int:
#     return x + y
#
# newadd = functools.partial(add, y=5)
#
# print(newadd(7))
# print(newadd(7,y=6))
# print(newadd(y=10,x=6))
# =============================================
# import functools
#
# def add(x, y, *args) -> int:
#     print(args)
#     return x + y
#
# newadd = functools.partial(add, 1, 5, 4, 2)
#
# print(newadd(7))
# print(newadd(7,10))
# ==================================================
import functools
import time
@functools.lru_cache()
def add(x, y):
    time.sleep(3)
    print(x+y)
    return x + y

#
# # add(4)
# add(4,5)
# add(4.0, 5)
# add(4,6)
# add(4,6,3)
# add(6,4)
# add(4,y=6)
add(x=4,y=6)
add(y=6,x=4)
# ==========================
# import functools
#
# @functools.lru_cache()
# def fib(n):
#     if n < 3:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print([fib(x) for x in range(35)])
# # print([x for x in range(35)])
# print(fib(34))