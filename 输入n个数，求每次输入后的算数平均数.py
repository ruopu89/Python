# 输入n个数，求每次输入后的算数平均数
abc = []
sum = 0
while True:
    n = input("pls input n:")
    if n == 'q':
        print("bye!!!!")
        break
    abc.append(int(n))
    for i in abc:
        sum += i
    print("!!!!!", sum, len(abc))
    print(sum / len(abc))
