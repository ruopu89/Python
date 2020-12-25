# 1 2 3        1 4
# 4 5 6  <=>   2 5
#              3 6
# 这是一个矩阵，但不是方阵
# enumerate(iterable[, start]) -> iterator for index, value of iterable
# 返回一个可迭代对象，将原有可迭代对象的元素和从start开始的数字配对

# 算法1
# 过程就是，扫描matrix第一行，在tm的第一列从上至下附加，然后再第二列附加。
# 举例，扫描第一行1,2,3，加入到tm的第一列，然后扫描第二行4,5,6，追加到tm的第二列

# 定义一个矩阵，不考虑稀疏矩阵
# 1 2 3        1 4
# 4 5 6  <=>   2 5
#              3 6
# import datetime
# matrix = [[1,2,3],[4,5,6]]
# tm = []
# count = 0
# for row in matrix:
#     for i,col in enumerate(row):
#         if len(tm) < i + 1:
#             tm.append([])
#             print('~~~~~~~~', tm)
#             # print('!!!!!!!!!!!',tm)
#             # break
#         tm[i].append(col)
#         count += 1
# print(matrix)
# print(tm)
# print(count)

# 思考：
# 能否一次性开辟目标矩阵的内存空间？
# 如果一次性开辟好目标矩阵内存空间，那么原矩阵的元素直接移动到转置矩阵的对称坐标就行了

# 1 2 3        1 4
# 4 5 6  <=>   2 5
#              3 6
# 在原有矩阵上改动，牵扯到增加元素和减少元素，麻烦，所以，定义一个新的矩阵输出

matrix = [[1,2,3],[4,5,6]]

tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]
print('~~~~~~~~~~~',tm)
count = 0

for i,row in enumerate(tm):
    for j,col in enumerate(row):
        tm[i][j] = matrix[j][i]
        count+=1

print(matrix)
print(tm)
print(count)