# 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到了第10天早上想吃时，只剩下一个桃子了。求第一天共摘了多少个桃子。
# 猴子应该第九天吃完时就已经知道只剩下一个桃子了。
# n = 1
# for _ in range(1, 10):
#     n = (n+1)*2  # x/2-1=n
#     print(n)

# 1
# n = 1
# print(1, n)
# count = 1
# for _ in range(1, 10):
#     count += 1
#     n = (n+1)*2
#     print(count, n)

# 2
n = 1
count = 1
for _ in range(1, 10):
    n = (n+1)*2
    print(n)