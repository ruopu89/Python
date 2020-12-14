# 输入两个数，比较大小后，从小到大升序打印
a = int(input("pls input n: "))
b = int(input("pls input n: "))
# if a > b:
#     print(b, a)
# else:
#     print(a, b)
print(a, b) if a < b else print(b, a)