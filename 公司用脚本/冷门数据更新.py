import pymysql
import logging
import requests
import json
from pathlib import Path
import os

FORMAT = '%(asctime)s %(thread)d %(threadName)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename='update_database.log', filemode='w')


class Lengmen:
    def __init__(self):
        self.db = pymysql.connect("172.16.168.107", "soonet", "soonet", "soonetgh")
        self.mysql = self.db.cursor()
        self.handledID = []
        self.url = "http://172.16.189.27:9090/com.bgctv.sdp.platform.pubsub.pub"
        self.data = {}
        self.count = 0
        self.uploadData = set()

    def readfile(self):  # 读取从mysql中生成的文件
        with open('mysqlresult_20201013.txt') as f:
            for i in f:
                yield i

    def _reConn(self, num=2880000, stime=3):
        """
        校验数据库连接是否异常
        num：8小时
        stime：间隔3秒重连
        """
        _number = 0
        _status = True
        while _status and _number <= num:
            try:
                self.db.ping()  # cping 校验连接是否异常
                _status = False
            except:
                if self.db == True:  # 重新连接,成功退出
                    _status = False
                    break
                _number += 1
                time.sleep(stime)

    def update_database(self):
        for i in self.readfile():  # 拿到每一条id
            if self.count >= 3:
                break
            pid = i.replace("\n", "").split('_')[0]  # 切割id，去掉换行符，并以下划线为分割符
            titleid = i.replace("\n", "").split('_')[1]
            if titleid in self.handledID:
                continue
            #            self._reConn()
            #            with self.db:
            #            print("self.db.ping:{}, titleid:{}".format(self.db.ping(),titleid))
            sql = "SELECT * from resource_transcode WHERE Title_ID='{}'".format(titleid)  # 要执行的sql语句
            result = self.mysql.execute(sql)  # 执行sql语句
            results = self.mysql.fetchall()  # 获取所有记录列表
            for row in results:  # 一条条打印出来
                url = row[14]
                if url.split('/')[2] == 'trans':  # 取第二段判断
                    aliurl = url.replace('trans', 'aliyunoss')  # 要更新的url
                elif url.split('/')[2] == 'newtrans':
                    aliurl = url.replace('newtrans', 'aliyunoss')  # 要更新的url
                else:
                    print("unknown url:{}".format(url))
                #    sql = "UPDATE resource_transcode set URL='{}' WHERE ID='{}'".format(aliurl,row[0])
                #    result = self.mysql.execute(sql)
                #                print(aliurl)
                self.handledID.append(titleid)
                logging.info("handledID: {}".format(self.handledID))
                #            yield row
                yield url, aliurl, row[5], row[11]  # 返回url, Asset_ID和MovieID
            self.count += 1

    def upload_data(self):
        for url, aliurl, assetid, movieid in self.update_database():
            print(url, aliurl, assetid, movieid)
            upload_Data = Path(url).parent
            aliupload_Data = Path(aliurl).parent
            print("self.upload_data:{},{},{}".format(upload_Data, aliupload_Data, self.uploadData))
            if upload_Data not in self.uploadData:
                print("uploadData:{},self.uploadData:{}".format(upload_Data, self.uploadData))
                os.system('mkdir -p /offline_program_oss/%s' % (aliupload_Data))
                print("mkdir complete: {}".format(aliupload_Data))
                #                os.system('cp -raf %s/* /offline_program_oss/%s' %(upload_Data,aliupload_Data))
                #                print('copy complete')
                self.uploadData.add(Path(url).parent)  # 使用
                self.post()
            else:
                continue

    def post(self):
        for url, aliurl, assetid, movieid in self.update_database():
            self.data = {"topic": "CMP.Asset",
                         "message": {"OpType": "insert", "AssetID": "assetid", "MovieID": "movieid"}, "expiredate": "",
                         "valid": ""}
            data_json = json.dumps(self.data)
            response = requests.post(url=self.url, data=data_json)
            logging.info("响应状态码：{}, 响应内容：{}".format(response.status_code, response.text))


# if __name__ == '__main__':
test = Lengmen()
# print(test.update_database())
# test.upload_data()
test.upload_data()
# aaa = test.update_database()
# print(next(aaa))
# for i in bbb:
#    print(next(i))
