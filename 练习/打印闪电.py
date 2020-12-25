# 思路：
# 行号	个数		前空格		后空格数	总空格数	数据
#  1	   1		3			3			6		-3
#  2	   2		2			3			5		-2
#  3	   3		1			3			4		-1
#  4	   7		0			0			0		0
#  5	   3		3			1			4		1
#  6	   2		3			2			5		2
#  7	   1		3			3			6		3
# 看一下上面数据一列
# for i in range(-3, 4):
#     if i < 0:
#         print(' ' * (-i) + '*' * (4+i))
#     elif i > 0:
#         print(' ' * 3 + '*' * (4-i))
#     else:
#         print('*' * 7)
# ===============================================================
# j = '*'
# for i in range(-3, 4):
#     if i == 0:
#         print(j * 7)
#     print(" " * (-i) + j * (i+4)) if i<0 else print(3*" " + j*(3-i))

# n = 13
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(e*' '+'*'*(e-i))

# 1
# n = 5
# e = n//2
# print(e)
# for i in range(-e, n-e): # -2,3, -2,-1,0,1,2
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i), (e-i), e, i)

# 2
# n = 5
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 3
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 4
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 4
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 5
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 6
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 7
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 8
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 9
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     if i == 0:
#         print('*'*n)
#     print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))

# 10
n = 9
e = n//2
for i in range(-e, n-e):
    if i == 0:
        print('*'*n)
    print(' '*(-i)+'*'*(i+e+1)) if i<0 else print(' '*e+'*'*(e-i))