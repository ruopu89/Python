alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
teststr = "abcda"
teststr1 = "ManMa"

def base64(src):
    ret = bytearray()
    length = len(src)
    r = 0
    for offset in range(0,length,3):
        if offset+3 <= length:  # 每3个字节为一段，取一次
            triple = src[offset:offset+3]
        else:
            triple = src[offset:]   # 不够3个字节的补0
            r = 3-len(triple)
            triple = triple+'\x00'*r
        b = int.from_bytes(triple.encode(),'big')   # 将字节转换为bytes类型再转换为数字
        print(hex(b),b,type(b),'@!@',type(triple),'!@!',triple,'#!@',triple.encode())
        for i in range(18,-1,-6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F
            ret.append(alphabet[index])
            print('~~~~',index,type(index))
        for i in range(1,r+1):
            print("r: {}, i: {}".format(r,i))
            ret[-i] = 0x3D
            print("ret: {}".format(ret[-i]))
    return ret

print(base64(teststr))
# s = int.from_bytes(b'abc','big')
# print(bin(s))