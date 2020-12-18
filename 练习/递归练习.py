# pre = 0
# cur = 1
# print(pre,cur,end=' ')
# n = 4
# for i in range(n-1):
#     pre,cur = cur, pre+cur
#     print(cur,end=' ')
# print()
#
#
# def fib(n):
#     # print(fib(n-1),fib(n-2))
#     return 1 if n < 2 else fib(n-1)+fib(n-2)
#
# for i in range(4):
#     print(fib(i),end=' ')
# print(fib(4))
# ====================================================
# pre = 0
# cur = 1
# print(pre,cur,end=' ')
# def fib(n,pre=0,cur=1):
#     pre,cur = cur,pre+cur
#     print(cur,end=' ')
#     if n == 2:
#         return
#     fib(n-1,pre,cur)
# fib(5)
# ==========================================
# def func(num):
#     if num == 1:
#         return 1
#     else:
#         return num * func(num-1)
#
# print(func(5))
# ---------------------------------------------
# def factorial(n,mu1=1):
#     mu1 *= n
#     if n == 1:
#         return mu1
#     return factorial(n-1,mu1)
#
# print(factorial(5))
# ================================================
# def fac(n):
#     if n == 1:
#         return 1
#     return n*fac(n-1)
# print(fac(5))
# =====================================
# def fac1(n,p=1):
#     if n == 1:
#         return p
#     p *= n
#     print(p)
#     fac1(n-1,p)
#     return p
# fac1(5)
# ======================================
# def fac2(n,p=None):
#     if p is None:
#         p = [1]
#     if n == 1:
#         return p[0]
#     p[0] *= n
#     print()
# =====================================
# def fac2(n,p=None):
#     if p is None:
#         p = [1]
#     if n == 1:
#         return p[0]
#     p[0] *= n
#     print(p[0])
#     fac2(n-1,p)
#     return p
#
# n = 5
# print(fac2(n))
# ==============================================
# 将一个数逆序放入列表中，例如1234 -> [4,3,2,1]
# data = str(1234)
# def reversal(x):
#     if x == -1:
#         return ''
#     else:
#         return data[x] + reversal(x-1)
#
# print(reversal(len(data)-1))
# ===========================================
# def reverse(n,lst=None):
#     if lst is None:
#         lst = []
#     lst.append(n%10)
#     if n//10 == 0:
#         return lst
#     return reverse(n//10,lst)
#
# s = reverse(12345)
# print(s)
# ==============================================
# data = str(1234)
# def revert(x):
#     if x == -1:
#         return ''
#     return data[x] + revert(x-1)
# print(revert(len(data)-1))
# ==========================================
# def revert(n,lst=None):
#     if lst is None:
#         lst = []
#
#     x,y = divmod(n,10)
#     lst.append(y)
#     if x == 0:
#         return lst
#     return revert(x,lst)
#
# s = revert(12345)
# print(s)
# =======================================
# num = 1234
# def revert(num,target=[]):
#     if num:
#         target.append(num[len(num)-1])
#         revert(num[:len(num)-1])
#     return target
# print(revert(str(num)))
# ==================================
# def peach(day=9,sum=1):
#     sum=2*(sum+1)
#     day-=1
#     if day==0:
#         return sum
#     return peach(day,sum)
# print(peach())
# ======================================
# def monkey(n):
#     if n == 1:
#         return 1
#     return 2*(monkey(n-1)+1)
#
# peach = monkey(10)
# print(peach)
# for _ in range(10):
#     print(_,"-->",monkey(_))
# =====================================
# def peach(days=10):
#     if days == 1:
#         return 1
#     return (peach(days-1)+1)*2
#
# print(peach())
# ========================================
# def peach(days=1):
#     if days == 10:
#         return 1
#     return (peach(days+1)+1)*2
#
# print(peach())
# =========================================
import datetime
start = datetime.datetime.now()
# pre = 0
# cur = 1
# print(pre,cur,end=' ')
# n = 100
# for i in range(n-1):
#     pre,cur = cur,pre+cur
#     print(cur, end=' ')
# delta = (datetime.datetime.now()-start).total_seconds()
# print(delta)

# def fib1(n,pre=0,cur=1):
#     pre,cur = cur,pre+cur
#     print(cur,end=' ')
#     if n == 2:
#         return
#     fib1(n-1,pre,cur)
#
# fib1(100)
# delta = (datetime.datetime.now()-start).total_seconds()
# print(delta)
# ==========================================================
def fib2(n):
    if n < 2:
        return 1
    return fib2(n-1)+fib2(n-2)

for i in range(100):
    print(fib2(i),end=' ')
delta = (datetime.datetime.now()-start).total_seconds()
print(delta)

