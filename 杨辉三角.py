# a = [[1], [1,1]]
# n = int(input("pls input n: "))
# for i in range(2, n+1):
#     cur = [1]
#     pre = a[i-1]  # 前一个索引，第一次[1,1]
#     for j in range(len(pre)-1):
#         cur.append(pre[j]+pre[j+1])
#     cur.append(1)
#     a.append(cur)
# print(a)
# a = []
# n = int(input("pls input n: "))
# for i in range(n):
#     row = [1]
#     a.append(row)
#     if i == 0:
#         continue
#     for j in range(i-1):
#         row.append(a[i-1][j]+a[i-1][j+1])
#     row.append(1)
# print(a)

# n = int(input("pls input n: "))
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1, n):
#     oldline = newline.copy()
#     print(1, oldline)
#     oldline.append(0)  # [1, 0]
#     print(2, oldline)
#     newline.clear()
#     offset = 0
#     while offset <= i:
#         newline.append(oldline[offset-1]+oldline[offset])
#         print(3, oldline)
#         print(4, newline)
#         offset += 1
#     print(newline)

# n = 6
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1, n):
#     oldline = newline.copy()
#     oldline.append(0)
#     print(1, oldline)
#     newline.clear()
#     for j in range(i+1):
#         newline.append(oldline[j-1]+oldline[j])
#         print(2, oldline)
#         print(3, newline)
#     print(newline)
# a = []
# n = 5
# for i in range(n):
#     row = [1] * (i+1)
#     a.append(row)
#     for j in range(1, i//2+1):
#         val = a[i-1][j-1] + a[i-1][j]
#         row[j] = val
#         if i != 2*j:
#             row[-j-1] = val
# print(a)

# triangle = [[1],[1,1]]
# for i in range(2,6):
#     cur = [1]
#     pre = triangle[i-1]
#     for j in range(len(pre)-1):
#         cur.append(pre[j]+pre[j+1])
#     cur.append(1)
#     triangle.append(cur)
# print(triangle)

# triangle = []
# n = 4
# for i in range(n):
#     row = [1]
#     triangle.append(row)
#     if i == 0:
#         continue
#     for j in range(i-1):
#         row.append(triangle[i-1][j]+triangle[i-1][j+1])
#     row.append(1)
# print(triangle)

# n = 6
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1, n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#     offset = 0
#     while offset <= i:
#         newline.append(oldline[offset-1]+oldline[offset])
#         offset += 1
#     print(newline)

# n = 6
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1,n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#     offset = 0
#     while offset <= i:
#         newline.append(oldline[offset-1]+oldline[offset])
#         offset += 1
#     print(newline)

# n = 6
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1,n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#     offset = 0
#     while offset <= i:
#         newline.append(oldline[offset-1]+oldline[offset])
#         offset += 1
#     print(newline)

# n = 6
# oldline = []
# newline = [1]
# print(newline)
# for i in range(1,n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#     # offset = 0
#     for j in range(i+1):
#         newline.append(oldline[j-1]+oldline[j])
#     print(newline)

# triangle = []
# n = 6
# for i in range(n):
#     row = [1]
#     for k in range(i):
#         row.append(1) if k == i-1 else row.append(0)
#     triangle.append(row)
#     if i == 0:
#         continue
#     for j in range(1, i//2+1):
#         val = triangle[i-1][j-1]+triangle[i-1][j]
#         row[j] = val
#         if i != 2*j:
#             row[-j-1] = val
# print(triangle)

triangle = []
n = 6
for i in range(n):
    row = [1] * (i+1)
    triangle.append(row)
    for j in range(1,i//2+1):
        val = triangle[i-1][j-1]+triangle[i-1][j]
        row[j] = val
        if i != 2*j:
            row[-j-1] = val
print(triangle)