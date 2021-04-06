# import imaplib, email

# def DeletMail(mailpath):
#     with imaplib.IMAP4_SSL('outlook.office365.com',993) as mail:

#     # mail = imaplib.IMAP4_SSL('outlook.office365.com',993)
#         mail.login("ruopu1989@hotmail.com","X5!")
#         # print(mail.select())
#         # print(mail.list())
#         # print(mail.select('Inbox'))
#         mail.select() # 不执行 select() 方法是不能执行 search() 方法的，会报错
#         typ, data = mail.search(None, 'from', 'ruopu1989@hotmail.com')
#     # print(typ)
#         print(f"data: {data}, data[0]: {data[0]}, data[0].split: {data[0].split()}") 
#     # data: [b'239 247 288 296 322 328 369 373 378 387'], data[0]: b'239 247 288 296 322 328 369 373 378 387', data[0].split: [b'239', b'247', b'288', b'296', b'322', b'328', b'369', b'373', b'378', b'387']
#     # 将字符串按照分隔符分割成若干字符串，并返回列表。缺省的情况下空白字符串作为分隔符
#         for num in data[0].split(): # num 是邮件的编号 ？？？
#             # typ, data = mail.fetch(num, '(onlinetransactions)')
#             # print(num)
#             # print('Message %s\n%s\n' % (num, data[0][1]))
#             mail.store(num, '+FLAGS', '\\Deleted')
#         mail.expunge()
    
# mail.close()
# mail.logout()
    
# mail = imaplib.IMAP4('mail.xor-media.tv',143)
# mail.login("zheng.yao@xor-media.tv","ruopu8964")
# mail.select()
# result, data = mail.uid('search',None, "ALL")
# uidlist = data[0].split()
# newUidList = processEmails(uidList)
# typ, data = mail.search(None, 'from', 'Linux_SSS_Logs_Monitor@mail.ghtech.net.cn')
# print(typ)
# box.expunge()
# typ, data = box.search(None,'ALL')
# for num in data[0].split():
#     typ, data = box.fetch(num,'UID BODY[TEXT]')
#     print(num)
#     print(data[0][1])
# mail.close()
# mail.logout()
# =========================================================
# test = '/abcdef\\a/\\//'
# cur = test.rstrip('/\\')
# print(cur)
# =============================================================
# class AttrDict:
#     def __init__(self, d:dict):
#         self.__dict__.update(d if isinstance(d, dict) else {})

#     def __setattr__(self, key, value):
#         # 不允许修改属性
#         raise NotImplementedError

#     def __repr__(self):
#         return "<AttrDict {}>".format(self.__dict__)

#     def __len__(self):
#         return len(self.__dict__)

# d = {'a':1, 'b':2}
# test = AttrDict(d)
# # print(test.__dict__)
# print(test.a)
# # test.b = 3
# print(test.b)




    # "code-runner.executorMap": {
    #     "bash" : "\"D:\\Git\\bin\\bash.exe\""
    # },
    # "code-runner.languageIdToFileExtensionMap": {

    #     "bat": ".bat",
    #     "powershell": ".ps1",
    #     "typescript": ".ts",
    #     "bash": ".sh",
    #     "/bin/bash": ".sh"
    # },
    # "code-runner.runInTerminal": true

    # "terminal.integrated.shell.windows": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",

# 最上面的代码是删除邮件的测试代码
import imaplib, email
import threading

def DeletMail(mailAddr):
    with imaplib.IMAP4('mail.xor-media.tv',143) as mail:
        mail.login("zheng.yao@xor-media.tv","ruopu8964")
        mail.select() # 不执行 select() 方法是不能执行 search() 方法的，会报错
        typ, data = mail.search(None, 'from', mailAddr)
        print(f"data: {data}, data[0]: {data[0]}, data[0].split: {data[0].split()}") 
    # data: [b'239 247 288 296 322 328 369 373 378 387'], data[0]: b'239 247 288 296 322 328 369 373 378 387', data[0].split: [b'239', b'247', b'288', b'296', b'322', b'328', b'369', b'373', b'378', b'387']
    # 将字符串按照分隔符分割成若干字符串，并返回列表。缺省的情况下空白字符串作为分隔符
        for num in data[0].split():
            mail.store(num, '+FLAGS', '\\Deleted')
        mail.expunge()
        mail.close()

mailAddress = [
    'Linux_SSS_Logs_Monitor@mail.ghtech.net.cn',
    'ADI_Import_Expection@mail.ghtech.net.cn',
    'AquaPaaS_Logs_Monitor@mail.ghtech.net.cn',
    'ADI_Import_Expection@mail.ghtech.net.cn',
    'A_SSS@xor-media.tv'
]

for mailA in mailAddress:
    DeletMail(mailA)
# lst = []

# for mailA in mailAddress:
#     t = threading.Thread(target=DeletMail,args=(mailA,))
#     t.start()
#     lst.append(t)

# for t in lst:
#     t.join()