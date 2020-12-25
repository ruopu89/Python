# 用户输入一个数字
# 1.判断是几位数
# 2.打印每一位数字及其重复的次数
# 3.依次打印每一位数字，顺序个、十、百、千、万...位
# m = input(">>>").strip().lstrip('0')
# print("这是{}位数".format(len(m)))
# for i in range(len(m)):
#     print("{}'s count = {}".format(m[i], m.count(m[i])))
#
# for j in range(len(m)):
#     n = m[-j-1]
#     print(n)
# print(m)

# num = ''
# while True:
#     num = input('Input a positive num >>>').strip().lstrip('0')
#     if num.isdigit():
#         break
# print("The length of {} is {}".format(num, len(num)))
#
# for i in range(len(num), 0, -1):
#     print(num[i-1], end=' ')
# print()
#
# for i in reversed(num):
#     print(i, end=' ')
# print()
#
# for i in range(len(num)):
#     print(num[-i-1], end=' ')
# print()
#
# counter = [0] * 10
# for i in range(10):
#     print(1, type(num))
#     counter[i] = num.count(str(i))
#     if counter[i]:
#         print("The count of {} is {}".format(i, counter[i]))
#
# print('~'*20)

# counter = [0]*10
# for x in num:
#     i = int(x)
#     if counter[i] == 0:
#         counter[i] = num.count(x)
#         print("The count of {} is {}".format(x, counter[i]))
# nums = []
# while len(nums) < 5:
#     num = input("Please input a num: ".strip().lstrip('0'))
#     if not num.isdigit():
#         continue
#     print('the length of {} is {}'.format(num, len(num)))
#     nums.append(int(num))
# print(nums)
# lst = nums.copy()
# lst.sort()
# print(lst)

