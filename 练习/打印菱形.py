# 思路：
# 行号	个数		前空格		总空格数
#  1	   1		3			6
#  2	   3		2			4
#  3	   5		1			2
#  4	   7		0			0
#  5	   5		1			2
#  6	   3		2			4
#  7	   1		3			6
# 这是中心对称的
# 我们关注的是一行如果打满星号总共的数量与前空格一列，每行菱形前面的空格从3-0,再从0-3
# for i in range(-3,4):
#     if i < 0:
#         prespace = -i
#     else:
#         prespace = i
#     print(' ' * prespace + '*' * (7-prespace*2))

# 1
# for i in range(-3, 4):
#     pre = -i if i<0 else i
#     print(' '*pre+'*'*(7-pre*2))

# 2
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'*'*(n-pre*2))

# 3
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre + '*'*(n-pre*2))

# 4
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'*'*(n-pre*2))

# 5
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'!'*(n-pre*2))

# 6
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'#'*(n-pre*2))

# 7
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'='*(n-pre*2))

# 8
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'&'*(n-pre*2))

# 9
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'*'*(n-pre*2))

# 10
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*pre+'*'*(n-pre*2))