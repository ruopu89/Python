# n = 5
# print('*' * n)
# for i in ('*' * (n-2)):
#     print('*' + ' ' * (n-2) + '*')
# print('*' * n)
# ==========================================================
# n = 6
# e = -n//2
# for i in range(e, n+e):  # -3, 3
#     if i == e or i == n+e-1:  # -3 == 3 or 2 == 2
#         print('*' * n)
#     else:
#         print('*' + ' '*(n-2) + '*')
# ==========================================================
# n = 5
# for i in range(5):
#     if i == 0 or i == n-1:
#         print('*'*n)
#     else:
#         print('*' + ' '*(n-2) + '*' )  # 字符串相加，不要用逗号分隔打印的内容

n = input("pls input n: ")
n1 = int(n)
for i in range(n1):
    if i == 0 or i == n1-1:
        print("* " * (n1-1)+"*")
    else:
        print("* "+"  "*(n1-2)+"*")