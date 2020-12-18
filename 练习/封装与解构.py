lst = list(range(10))
one,two,three,four,*_,Mtwo,Mone = lst
print(two, four, Mtwo)

lst1 = [1,(2,3,4),5]
_,(*_,a),_ = lst1
print(a)

s = 'JAVA_HOME=/usr/bin'
name,_,path = s.partition('=')
print(name,path)

name,path = s.split('=')
print(name,path)

name1,*_,path1 = s.split('=')
print(name1,path1)

lst2 = [1,9,8,7,6,5,4,3,2]
for i in range(9):
    for j in range(8-i):
        if lst2[j] > lst2[j+1]:
            lst2[j],lst2[j+1] = lst2[j+1],lst2[j]
print(lst2)

lst3 = [1,9,8,7,6,5,4,3,2]
for i in range(len(lst3)):
    for j in range(8,0,-1):
        if lst3[j] > lst3[j-1]:
            lst3[j],lst3[j-1] = lst3[j-1],lst3[j]
print(lst3)