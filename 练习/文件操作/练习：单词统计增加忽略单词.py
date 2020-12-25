# 对sample文件进行不区分大小写的单词统计
# 要求用户可以排除一些单词的统计，例如a、the、of等不应该出现在具有实际意义的统计中，应当忽略。
# 要求，全部代码使用函数封装、调用完成
# 之前代码中，切分单词的太繁琐，因为makekey1函数已经可以直接把一行数据切成一个个单词了，所以对上面的代码重新封装。
def makekey2(line:str,chars=set("""!'"#./\()[],*- \r\n""")):
    start = 0

    for i,c in enumerate(line):
        # print(1,i,c)
        if c in chars:
            print(3, start, i)
            if start == i:
                print(1, start,i)
                start += 1
                print(2, start, i)
                continue
            print('start:{},i:{},line:{}'.format(start,i,line))
            yield line[start:i]
            start = i + 1
    else:
        if start < len(line):
            yield line[start:]

abc = makekey2('.a.b.c')
print(next(abc))
print(next(abc))
print(next(abc))

# for i in makekey2('.a.bc'):
#     print(i)


def wordcount(filename,encoding='utf8',ignore=set()):
    d = {}
    with open(filename,encoding=encoding) as f:
        for line in f:
            for word in map(str.lower,makekey2(line)):
                if word not in ignore:
                    d[word] = d.get(word,0) + 1
    return d

def top(d:dict,n=10):
    for i,(k,v) in enumerate(sorted(d.items(),key=lambda item:item[1],reverse=True)):
        if i > n:
            break
        print(k,v)

# top(wordcount('/media/shouyu/C64CC89B4CC8879F/works/马哥2018python/01.课堂笔记/p10c06/sample.txt',ignore={'the','a'}))

