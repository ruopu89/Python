# import imaplib, email

# mail = imaplib.IMAP4('mail.xor-media.tv',143)
# mail.login("zheng.yao@xor-media.tv","ruopu8964")
# mail.select()
# # result, data = mail.uid('search',None, "ALL")
# # uidlist = data[0].split()
# # newUidList = processEmails(uidList)
# # typ, data = mail.search(None, 'from', 'Linux_SSS_Logs_Monitor@mail.ghtech.net.cn')
# # print(typ)
# # box.expunge()
# # typ, data = box.search(None,'ALL')
# # for num in data[0].split():
# #     typ, data = box.fetch(num,'UID BODY[TEXT]')
# #     print(num)
# #     print(data[0][1])
# mail.close()
# mail.logout()
# =========================================================
# test = '/abcdef\\a/\\//'
# cur = test.rstrip('/\\')
# print(cur)
# =============================================================
class AttrDict:
    def __init__(self, d:dict):
        self.__dict__.update(d if isinstance(d, dict) else {})

    def __setattr__(self, key, value):
        # 不允许修改属性
        raise NotImplementedError

    def __repr__(self):
        return "<AttrDict {}>".format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

d = {'a':1, 'b':2}
test = AttrDict(d)
# print(test.__dict__)
print(test.a)
# test.b = 3
print(test.b)




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