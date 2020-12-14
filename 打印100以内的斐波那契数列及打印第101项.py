# 打印100以内的斐波那契数列及打印第101项
a,b,c = 0,1,1
sum = [a,b,c]
# print(sum)
# while True:
#     d = b + c
#     if d > 100:
#         break
#     sum.append(d)
#     b,c = c,d
# print(sum)

for i in range(102):
    d = b + c
    sum.append(d)
    b,c = c,d
print(sum.index(sum[101]), sum[101])
# 573147844013817084101