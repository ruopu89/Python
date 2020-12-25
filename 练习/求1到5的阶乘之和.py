# n = 5
# sum = 0
# for i in range(1, n+1):  # 1 - 5
#     tmp = 1
#     for j in range(1, i+1):  # 1 - 2, 1 - 3, 1 - 4, 1 - 5
#         tmp *= j # 1*2, 1*2*3, 1*2*3*4, 1*2*3*4*5
#     sum += tmp
# print(sum)
# # =============================================================
# nums = 1
# sum = 0
# for n in range(1,6):
#     nums *= n  # 1*1, 1*1*2, 1*1*2*3
#     sum += nums
# print(sum)

n = int(input("pls input n: "))
sum = 0
factorial = 1
for i in range(1, n+1):
    factorial *= i
    # print("factorial: {}".format(factorial))
    sum += factorial
    # print("sum: {}".format(sum))
print(sum)