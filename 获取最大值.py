# 请输入若干个整数，打印出最大值
n = int(input("pls input n: "))
abc = []
while True:
    if len(abc) == 0:
        abc.append(n)
    print(max(abc))