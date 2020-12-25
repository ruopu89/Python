# 最简单的思路，按照定义来，假设有一个数n(n>1)，从2开始判断，一直判断到n-1

n = int(input("pls input n: "))
for i in (2, n+1):
    if n % i == 0:
        print("{} is not ss".format(n))
        break
    else:
        print("{} is ss".format(n), "!!!!!!")


