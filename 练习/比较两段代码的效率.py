# 如何比较两段代码的效率？效率一是看时间，一是看进入循环的次数
# 算10万以内的质数-1
# import datetime
# n = 100000
# pn = []
# count = 0
# start = datetime.datetime.now()
# for x in range(2, n):
#     for i in pn:
#         count += 1
#         if x % i == 0:
#             break
#     else:
#         pn.append(x)
# delta = (datetime.datetime.now() - start).total_seconds()
# print(len(pn))
# print(count)
# print(delta)
# print(pn)
# =======================================================================
import datetime
import math
n = 100000
pn = []
flag = False
count = 0
start = datetime.datetime.now()
for x in range(2, n):
    for i in pn:
        count += 1
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(x**0.5):
            flag = False
            break
    if not flag:
        pn.append(x)
delta = (datetime.datetime.now() - start).total_seconds()
print(len(pn))
print(count)
print(delta)
print(pn)