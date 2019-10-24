# 打印一个边长为n的正方形
n = 5
print('*'*n)
for i in ('*'*(n-2)):
    print('*'+' '*(n-2)+'*')
print('*'*n)

n = 6
e = -n//2
for i in range(e,n+e):
    if i == e or i == n+e-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')

n = 5
for i in range(5):
    if i == 0 or i == n-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')

# 求100以内所有奇数之和
sum = 0
for i in range(1,100,2):
    sum += i
print(sum)

# 求1到5的阶乘之和
n = 5
sum = 0
for i in range(1,n+1):
    tmp = 1
    for j in range(1,i+1):
        tmp *= j
    sum += tmp
print(sum)

nums = 1
sum = 0
for n in range(1,6):
    nums *= n
    sum += nums
print(sum)

# 给一个半径，求圆的面积和周长。圆周率3.14
r = int(input('r='))
print('area='+str(3.14*r*r))
print('circumference='+str(2*3.14*r))

# 输入两个数，比较大小后，从小到大升序打印
a = input('first:')
b = input('second:')
if a > b:
    print(b,a)
else:
    print(a,b)

print(b,a) if a>b else print(a,b)
# 三目运算

# 获取最大值
m = int(input('Input first number >>>'))
while True:
    c = input('Input a number >>>')
    if c:
        n = int(c)
        if n > m:
            m = n
        print('Max is',m)
    else:
        break

# 输入n个数，求每次输入后的算数平均数
n = 0
sum = 0
while True:
    i = input('>>>')
    if i == 'quit':
        break
    n += 1
    sum += int(i)
    avg = sum/n
    print(avg)

# 九九乘法表
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print('{}*{}={}'.format(i,j,i*j),end=' ')
    print(" ")

for i in range(1,10):
    for j in range(i,10):
        print('{}*{}={}\t'.format(i,j,i*j),end=' ')
    print("")

for i in range(1,10):
    for k in range(1,i):
        print(end="\t ")
    for j in range(i,10):
        print('{}*{}={}\t'.format(i,j,i*j),end=' ')
    print(" ")

for i in range(1,10):
    for k in range(1,10-i):
        print(end="\t ")
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end="\t ") 
        # \t放在end=""中好像更容易理解
#         print("{}*{}={}\t".format(i,j,i*j),end=" ")
    print("")

# 打印100以内的斐波那契数列及打印第101项
# 费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出。首几个费波那契系数是：
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233……（OEIS中的数列A000045）
# 特别指出：0不是第一项，而是第零项。
a = 0
b = 1
print(a,end=",")
print(b,end=",")
for i in range(1,100):
    c = a + b
    if c > 100:
        break
    print(c,end=",")
#     a = b
#     b = c
    a,b = b,c
    # 这一句相当于a = b和b = c两句

# 打印101项斐波那契数
a = 0
b = 1
# 手动打印前两项
print('{},{}'.format(0, a))
print('{},{}'.format(1, b))
index = 1
while True:
    c = a + b
    a = b
    b = c
    index += 1
    print('{},{}'.format(index, c))
    # 这里的index就是显示中前面的序号
    if index == 101:
        break

# 打印第101项斐波那契数
a = 0
b = 1
# print('{},{}'.format(0,a))
# print('{},{}'.format(1,b))
index = 1
while True:
    c = a + b
    a,b = b,c
    index += 1
    if index == 101:
        print('{},{}'.format(index,c))
        break

a = 0
b = 1
for i in range(1,101):
    c = a + b
    a,b = b,c
    if i < 100:
        continue
    print(c)

# 求素数
n = int(input("Please input a prime number >>>"))
flag = False
for i in range(2,n):
    if n % i == 0:
        flag = True
        print(i)
        break
if flag:
    print(n,'is not a prime number.')
else:
    print(n,'is a prime number.')

n = int(input("Please input a prime number >>>"))
for i in range(2,int(n**0.5)):
    if n % i == 0:
        print(n,'is not a prime number.')
        break
else:
    print(n,'is a prime number.')

# 求10万内的所有素数
# 质数（Prime number），又称素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数（也可定义为只有1与该数本身两个正因数的数）。
# 大于1的自然数若不是素数，则称之为合数（也称为合成数）。
# 算术基本定理确立了素数于数论里的核心地位：任何大于1的整数均可被表示成一串唯一素数之乘积。
# 为了确保该定理的唯一性，1被定义为不是素数，因为在因式分解中可以有任意多个1（如3、1×3、1×1×3等都是3的有效约数分解）。
import time
t = [2]  # 素数从2开始
t0 = time.time()
count = 1
for x in range(3,100001,2):
    if x > 5 and x % 10 == 5:
        continue
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            break
    else:
        count += 1
        t.append(x)
print(t)
print('花费时间：{}'.format(time.time() - t0))
print('质数个数：{}'.format(count))
print('质数个数：{}'.format(len(t)))

# 打印菱形
for i in range(-3,4):
    if i < 0:
        prespace = -i
    else:
        prespace = i
    print(' '*prespace + '*'*(7-prespace*2))

for i in range(-3,4):
    prespace=-i if i<0 else i
    # 三目运算符方法。这里不能写成prespace=-i if (i < 0) else prespace=i，这样会报语法错误。
    print(' '*prespace+'*'*(7-prespace*2))  

# 打印对顶三角形
n = 7
e = n//2
for i in range(-e,n-e):
    prespace = -i if i<0 else i
    print(' '*(e-prespace)+'*'*(2*prespace+1))

# 打印闪电
for i in range(-3,4):
    if i < 0:
        print(' '*(-i)+'*'*(4+i))
    elif i > 0:
        print(' '*3+'*'*(4-i))
    else:
        print('*'*7)

j = '*'
for i in range(-3,4):
    if i == 0:
        print(j*7)
    print(' '*(-i)+j*(i+4)) if i < 0 else print(3*" "+j*(3-i))

# 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到了第10天早上想吃时，只剩下一个桃子了。求第一天共摘了多少个桃子。
# 猴子应该第九天吃完时就已经知道只剩下一个桃子了。
n = 1
for _ in range(1,10):
    n = (n+1)*2
    print(n)

# 改造，如果知道桃子的总量，算每天吃掉的数量
n = int(input(">>>"))
count = 0
while True:
    n = n/2-1
    if n <= 1:
        break
    print(n)
    count +=1
print('count:',count)


# 杨辉三角
# 方法一.
# 思路，首先把杨辉三角的前两行先放入大的列表中，之后从列表的第三个元素开始循环，先加入一个开头的1,
# 就是cur = [1]，再添加中间的部分，用pre是要计算的列表元素的上一个元素，也就是triangle列表中的哪个小的列表。
# for j in循环来添加中间的部分。最后再加上尾部的1，这样就凑出了杨辉三角的一行，把这一行追加到整个列表中，
# 整个列表就是杨辉三角
triangle=[[1],[1,1]]
for i in range(2,6):
    cur = [1]
    pre = triangle[i-1]
    for j in range(len(pre)-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)

# 先定义一个杨辉三角的空列表，下面进行循环，将计算出的row小列表追加到这个大的列表中。这里需要注意的是，当
# row列表追加到triangle列表中后，还可以再向这个row小列表中追加数据
triangle=[]
n = 4
for i in range(n):
    row = [1]
    triangle.append(row)
    if i == 0:  # i是0的时候从这里重新进入循环
        continue
    for j in range(i-1):   # i是2时才会进入这里
        row.append(triangle[i-1][j]+triangle[i-1][j+1])
    row.append(1)   # i是1时会直接跳转到这里追加1，不会执行上面的循环
print(triangle)

# 方法二，while
# 思路，通过多个小的列表呈现杨辉三角，每个列表打印后换行。先打印出第一行的[1]，之后从第二行开始计算，先把前
# 一行的数据复制到oldline，如第一次计算第二行时，就先把newline中的[1]复制给oldline，之后清空newline，
# 再计算后面的部分，用offset与i来控制。
n = 6
oldline = []
newline = [1]
# length = 0
print(newline)
for i in range(1,n):
    oldline = newline.copy()
    oldline.append(0)
    newline.clear()
    offset = 0
    while offset <= i:
        newline.append(oldline[offset - 1]+oldline[offset])
        offset += 1
    print(newline)

n = 6
oldline = []
newline = [1]
print(newline)
for i in range(1,n):
    oldline = newline.copy()
    oldline.append(0)
    newline.clear()
    offset = 0
    for j in range(i+1):
        newline.append(oldline[j-1]+oldline[j])
    print(newline)

triangle = []
n = 6
for i in range(n):
    row = [1]
    for k in range(i):
        row.append(1) if k == i-1 else row.append(0)
    triangle.append(row)
    if i == 0:
        continue
    for j in range(1,i//2+1):
        val = triangle[i-1][j-1] + triangle[i-1][j]
        row[j] = val
        if i != 2*j:
            row[-j-1] = val
print(triangle)

triangle = []
n = 6
for i in range(n):
    row = [1] * (i+1)  # i是2时，这里就是[1,1,1]
    triangle.append(row)   # 把[1,1,1]追加到triangle列表中
    for j in range(1,i//2+1):   # i是2时，这里的j只能是1
        val = triangle[i-1][j-1] + triangle[i-1][j]   
        # i是2，triangle[1][0] + triangle[1][1]，也就是[1,1]中的两个1相加就是val，再修改row[1]的值
        # 也就是[1,1,1]中，中间那个1改成了2
        # 当i是3时，这里还是循环一次，row是[1,1,1,1]，j是1，
        row[j] = val
        if i != 2*j:
            row[-j-1] = val
print(triangle)
