# 语法：lambda 参数列表:表达式
# 切记，不需要return，表达式的值就是return的值

print((lambda :0)())
print((lambda x,y=3:x+y)(5))
print((lambda x,y=4:x+y)(5,2))
print((lambda *args:(x for x in args))(*range(5)))
print((lambda args:[x+1 for x in args])(range(5)))
print((lambda args:{x+2 for x in args})(range(5)))
print((lambda args:(x+1 for x in args))(range(5)))
s = [x for x in (lambda args:map(lambda x:x+1,args))(range(5))]
print('~~~~~~~~~~~',s)
s1 = [x for x in (lambda args:map(lambda x:(x+1,args),args))(range(5))]
print('!!!!!!!!!!!!!!!',s1)