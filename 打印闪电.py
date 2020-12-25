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
n = int(input("pls input n: "))
w = n // 2
for i in range(-w, w+1):
    if i < 0:
        print(' '*-i + (w+i)*'*')
    elif i > 0:
        print(' '*w + (w-i)*'*')
    else:
        print('*'*n)
