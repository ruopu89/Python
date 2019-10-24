# 冒泡法
# 冒泡法总结
# - 冒泡法需要数据一轮轮比较
# - 可以设定一个标记判断此轮是否有数据交换发生，如果没有发生交换，可以结束排序，如果发生交换，继续下一轮排序
# - 最差的排序情况是，初始顺序与目标顺序完全相反，遍历次数1,...,n-1之和n(n/1)/2
# - 最好的排序情况是，初始顺序与目标顺序完全相同，遍历次数n-1
# - 时间复杂度O(n**2)
## 方法一
num_list = [[1,9,8,5,7,6,4,2,3],[1,2,3,4,5,6,7,9,8]]
nums = num_list[1]
print(nums)
length = len(nums)
count_swap = 0
count = 0
for i in range(length):
    for j in range(length-i-1):
        count += 1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            count_swap += 1
print(nums, count_swap, count)

## 方法二优化
num_list = [[1,9,8,5,7,6,4,2,3],[1,2,3,4,5,6,7,9,8]]
nums = num_list[1]
print(nums)
length = len(nums)
count_swap = 0
count = 0

for i in range(length):
    flag = False
    for j in range(length-i-1):
        count += 1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums, count_swap, count)

# 命名元组 namedtuple
# 语法：
    # namedtuple(typename,field_names,verbose=False,rename=False)
    # 命名元组，返回一个元组的子类，并定义了字段
    # typename表示此元组的名称
    # field_names表示元组中元素的名称，此字段有多种表达方式，可以是空白符或逗号分隔的字段的字符串，可以是字段的列表
    # rename表示如果元素名称中含有python的关键字，则必须设置为rename=True
    # verbose使用默认就可以。

from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
s = Student('Jim',21,'male','123@fqq.com')
print(s.name)
print(s.age)
isinstance(s,tuple)

