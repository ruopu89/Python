# 打印一个边长为n的正方形
n = int(input("pls input nums: "))
for i in range(n):
    if i == 0 or i == n-1:
        print('*' * n)
    else:
        print('*',' ' * (n-2),'*')