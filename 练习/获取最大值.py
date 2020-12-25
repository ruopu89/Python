# 请输入若干个整数，打印出最大值
# m = int(input('Input first number >>>'))
# while True:
#     c = input('Input a number >>>')
#     if c:
#         n = int(c)  # 报错由int函数抛出
#         if n > m:
#             m = n
#         print('Max is', m)
#     else:
#         break

w = []
while True:
    n = input("pls input n: ")
    if n == 'q':
        break
    else:
        n1 = int(n)
        w.append(n1)
print(w)
print(max(w))