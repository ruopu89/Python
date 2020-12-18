line = "20200511231550_1496582320,10829.8h3BK2tIFM0J6H2EPxj9ix,2020-05-11 23:15:50.000,2020-05-12 00:02:51.000,2821.0,999999,0,0,0,0449045110,0449045110,10829,NULL,60010011,60010011,回看,NULL,NULL,NULL,0.0,4320,1016940650,Gehua.com,GEHU5512005110920000,英语(选修-师大版)11,英语(选修-师大版)11,\NVOD Catalog\RestartTV\空中课堂高二,NULL,0,NULL,551,空中课堂高二,2400.0"


def makekey(line=line):
    # print(type(line),line)
    # bytes(line)
    line1 = line.replace("\\N","\\\\N")
    # key = str(line.split(',')[25:26])
    # key1 = str(line.split(',')[31:32])
    # key1 = str(line.split())
    #print(1, key)
    # return key,key1
    return line1

print(makekey())

