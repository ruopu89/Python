import datetime
# matrix = [[1,2,3],[4,5,6]]
matrix = [[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,4],[2,5],[3,6]]
#
# print('\nMethod 1')
# start = datetime.datetime.now()
# for c in range(100000):
#     # print('***',c)
#     tm = []
#     for row in matrix:
#         for i,item in enumerate(row):
#             if len(tm) < i + 1:
#                 tm.append([])
#             tm[i].append(item)
# delta = (datetime.datetime.now()-start).total_seconds()
# print(delta)
# print(matrix)
# print(tm)


print('\nMethod 2')
start = datetime.datetime.now()
for c in range(100000):
    tm = [0] * len(matrix[0])
    # print("tm: {}".format(tm))
    for i in range(len(tm)):
        tm[i] = [0] * len(matrix)
        # print("tm: {}".format(tm))
    for i,row in enumerate(tm):
        for j,col in enumerate(row):
            tm[i][j] = matrix[j][i]
delta = (datetime.datetime.now()-start).total_seconds()
print(delta)
print(matrix)
print(tm)