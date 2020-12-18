# 列表-依次接收用户输入的3个数，排序后打印
# nums = []
# count = 0
# while True:
#     x = int(input("pls input nums: "))
#     nums.append(x)
#     count += 1
#     if count >= 3:
#         break
# if nums[0] > nums[1]:
#     if nums[0] > nums[2]:
#         i1 = nums[0]
#         if nums[1] > nums[2]:
#             i2 = nums[1]
#             i3 = nums[2]
#         else:
#             i2 = nums[2]
#             i3 = nums[1]
# elif nums[1] > nums[0]:
#     if nums[1] > nums[2]:
#         i1 = nums[1]
#         if nums[0] > nums[2]:
#             i2 = nums[0]
#             i3 = nums[2]
#         else:
#             i2 = nums[2]
#             i3 = nums[0]
# elif nums[2] > nums[0]:
#     if nums[2] > nums[1]:
#         i1 = nums[2]
#         if nums[0] > nums[1]:
#             i2 = nums[0]
#             i3 = nums[1]
#         else:
#             i2 = nums[1]
#             i3 = nums[0]
# print(i1, i2, i3)

# nums = []
# out = None
# for i in range(3):
#     nums.append(int(input("pls input nums{}: ".format(i+1))))
#
# while True:
#     cur = min(nums)
#     print(cur)
#     nums.remove(cur)
#     if len(nums) == 1:
#         print(nums[0])
#         break
# nums = []
# for i in range(3):
#     nums.append(int(input("pls input num{}: ".format('s'))))
#
# nums.sort()
# print(nums)

w = []
for _ in range(3):
    n = input("pls input n: ")
    if n == 'q':
        break
    else:
        n1 = int(n)
        w.append(n)
# print(sorted(w))
w.sort()
print(w)