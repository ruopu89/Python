# s1 = 'abcdefg'
# s2 = 'defabcd'
# s2 = 'defabcdoabcdeftw'
# s3 = '1234a'
# s4 = "5678"
# s5 = 'abcdd'
#
# def findit(str1, str2):
#     matrix = []
#     xmax = 0
#     xindex = 0
#     for i,x in enumerate(str2):
#         matrix.append([])
#         # print('1', matrix[i])
#         # print(matrix)
#         for j,y in enumerate(str1):
#             if x != y:
#                 # print('1',matrix[i])
#                 matrix[i].append(0)
#                 # print('2',matrix[i])
#                 # break
#             else:
#                 if i == 0 or j == 0:
#                     matrix[i].append(1)
#                 else:
#                     matrix[i].append(matrix[i-1][j-1]+1)
#                 if matrix[i][j] > xmax:
#                     print('1',matrix[i][j],xmax)
#                     xmax = matrix[i][j]
#                     print('2',matrix[i][j],xmax)
#                     xindex = j
#                     xindex += 1
#             # print(matrix)
#     return str1[xindex-xmax:xindex]
#
# print(findit(s1,s2))
# ===============================================================
s1 = 'abcdefg'
s2 = 'defabcdoabcdeftw'
s3 = '1234a'

def findit(str1,str2):
    count = 0
    length = len(str1)

    for sublen in  range(length,0,-1):
        for start in range(0,length-sublen+1):
            substr = str1[start:start+sublen]
            count += 1
            print(substr)
            if str2.find(substr) > -1:
                # print('111',substr, str2.find(substr), sublen)
                # print(substr)
                print('count={},substrlen={}'.format(count,sublen))
                return substr

print(findit(s1,s2))
print(findit(s1,s3))
