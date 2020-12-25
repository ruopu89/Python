# 最简单的思路，按照定义来，假设有一个数n(n>1)，从2开始判断，一直判断到n-1
# 只能被1和自己整除的数就是素数
# n = 12577
# flag = False
# for i in range(2, n):
#     if n % i == 0:
#         flag = True
#         print(i)
#         break
# if flag:
#     print(n, 'is not a prime number. ')
# else:
#     print(n, 'is a prime number. ')
# ===================================================
# n = 1578
# for i in range(2, n):
#     if n % i == 0:
#         print(n, 'is not a prime number')
#         break
# else:
#     print(n, 'is a prime number')

n = 99991
for i in range(2, n):
    if n % i == 0:
        print("{} is not su".format(n))
        break
else:
    print("{} is su".format(n))
