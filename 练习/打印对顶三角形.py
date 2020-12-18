# 思路：
# 行号	对称序列	  星号数	  总空格数	前置空格数		后置空格数
#  1		3			7			0		0				0
#  2		2			5			2		1				1
#  3		1			3			4		2				2
#  4		0			1			6		3				3
#  5		1			3			4		2				2
#  6		2			5			2		1				1
#  7		3			7			0		0				0
# 可以看出，只与前置空格、起点、终点有关
# n = 7
# e = n//2
# for i in range(-e, n-e):
#     prespace = -i if i<0 else i
#     print(' ' * (e-prespace) + '*' * (2 * prespace+1))

# n = 7
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre) + '*' * (2*pre+1))
#
# n = 7
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre)+'*'*(2*pre+1))

# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre)+'*'*(2*pre+1))

# 4
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i < 0 else i
#     print(' '*(e-pre)+'*'*(2*pre+1))

#5
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre)+'*'*(2*pre+1))

# 6
# n = 9
# e = n // 2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre) + '*'*(2*pre+1))

# 7
# n = 9
# e = n // 2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre)+'*'*(2*pre+1))

# 8
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre)+'*'*(2*pre+1))

# 9
# n = 9
# e = n//2
# for i in range(-e, n-e):
#     pre = -i if i<0 else i
#     print(' '*(e-pre)+'*'*(2*pre+1))

# 10
n = 9
e = n//2
for i in range(-e,n-e):
    pre = -i if i<0 else i
    print(' '*(e-pre)+'*'*(2*pre+1))