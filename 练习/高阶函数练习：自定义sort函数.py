# def sort(iterable):
#     ret = []
#     for x in iterable:
#         print('s',ret)
#         for i,y in enumerate(ret):
#             print('0',ret)
#             if x > y:
#                 print('1',ret)
#                 ret.insert(i,x)
#                 print('2',ret)
#                 break
#         else:
#             ret.append(x)
#     return ret

# print(sort([6,4,3,1,3,6]))

# def sort(iterable,reverse=False):
#     ret = []
#     for x in iterable:
#         for i,y in enumerate(ret):
#             flag = x > y if reverse else x < y
#             if flag:   # 是否能进一步改进
#                 print(flag)
#                 ret.insert(i,x)
#                 break
#         else:
#             ret.append(x)
#     return ret
# print(sort([1,2,5,4,2,3,5,6]))

def sort(iterable,reverse=False,key=lambda x,y:x<y):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            flag = key(x,y) if not reverse else key(y,x)
            if flag:
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret
print(sort([1,2,5,4,2,3,5,6],True))

ss = list(map(lambda x:2*x+1,range(5)))
sss = dict(map(lambda x:(x%5,x),range(500)))
print(ss, sss)