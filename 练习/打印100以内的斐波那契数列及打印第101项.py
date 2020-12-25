# 费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出。首几个费波那契系数是：
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233……（OEIS中的数列A000045）
# 特别指出：0不是第一项，而是第零项。
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(1, 100):
#     c = a + b
#     if c > 100:
#         break
#     print(c)
#     a = b
#     b = c
# =================================================
a = 0
b = 1
print('{}, {}'.format(0, a))
print('{}, {}'.format(1, b))
index = 1  # 计数用，到101时终止
while True:
    c = a + b
    a = b
    b = c
    index += 1
    print('{}, {}'.format(index, c))
    if index == 101:
        break
# =======================================================
# a = 0
# b = 1
# for i in range(1, 101):
#     c = a + b
#     a = b
#     b = c
#     if i < 100:
#         continue
#     print(c)
# ==========================================================
# a = 0
# b = 1
# index = 1
# while True:
#     c = a + b
#     a,b = b,c   # 封装与解构
#     index += 1
#     if index == 101:
#         print('{}, {}'.format(index, c))
#         break
# ===========================================================
# def fibonacci():
#     a=b=1
#     yield a
#     yield b
#     while True:
#         a,b = b, a+b
#         yield b
#
# for num in fibonacci():
#     if num > 1000:
#         break
#     print(num, type(num))
# 生成器案例，使用yield实现斐波那契数列

cur = 0
pre = 1
count = [0,1]
for _ in range(101):
    d = cur + pre
    pre, cur = d, pre
    count.append(d)
    # if d >= 100:
    #     break
print(d)
print(len(count))
# 354224848179261915075