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

n = int(input("pls input n: "))
w = n // 2
if n % 2 == 0:
    n += 1
for i in range(-n, n+1):
    abc = -i if i < 0 else i
    print(' '*(n-abc) + '*'*(abc+1))