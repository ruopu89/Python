# 随机产生10个数字
# 要求：
# 每个数字取值范围[1,20]
# 统计重复的数字有几个？分别是什么？
# 统计不重复的数字有几个？分别是什么？
# 举例：11,7,5,11,6,7,4，其中2个数字7和11重复了，3个数字4,5,6没有重复过
# 思路：

# import random
# nums = []
# for _ in range(10):
#     nums.append(random.randrange(5))
#
# print("Origin numbers = {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
#
# for i in range(length):
#     flag = False
#     if states[i] == 1:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             flag = True
#             # print("flag {}".format(flag))
#             states[j] = 1
#             # print(states)
#     if flag:
#         samenums.append(nums[i])
#         # print("samenums: {}".format(samenums))
#         states[i] = 1
#     else:
#         diffnums.append(nums[i])
#         print("diffnums: {}".format(diffnums))
#
# print("Same numbers = {1},Counter = {0}".format(len(samenums),samenums))
# print("Different numbers = {1},Counter = {0}".format(len(diffnums),diffnums))
# print(list(zip(states,nums)))
# for w in samenums:
#     print(w, "count {}".format(nums.count(w)))

# 1
# import  random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(21))
#
# print("Origin num = {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
# for i in range(length):
#     flag = False
#     if states[i] == 1:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             flag = True
#             states[j] = 1
#     if flag:
#         samenums.append(nums[i])
#         states[i] = 1
#     else:
#         diffnums.append(nums[i])
#
# print("Same nums = {}, counter = {}".format(samenums, len(samenums)))
# print("Diff nums = {}, counter = {}".format(diffnums, len(diffnums)))
# for w in samenums:
#     print(w, "count {}".format(nums.count(w)))
#
# import random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(21))
#
# print("Origin nums = {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
# # print(states, type(states))
# for i in range(length):
#     flag = False
#     if states[i] == i:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             flag = True
#             states[j] = 1
#     if flag:
#         samenums.append(nums[i])
#         states[i] = 1
#     else:
#         diffnums.append(nums[i])
#
# print("Same nums = {}, count = {}".format(samenums, len(samenums)))
# print("Diff nums = {}, count = {}".format(diffnums, len(diffnums)))
# print(list(zip(states, nums)))
# for w in samenums:
#     print(w, "count {}".format(nums.count(w)))

# 1
# import random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(20))
#
# print("Origin nums = {}".format(nums))
# print()
#
# length = len(nums)
# samesums = []
# diffnums = []
# states = [0] * length
# for i in range(length):
#     flag = False
#     if states[i] == 1:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             flag = True
#             states[j] = 1
#     if flag:
#         samesums.append(nums[i])
#         states[i] = 1
#     else:
#         diffnums.append(nums[i])
#
# print("Same nums = {}, count = {}".format(samesums, len(samesums)))
# print("Diff nums = {}, count = {}".format(diffnums, len(diffnums)))
# print(list(zip(states, nums)))
# for w in samesums:
#     print(w, "count = {}".format(nums.count(w)))

# 2
# import  random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(21))
#
# print("origin nums = {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
#
# for i in range(length):
#     flag = False
#     if states[i] == 1:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             flag = True
#             states[j] = 1
#     if flag:
#         samenums.append(nums[i])
#         states[i] = 1
#     else:
#         diffnums.append(nums[i])
#
# print("same nums = {}, count = {}".format(samenums, len(samenums)))
# print("diff nums = {}, count = {}".format(diffnums, len(diffnums)))
# print(list(zip(states, nums)))
# for w in samenums:
#     print(w, "count: {}".format(nums.count(w)))

# 3
# import random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(21))
#
# print("origin nums {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
# for i in range(length):
#     flag = False
#     if states[i] == 1:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             states[j] = 1
#             flag = True
#     if flag:
#         samenums.append(nums[i])
#     else:
#         diffnums.append(nums[i])
#
# print("same nums {}, count {}".format(samenums, len(samenums)))
# print("diff nums {}, count {}".format(diffnums, len(diffnums)))
# print(list(zip(states, nums)))
# for w in samenums:
#     print(w, "count {}".format(nums.count(w)))

# 4
# import random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(21))
#
# print("origin nums {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
# for i in range(length):
#     flag = False
#     if states[i] == 1:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             states[j] = 1
#             flag = True
#     if flag:
#         samenums.append(nums[i])
#         states[i] = 1
#     else:
#         diffnums.append(nums[i])
#
# print("same nums {}, count {}".format(samenums, len(samenums)))
# print("diff nums {}, count {}".format(diffnums, len(diffnums)))
# print(list(zip(states, nums)))
# for w in samenums:
#     print(w, "count {}".format(nums.count(w)))

# 5
# import random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(21))
#
# print("origin nums {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
# for i in range(length):
#     flag = False
#     if states[i] == 1:
#         continue
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             states[j] = 1
#             flag = True
#     if flag:
#         samenums.append(nums[i])
#     else:
#         diffnums.append(nums[i])
# print("same nums {}, count {}".format(samenums, len(samenums)))
# print("diff nums {}, count {}".format(diffnums, len(diffnums)))
# print(list(zip(states, nums)))
# for w in samenums:
#     print(w, "count {}".format(nums.count(w)))

# 6
# import random
# nums = []
# for _ in range(20):
#     nums.append(random.randrange(21))
# print("origin nums {}".format(nums))
# print()
#
# length = len(nums)
# samenums = []
# diffnums = []
# states = [0] * length
# for i in range(length):
#     if states[i] == 1:
#         continue
#     flag = False
#     for j in range(i+1, length):
#         if states[j] == 1:
#             continue
#         if nums[i] == nums[j]:
#             flag = True
#             states[j] = 1
#     if flag:
#         samenums.append(nums[i])
#         states[i] = 1
#     else:
#         diffnums.append(nums[i])
# print("same nums {}, count {}".format(samenums, len(samenums)))
# print("diff nums {}, count {}".format(diffnums, len(diffnums)))
# print(list(zip(states, nums)))
# for w in samenums:
#     print(w, "count {}".format(nums.count(w)))