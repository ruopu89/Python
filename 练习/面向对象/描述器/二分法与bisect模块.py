# 有一个无序序列[37, 99, 73, 48, 47, 40, 40, 25, 99, 51]，请先排序并打印输出。
# 分别尝试插入20、40、41到这个序列中合适的位置，保证其有序。
#
# 思路
# 排序后二分查找到适当位置插入数值。
# 排序使用sorted解决，假设升序输出。
# 查找插入点，使用二分查找完成。
# 假设全长为n，首先在大致的中点元素开始和待插入数比较，如果大则和右边的区域的中点继续比较，如果小则和左边的区域的中点进行比较，以此类推。
#
# def insert_sort(orderlist, i):
#     # print(1, "orderlist:{}".format(orderlist))
#     ret = orderlist[:]
#     low = 0
#     high = len(orderlist)
#     while low < high:  # 0 < 9
#         mid = (low + high) // 2
#         if orderlist[mid] < i:
#             low = mid + 1
#         else:
#             high = mid
#     print(2, "low:{}".format(low))
#     ret.insert(low, i)
#     return ret
#
# # newlst = []
# lst = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51]
# newlst = sorted(lst)
# r = newlst
# for x in (40, 20, 41, 100,200,5):
#     r = insert_sort(r, x)
#     print(3, "r:{}".format(r))
# =========================================================================
# 二分法
# Bisect模块
import bisect

lst = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51, 100]

newlst = sorted(lst)
print(newlst)
print(list(enumerate(newlst)))
print(20, bisect.bisect(newlst, 20))
print(30, bisect.bisect(newlst, 30))
print(40, bisect.bisect(newlst, 40))
print(20, bisect.bisect_left(newlst, 20))
print(30, bisect.bisect_left(newlst, 30))
print(40, bisect.bisect_left(newlst, 40))
# print(140, bisect.insort(newlst, 140), newlst)
for x in (20,30,40,100):
    bisect.insort_left(newlst, x)
    print(newlst)
