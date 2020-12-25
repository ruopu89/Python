alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64decode(src:bytes):
    ret = bytearray()
    print(ret)
    length = len(src)
    step = 4
    for offset in range(0, length, step):
        tmp = 0x00
        block = src[offset:offset+step]
        for i,c in enumerate(reversed(block)):
            index = alphabet.find(c)
            print(12345, index)
            if index == -1:
                continue
            tmp += index << i*6
        ret.extend(tmp.to_bytes(3,'big'))
    return bytes(ret.rstrip(b'\x00'))
#
txt = "TWFuTQ=="
# # txt = "TWFuTQ=="
txt = txt.encode()
print(1, txt)
print(2, base64decode(txt).decode())
# print(3, base64decode(txt))
# =======================================================
# import base64
# print(base64.b64decode(txt).decode())