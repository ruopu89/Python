# 将列表中的数字排
# 下面这是将大数往最后放，比较时第一个索引(j)是不会变的，结尾的索引每比较一轮就减一个。
# numlist = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9]]
# nums = numlist[0]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):  # 0-9
#     for j in range(length-i-1): # 0-9, 0-8, 0-7
#         count += 1
#         print(j, j+1)
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             count_swap += 1
# print(nums, count_swap, count)
# 下面准备将大数往前放，比较时结尾索引(j)是不会变的，开头索引每比较一轮就加一。该怎么做
# 下面只是从大到小排列，还没有实现结尾索引(j)是不会变的，开头索引每比较一轮就加一。是否需要使用负索引从后向前比较
# numlist = [[14,9,83,51,6,7,43,38,23],[1,2,3,4,5,6,7,8,9]]
# nums = numlist[0]
# cur = None
# length = len(nums)
# for i in range(length):
#     for j in range(length-i-1):
#         if nums[j] < nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
# print(nums)
# 如果已经是排好的，比较一轮后就可以直接出结果了
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     flag = False
#     for j in range(length-i-1):
#         count += 1
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, count, count_swap)

# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     flag = False
#     for j in range(length-i-1):
#         count += 1
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, count, count_swap)
#
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     flag = False
#     for j in range(length-i-1):
#         count += 1
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, )

# 1
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     flag = False
#     count += 1
#     for j in range(length-i-1):
#         if nums[j+1] < nums[j]:
#             nums[j+1],nums[j] = nums[j],nums[j+1]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, count_swap, count)

# 2
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# js = 0
# for i in range(length):
#     count += 1
#     flag = False
#     for j in range(length):
#         # js += 1
#         # print(nums[i], nums[j], js)
#         if nums[i] > nums[j]:
#             # print(nums[i], nums[j])
#             nums[i],nums[j] = nums[j],nums[i]
#             count_swap += 1
#             flag = True
#     if not flag:
#         break
# print(nums, count, count_swap)

# 3
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     flag = False
#     count += 1
#     for j in range(length-i-1):
#         if nums[j] < nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, count, count_swap)

# 4
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     flag = False
#     count += 1
#     for j in range(length-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, count_swap, count)

# 5
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     count += 1
#     flag = True
#     for j in range(length):
#         if nums[i]>nums[j]:
#             nums[i],nums[j] = nums[j],nums[i]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, count_swap, count)

# 5
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     count += 1
#     flag = False
#     for j in range(length-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             count_swap += 1
#             flag = True
#     if not flag:
#         break
# print(nums, count_swap, count)

# 6
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     count += 1
#     flag = False
#     for j in range(length):
#         if nums[i] > nums[j]:
#             nums[i],nums[j] = nums[j],nums[i]
#             count_swap += 1
#             flag = True
#     if not flag:
#         break
# print(nums, count_swap, count)


# 7
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     count += 1
#     flag = False
#     for j in range(length-i-1):
#         if nums[j] < nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             flag = True
#             count_swap += 1
#     if not flag:
#         break
# print(nums, count_swap, count)

# 9
# num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
# nums = num_list[2]
# print(nums)
# length = len(nums)
# count_swap = 0
# count = 0
# for i in range(length):
#     count += 1
#     flag = False
#     for j in range(length):
#         if nums[i] > nums[j]:
#             nums[i],nums[j] = nums[j],nums[i]
#             count_swap += 1
#             flag =True
#     if not flag:
#         break
# print(nums, count_swap, count)

# 10
num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1321312,232,32,1114,5231,6231,711,92,81]]
nums = num_list[2]
print(nums)
length = len(nums)
count_swap = 0
count = 0
for i in range(length):
    count += 1
    flag = False
    for j in range(length):
        if nums[i] < nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
            count_swap += 1
            flag =True
    if not flag:
        break
print(nums, count_swap, count)