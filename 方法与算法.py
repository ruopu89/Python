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

# 简单选择排序
  # 属于选择排序
  # 两两比较大小，找出极值（极大值或极小值）被放置在固定的位置，这个固定位置一般指的是某一端
  # 结果分为升序和降序排列
# 降序
  # n个数从左至右，索引从0开始到n-1，两两依次比较，记录大值索引，此轮所有数比较完毕，将大数和索引为0的数交换，如果大数就是索引0，不交换。第二轮，从索引1开始比较，找到最大值，将它和索引1位置交换，如果它就在索引1位置则不交换。依次类推，每次左边都会固定下一个大数。
# 升序
  # 和降序相反

# 简单选择排序代码实现一  
m_list = [[1,9,7,2,3,4,6,5,8],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]]
nums = m_list[0]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0

for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
    if i != maxindex:
        nums[i],nums[maxindex] == nums[maxindex],nums[i]
        count_swap += 1
        
print(nums,count_swap,count_iter)

# 简单选择排序代码实现二（优化）
m_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]]
nums = m_list[1]
length = len(nums)
print(nums)

count_swap = 0   # 交换次数
count_iter = 0   # 迭代次数

for i in range(length // 2):   # [1,9,8,5,6,7,4,3,2]，因为每轮找到两个极值，所以要整除2
    maxindex = i
# 假定最大值的索引是最左边的i
    minindex = -i - 1
# 假定最小值的索引是最右边的数，因为是前包后不包，所以还要减1
    minorigin = minindex
# minorigin是记录每轮最小值开头的索引，每轮最大值开头的索引就是i，但没有记录最小值开头的索引，所以这里
# 要定义一个minorigin。
    
    for j in range(i + 1, length - i):  # 每次左右都要少比较一个，所以range()内的数字都要减少
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
        if nums[minindex] > nums[-j - 1]:
            minindex = -j - 1
# 每轮进行两次比较，得到最大值与最小值索引          
#     print(maxindex,minindex)  打印每轮比较后得到的两个极值 
    
    if i != maxindex:   
# 如果最大值索引与i不同，就进行下面的交换。下面交换的是值，也就是把最大索引指向的值与i指向听值交换
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        # 上面三行改为nums[i],nums[maxindex] = nums[maxindex],nums[i]也可以。
        count_swap += 1
        if i == minindex or i == length + minindex:
            minindex = maxindex
# 这里需要判断一下最小值索引与i是不是一样的，如果一样，经过上面最大值的交换后，i索引的值也发生了变化。所
# 以这里要判断一下，如果i与最小值索引一样，那么就说明i受到了影响，因为上面i与maxindex指向的值对调了，
# 所以，索引也应该对调，所以这里把maxindex赋值给minindex。这样做是为了修正最小值的索引，因为如果最小
# 值索引就是i，那就上面交换后发生了变化，最小值索引变成了maxindex，所以这里要将maxindex赋值给
# minindex。上面的判断中使用了or来判断两种情况是因为minindex可能是负数，i是不会等于负数的，如果是负
# 数，就要用长度加上这个负索引值，这是就修正为了正数的索引。保存了最小值索引，才能保证下面的判断是有意义的。
    if minorigin != minindex:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap += 1
# 这里与上面一样，判断最小值索引与minorigin是否一致，如果不一致就要交换这两个索引指向的值。
print(nums, count_swap, count_iter)
输出：
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1] 8 20
# 通过取两个极值，可以看到迭代的次数从36变成了20

# 改进实现一
m_list = [[1,9,7,2,3,4,6,5,8],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],[1,1,1,1,1,1,1,1,1]]
nums = m_list[3]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0

for i in range(length // 2):
    maxindex = i
    minindex = -i-1
    minorigin = minindex
    for j in range(i+1,length-i):
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
        if nums[minindex] > nums[-j-1]:
            minindex = -j-1
            
    if nums[maxindex] == nums[minindex]:
        break
        
    if i != maxindex:
        nums[i],nums[maxindex] = nums[maxindex],nums[i]
        count_swap += 1
        if i == minindex or i == length+minindex:
            minindex = maxindex
    if minorigin != minindex:
        nums[minorigin],nums[minindex] = nums[minindex],nums[minorigin]
        count_swap += 1
print(nums,count_swap,count_iter)

# 改进实现二
m_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,2]]
nums = m_list[3]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0

for i in range(length // 2):
    maxindex = i
    minindex = -i-1
    minorigin = minindex
    for j in range(i+1,length-i):
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
        if nums[minindex] > nums[-j-1]:
            minindex = -j-1
    print(maxindex,minindex)
    
    if nums[maxindex] == nums[minindex]:
        break
        
    if i != maxindex:
        nums[i],nums[maxindex] = nums[maxindex],nums[i]
        count_swap += 1
        if i == minindex or i == length + minindex:
            minindex = maxindex
    
    if minorigin != minindex and nums[minorigin] != nums[minindex]:
        nums[minorigin],nums[minindex] = nums[minindex],nums[minorigin]
        count_swap += 1
print(nums,count_swap,count_iter)
