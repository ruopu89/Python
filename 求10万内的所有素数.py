# 质数（Prime number），又称素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数（也可定义为只有1与该数本身两个正因数的数）。
# 大于1的自然数若不是素数，则称之为合数（也称为合成数）。
# 算术基本定理确立了素数于数论里的核心地位：任何大于1的整数均可被表示成一串唯一素数之乘积。
# 为了确保该定理的唯一性，1被定义为不是素数，因为在因式分解中可以有任意多个1（如3、1×3、1×1×3等都是3的有效约数分解）。
# import  time
# abc = time.time()
# flag = False
# jh = [2,3]
# for i in range(4,10001):
#     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 10 == 0:
#         continue
#     for j in range(2, 10001):
#         if i % j == 0:
#             continue
#     else:
#         jh.append(i)
# print(jh, "花费时间：{}".format(time.time() - abc))
import time
t = time.time()
count = 1
abc = [2]
for i in range(3, 100001, 2):
    if i > 5 and i % 10 == 5:
        continue
    for j in range(3, int(i ** 0.5)+1, 2):
        if i % j == 0:
            break
    else:
        count += 1
        abc.append(i)
print("使用时长：{}".format(time.time()-t))
print(abc)
print("素数个数：{}".format(count))