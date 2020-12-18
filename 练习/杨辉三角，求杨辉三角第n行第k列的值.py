# 算法1
# 计算到m行，打印出k项
# 求m行k个元素
# m行元素有m个，所以k不能大于m
# 这个需求需要保存m行的数据，那么可以使用一个嵌套机构[[],[],[]]
m = 9
k = 5
a = []
lun = 0
for i in range(m):
    row = [1]
    a.append(row)
    if i == 0:
        continue
    for j in range(1,i):
        row.append(a[i-1][j]+a[i-1][j-1])
        print("第{}次循环".format(lun), j, row)
        lun += 1
    row.append(1)
print(a)
print(a[m-1][k-1])

# 算法2
# 根据杨辉三角的定理：第n行的m个数(m>0且n>0)可表示为C(n-1,m-1)，即为从n-1个不同元素中取m-1个元素的组合数
# 组合数公式：有m个不同元素，任意取n(n<=m)个元素，记作c(m,n)，组合数公式为：
# C(m,n) = m!/(n!(m-n)!)
# m行k列的值，c(m-1,k-1)组合数
m = 9
k = 5
n = m - 1
r = k - 1
d = n - r
tragets = []
factorial = 1
for i in range(1, n+1):
    factorial *= i
    if i == r:
        tragets.append(factorial)
    if i == d:
        tragets.append(factorial)
    if i == n:
        tragets.append(factorial)
print(tragets)
print(tragets[2]//(tragets[0]*tragets[1]))
