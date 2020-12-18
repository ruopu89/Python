filename1 = '/tmp/test.txt'
filename2 = '/tmp/test1.txt'

f = open(filename1, 'w+')
lines = ['abc', '123', 'magedu']
f.writelines('\t'.join(lines))
f.seek(0)
print(f.read())
f.close()

def copy(src, dest):
    with open(src) as f1:
        with open(dest, 'w') as f2:
            f2.write(f1.read())

copy(filename1, filename2)

with open(filename2) as f:
    print(2, f, f.read())