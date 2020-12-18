# triangle = [[1],[1,1]]
# for i in range(2, 6):
#     cur = [1]
#     pre = triangle[i-1]  # 第一次[1,1]
#     for j in range(len(pre) - 1): # 这里是range(1)时，j只能是0
#         cur.append(pre[j]+pre[j+1])  # pre[0]+pre[1]=1+1=2
#     cur.append(1)
#     triangle.append(cur)
# print(triangle)
# for a in range(1):
#     print(a)
# =================================================================
# triangle = []
# n = 6
# for i in range(n):
#     row = [1]
#     triangle.append(row)
#     if i == 0:
#         continue
#     for j in range(i-1):   # range(0)时，j是空，什么都不会输出
#         row.append(triangle[i-1][j]+triangle[i-1][j+1])
#     row.append(1)
# print(triangle)
# for i in range(0):
#     print(i)
# ===============================================================
# n = 6
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1, n):
#     oldline = newline.copy()
#     oldline.append(0)   # [1,0]
#     newline.clear()
#     offset = 0
#     while offset <= i:
#         newline.append(oldline[offset-1] + oldline[offset])
#         # print(newline,'**********')
#         offset += 1
#     print(newline)
# =========================================================================
# n = 6
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1, n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#     offset = 0
#     for j in range(i+1):
#         newline.append(oldline[j-1] + oldline[j])
#     print(newline)
# =============================================================================
# 尾部追加效率最高
# 能不能一次性开辟空间。所谓一次性开辟，就是将一列先算出来，不断向后追加，直到追加完最后一个1。中间部分先用数字填充，下面两例使用0或1来填充。如[1,0,1] [1,1,1,1]
# 列表解析式
# 循环迭代
# 能不能少算一半的数字
# 思路：先开辟新列表，把列表中元素的个数先定下来，之后再改。下面计算包括中间点向左部分的数字，
# 也就是range(1,i//2+1)，之后每计算出中间点向左部分的数字时，都会用if判断语句在反方向相对应的位置加入
# 相同的一个数字。最后修改的是中间部分的数字。
# triangle = []
# n = 6
# for i in range(n):
#     row = [1]
#     for k in range(i):
#         row.append(1) if k == i-1 else row.append(0)
#     triangle.append(row)
#     if i == 0:
#         continue
#     for j in range(1, i//2+1):  # range(1,1)时，j是空，不会打印输出
#         val = triangle[i-1][j-1] + triangle[i-1][j]
#         row[j] = val
#         if i != 2*j:
#             row[-j-1] = val
# print(triangle)
# ==============================================================================
# for i in range(1,1):
#     print(i)
# =============================================================================
triangle = []
n = 6
for i in range(n):
    row = [1] * (i+1) # [1],[1,1],[1,1,1]
    triangle.append(row)
    for j in range(1, i//2+1):
        val = triangle[i-1][j-1] + triangle[i-1][j]
        row[j] = val
        if i != 2*j:
            row[-j-1] = val
print(triangle)