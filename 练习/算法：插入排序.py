m_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,2]]
nums = [0] + m_list[0]
sentinel,*origin = nums
count_swap = 0
count_iter = 0
length = len(nums)
for i in range(2,length):
    nums[0] = nums[i]
    j = i - 1
    count_iter += 1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j -= 1
            count_swap += 1
        nums[j+1] = nums[0]
print(nums,count_swap, count_iter)
