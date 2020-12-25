# 编写一个函数，接受一个参数n，n为正整数，左右两种打印方式。要求数字必须对齐
# 上三角
# def show(n):
#     tail = " ".join([str(i) for i in range(n, 0, -1)])
#     width = len(tail)
#     for i in range(1, n):
#         print("{:>{}}".format(" ".join([str(j) for j in range(i,0,-1)]), width))
#     print(tail)
# show(12)

# 下三角
# def showtail(n):
#     tail = " ".join([str(i) for i in range(n,0,-1)])
#     print(tail)
#     for i in range(len(tail)):
#         if tail[i] == ' ':
#             print(' '*i, tail[i+1:])
# showtail(12)
#
# def showtail1(n):
#     tail1 = ' '.join(str(i) for i in range(n,0,-1))
#     width1 = len(tail1)
#     for i in range(n,0,-1):
#         print("{:>{}}".format(" ".join(str(j) for j in range(i,0,-1)), width1))
# showtail1(11)

tail = "*".join([str(i) for i in range(12, 0, -1)])
for v,i in enumerate(tail):
    print(v,i)

print(tail)