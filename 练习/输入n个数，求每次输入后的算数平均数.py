# n = 0
# sum = 0
# while True:
#     i = input('>>>')
#     if i == 'quit':
#         break
#     n += 1
#     sum += int(i)
#     avg = sum/n
#     print(avg+ 'count: ', n)  # 这里要用逗号分隔，不能用加号，因为变量的类型不是字符串


sum = 0
count = 0
while True:
    n = input("pls input n: ")
    if n == 'q':
        break
    else:
        count += 1
        n1 = int(n)
        sum += n1
        print(sum / count)





