# 用户输入一个数字
# - 打印每一位数字及其重复的次数

# num = input('>>>')
# d = {}
# for c in num:
#     if not d.get(c):
#         d[c] = 1
#         continue
#     d[c] += 1
# print(d)

# d = {}
# for c in num:
#     if c not in d.keys():
#         d[c] = 1
#     else:
#         d[c] += 1
# print(d)

# 数字重复统计
#
# - 随机产生100个整数
# - 数字的范围[-1000,1000]
# - 升序输出所有不同的数字及其重复的次数
# import random
#
# n = 100
# nums = [0] * n
# for i in range(n):
#     nums[i] = random.randint(-1000,1000)
# print(nums)
# t = nums.copy()
# t.sort()
# print(t)
#
# d = {}
# for x in nums:
#     if x not in d.keys():
#         d[x] = 1
#     else:
#         d[x] += 1
# print(d)
# d1 = sorted(d.items())
# print(d1)

# 字符串重复统计
#
# - 字符表'abcdefghijklmnopqrstuvwxyz'
# - 随机挑选2个字母组成字符串，共挑选100个
# - 降序输出所有不同的字符串及重复的次数

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

words = []
for _ in range(100):
    words.append(''.join(random.choice(alphabet) for _ in range(2)))
# print(words)

d = {}
for x in words:
    # print("x: {}".format(x))
    d[x] = d.get(x,0) + 1
# 这个方法比之前的if not d.get(c)和if c not in d.keys更加方便
print(d)

d1 = sorted(d.items(), reverse=True)
print(d1)