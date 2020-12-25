# 生成器指生成器对象
# def inc():
#     for i in range(5):
#         yield i
#
# print(type(inc))
# print(type(inc()))
#
# x = inc()
# print(type(x))
# print(next(x))
# for m in x:
#     print(m,'*')
# for n in x:
#     print(n,'**')
#
# y = (i for i in range(5))
# print(type(y))
# print(next(y))
# print(next(y))
# ======================================
# def gen():
#     print('line 1')
#     yield 1
#     print('line 2')
#     yield 2
#     print('line 3')
#     return 3
# next(gen())
# next(gen())
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g,'End'))
# ===========================================
# def counter():
#     i = 0
#     while True:
#         i += 1
#         yield i
#
# def inc(w):
#     return next(w)
#
# c = counter()
#
# while True:
#     s = inc(c)
#     if s == 100:
#         break
#     print(s)
# # 输出1到99, 因为在拨动同一个生成器对象
# # ============================================================
# def counter():
#     i = 0
#     while True:
#         i += 1
#         yield  i
#
# def inc():
#     c = counter()
#     return next(c)
#
# s = inc()
# print(s)
# print(s)
# # 因为生成器对象定义在了inc函数中，所以每次调用都会产生新的生成器对象，所以输出的只是1。
# # ==========================================================================
# def counter():
#     i = 0
#     while True:
#         i += 1
#         yield  i
#
# def inc():
#     c = counter()
#     return lambda :next(c)
#
# s = inc()
# print(s())
# print(s())
# # 生成器对象虽然定义在inc函数中，但因为使用了闭包，所以c变量的值被保留了下来
# # ===============================================================================
# def counter():
#     i = 0
#     while True:
#         i += 1
#         yield i
#
# def inc(c):
#     return next(c)
#
# # c = counter()
#
# while True:
#     c = counter()
#     g = inc(c)
#     print(g)
#     if g == 100:
#         break
# 20200526晚在台式机上测试，c = counter()这行放在while循环里就可以累加，放在循环外就一直显示1，为什么?是否与全局变量不可改变有关，写在里面时是局部变量，可变
# 20200527早在笔记本上测试，情况刚好相反，放在外面就可以连续输出，放在while中就只会输出1, 按照生成器的定义，这更符合生成器的定义。在台式机上测试为什么是另一种情况，原因不明。
# ======================================================================================
# def fib():
#     x = 0
#     y = 1
#     while True:
#         yield y
#         x,y = y,x+y
#
# foo = fib()  # 固定生成器对象
# for _ in range(5):
#     print('#####',next(foo))
#
# for _ in range(100):
#     print(next(foo))
# ======================================
# def fib1(n,pre=0,cur=1):
#     pre,cur = cur,pre+cur
#     print(cur, end=' ')
#     if n == 2:
#         return
#     fib1(n-1,pre,cur)
#
# print(fib1(100))
# ======================================
def counter(n):
    for x in range(n):
        yield x

def inc(n):
    for i in counter(n): # 固定从生成器函数counter返回的生成器对象
        yield i
    # yield from counter(n)

foo = inc(10)  # 固定从生成器函数inc返回的生成器对象
while True:
    print(next(foo))
    # if foo == 5:
    #     break
# print(next(foo))