from pathlib import Path
import csv
import re

def handleSpacedSowing():
    dbcs = {}
    dbsc = {}
    testdbcs = []
    p = Path('/media/shouyu/C64CC89B4CC8879F/works/异瀚数码/项目文档/脚本/20200217提取点播次数和时长-罗升廷/a/20200219all.csv')

    with open(str(p)) as f:
        reader = csv.reader(f)
        # print(next(reader))
        for i,c in enumerate(reader):
            if c[18] == 'application_name' or c[18] == 'duration':
                continue
            else:
                if c[18] not in dbcs.keys():

                    dbcs[c[18]] = 1
                    value = c[27]
                    # print(float(value))  # 不能使用int()转换非纯数字的字符串，如32.0，如果用int(32.0)就会报错
                    dbsc[c[18]] = float(value)
                else:
                    if c[18] == 'application_name' or c[18] == 'duration':
                        continue
                    dbcs[c[18]] += 1
                    value = c[27]
                    dbsc[c[18]] += float(value)
        print(dbcs)
        print(dbsc)



handleSpacedSowing()