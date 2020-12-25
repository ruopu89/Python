# -*- coding: utf-8 -*-

import datetime
import pymysql
import logging
import psutil
import requests
import json
import multiprocessing
from pathlib import Path
import os
from threading import Event, Thread

FORMAT = '%(asctime)s %(thread)d %(threadName)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename='update_database.log', filemode='a')

class Lengmen:
    def __init__(self):
        self.db = pymysql.connect("172.16.168.107", "soonet", "soonet", "soonetgh")
        self.mysql = self.db.cursor()
        self.handledID = set()   # 保存已处理过的titleid
        self.url = "http://172.16.189.27:9090/com.bgctv.sdp.platform.pubsub.pub"
        self.data = {}
        self.count = 0
        self.uploadData = set()
        self.event = Event()

    def readfile(self):  # 读取从mysql中生成的文件
        with open('mysqlresult_20201013.txt') as f:
            for i in f:
                yield i

    def _reConn(self):   # 重连mysql
        if self.db.ping():
            self.db = pymysql.connect("172.16.168.107", "soonet", "soonet", "soonetgh")
            self.mysql = self.db.cursor()

    def update_database(self):
        for i in self.readfile():  # 拿到每一条id
            with open('handleURL.txt','r+') as f:
                if i in f.read():
                    continue
#            if len(open('handleURL.txt', 'r').readlines()) >= 1000:   # 统计文件行数
#                break
#            else:
#                print('line: {}'.format(len(open('handleURL.txt', 'r').readlines())))
            pid = i.replace("\n", "").split('_')[0]  # 切割id，去掉换行符，并以下划线为分割符
            titleid = i.replace("\n", "").split('_')[1]
            # 10014_GTIT0120150923200361  pid与titleid混在了一起，前面是pid，后面是titleid
            if titleid in self.handledID:  # 已处理过的titleid列表，如果titleid在列表中就跳过，说明已经处理了
                continue
            self._reConn()  # 避免mysql断开，重连机制
            sql = "SELECT * from resource_transcode WHERE Title_ID='{}'".format(titleid)  # 要执行的sql语句，一段会有四条结果
            result = self.mysql.execute(sql)  # 执行sql语句
            results = self.mysql.fetchall()  # 获取mysql执行后所有记录的列表
            for row in results:  # 一条条打印出来
                url = row[14]  # 获取结果中的url路径
                if url.split('/')[2] == 'trans':  # 取第二段判断，因为第二段可能是trans，也可能是newtrans
                    aliurl = url.replace('trans', 'aliyunoss')  # 要更新的url
                elif url.split('/')[2] == 'newtrans':
                    aliurl = url.replace('newtrans', 'aliyunoss')  # 要更新的url
                elif url.split('/')[2] == 'newtrans2':
                    aliurl = url.replace('newtrans2', 'aliyunoss')  # 要更新的url
                else:
                    logging.info("unknown url:{}".format(url))
                    aliurl = url
                self.handledID.add(titleid)  # 写在这里要重复加四次，个人感觉应该这样写，不然下面的yield又没法一次返回4条记录的结果
                logging.info("handledID: {}".format(self.handledID))
                yield url, aliurl, row[5], row[4], i  # 返回url,aliurl,Asset_ID和MovieID，i是pid_titleid

    def upload_data(self):
        for url, aliurl, assetid, movieid, i in self.update_database():
#            with open('/root/scripts/yaoscr/handleURL.txt','r') as f:
#                count = len(f.readlines())
#                print('count: {}'.format(count))
#                if count >= 1000:
#                    exit()
            upload_Data = str(Path(url).parent)
            aliupload_Data = Path(aliurl).parent
#            print(1, aliupload_Data)
            # 上面两条可以取得url路径的父目录，以方便之后上传文件时拼凑路径使用
            with open('handleURL.txt','r+') as f:
                count = len(f.readlines())
                if count >= 1000:
                    exit()
                elif upload_Data.split('/')[2] == 'aliyunoss':
                    continue
                elif upload_Data not in f.read():
                    start = datetime.datetime.now()
                    s1 = psutil.net_io_counters(pernic=True)['ens160']
                    os.system('mkdir -p /offline_program_oss/%s' % (aliupload_Data))
#                    print(2, aliupload_Data)
                    os.system('/xor/data2/log/ossupload/aliupload/ossutil64 cp -rfu -j 10 --loglevel info -c /root/scripts/yaoscr/ossutilconfig %s oss://offline-program-oss%s' % (upload_Data, aliupload_Data))
                    print('upload: {}, aliupload_Data: {}'.format(upload_Data,aliupload_Data))
                    s2 = psutil.net_io_counters(pernic=True)['ens160']
                    second = (datetime.datetime.now()-start).total_seconds()
                    result = str((s2.bytes_sent-s1.bytes_sent)/1024/1024/second) + 'Mb/s'
                    f.write('{} {} {} {} {}'.format(datetime.datetime.now(),upload_Data,result,second,i))
                    logging.info('upload complete: {}'.format(movieid))

test = Lengmen()
test.upload_data()
