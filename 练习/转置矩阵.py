# 转置矩阵
# 1 2 3           1 4 7
# 4 5 6    ==>    2 5 8
# 7 8 9           3 6 9
# 规律：对角线不动，a[i][j] <=> a[j][i]，而且到了对角线，就停止，去做下一行，对角线上的元素不动。

# 定义一个方阵
# 1 2 3           1 4 7
# 4 5 6    ==>    2 5 8
# 7 8 9           3 6 9
zhz = [[1,2,3],[4,5,6],[7,8,9]]
print(zhz)
count = 0
for i,row in enumerate(zhz):
    for j,col in enumerate(row):
        if i<j:
            zhz[i][j],zhz[j][i] = zhz[j][i],zhz[i][j]
            count+=1
print(zhz)
print(count)

# matrix = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[1,2,3,4]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
length = len(matrix)
count1 = 0
for i in range(length):
    print('!!!!!!!!',matrix)
    for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        count1 += 1
        print('~~~~~~~~~~',matrix)
print(matrix)
print(count1)
