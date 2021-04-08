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
# 下面为第一版删除邮件的代码，基本可以工作了
import imaplib, email
import threading
import time

# 这个脚本的问题是需要查看 windows 主机上对邮箱 143 端口的连接数，一般连接数达到 5 个时，运行脚本时就会报错，需要在 windows 上杀死这些连接才能再运行这个脚本
# imaplib 模块的使用可以到官网查看，地址：https://www.docs4dev.com/docs/zh/python/3.7.2rc1/all/library-imaplib.html#toolbar-title

def DeletMail(mailAddr=None):
    print(mailAddr)
    with imaplib.IMAP4('mail.xor-media.tv',143) as mail: # IMAP4 支持 with 方法，参数是收件服务器地址
        mail.login("zheng.yao@xor-media.tv","ruopu8964") # 登录用户信息
        mail.select() # 不执行 select() 方法是不能执行 search() 方法的，会报错
        typ, data = mail.search(None, 'from', mailAddr) # typ 感觉用处不大，一般都是 OK。data 是一个列表，列表中是 b''，
#        print(f"data: {data}, data[0]: {data[0]}, data[0].split: {data[0].split()}") 
        print(f"data: {data}, count: {len(data[0].split())}") # 因为列表中只有一个 b''，所以要用 data[0]来取值，用 split() 把 b'' 中的字符以空格分开，空格是 split() 指定的默认分隔符 
    # data: [b'239 247 288 296 322 328 369 373 378 387'], data[0]: b'239 247 288 296 322 328 369 373 378 387', data[0].split: [b'239', b'247', b'288', b'296', b'322', b'328', b'369', b'373', b'378', b'387']
    # 将字符串按照分隔符分割成若干字符串，并返回列表。缺省的情况下空白字符串作为分隔符
        for num in data[0].split():
            mail.store(num, '+FLAGS', '\\Deleted') # 删除邮件，xor 公司的邮箱这样操作后就直接删除了，hotmail  会把邮件放到垃圾箱中
        mail.expunge() # 永久删除所选邮箱中的已删除邮件。
        mail.close() # 关闭当前选择的邮箱。删除的邮件将从可写邮箱中删除。这是LOGOUT之前的推荐命令。感觉在退出前用 close() 方法可以关闭端口，也许吧。

mailAddress = [
    'Linux_SSS_Logs_Monitor@mail.ghtech.net.cn',
    'ADI_Import_Expection@mail.ghtech.net.cn',
    'AquaPaaS_Logs_Monitor@mail.ghtech.net.cn',
    'ADI_Import_Expection@mail.ghtech.net.cn',
    'A_SSS@xor-media.tv',
    '年华报表@mail.ghtech.net.cn'.encode(encoding="utf-8"), # 因为有中文，所以要用 encode 方法，不然会报错
    'monitor_center@mail.ghtech.net.cn',
    'ETL_monitor@mail.ghtech.net.cn',
    'CDNH_GEHU@xor-media.tv',
    'Linux_SSS_Service@mail.ghtech.net.cn',
    'AquaPaaS_Exception@mail.ghtech.net.cn',
    'zhaoqi1@bgctv.com.cn',
    'tao.liu@xor-media.tv',
    'yuanchen@bgctv.com.cn',
    'jie.guo@xor-media.tv',
    'chenlei@bgctv.com.cn',
    'shuming.li@xor-media.tv',
    'zhangyanjia@bgctv.com.cn',
    'zach.zhu@xor-media.tv',
    'zhengli@bgctv.com.cn',
    'chao.han@xor-media.tv',
    'chailijun@bgctv.com.cn',
    'xiangxue.jing@xor-media.tv',
    'wujian@bgctv.com.cn',
    'shun.liu@xor-media.tv',
    'monitor@monitor.aliyun.com',
    'system@notice.aliyun.com',
    'caoyun.gao@xor-media.tv',
    'yun.gu@xor-media.tv',
    'zhangtong@bgctv.com.cn',
    'CTVIT_OTT01@163.com',
    'yangweidong@bjdgwa.com',
    'gamzeh84@mcsorley.org.uk',
    'lonnie3bonner@hankins.us',
    'zhangtong@bgctv.com.cn',
    'ziwei.zhang@xor-media.tv'
]

#def createmailA(): 
#    for mailA in mailAddress:
#        yield mailA

#for i in createmailA():
#    print(i)
for mailA in mailAddress:
    f = DeletMail(mailA)
    if f: # 对于 xor 公司邮箱来说，直接运行循环语句会报错，可能是连接数太多了，所以这里需要判断一下，如果上一个 DeletMail 函数执行完成了，再执行下一个 DeletMail 函数
        DeletMail(mailA)
#    time.sleep(60)
#DeletMail()
#    print(mailA)
#lst = []

#for mailA in mailAddress:
#    t = threading.Thread(target=DeletMail,args=(mailA,))
#    t.start()
#    lst.append(t)

#for t in lst:
#    t.join()


# vim 的配置文件，.vimrc
# "Vundle
# "去除VI一致性
# set nocompatible
# filetype off
# "设置Vundle的运行路径
# set rtp+=~/.vim/bundle/Vundle.vim
# "设置插件的安装路径,vundle插件起始标志
# call vundle#begin()
# "让vundle管理插件版本
# Plugin 'VundleVim/Vundle.vim'
# "设置插件的安装路径,vundle插件结束标志
# call vundle#end()
# "加载vim自带和插件相应的语法和文件类型相关脚本
# filetype plugin indent on

# set encoding=utf-8 "设置utf-8编码
# "set number "显示行号
# syntax on "开启语法高亮
# set background=dark "设置背景色
# set showmatch "显示匹配的括号
# set backspace=2 "可以删除任意值
# set scrolloff=5 "距离顶部和底部5行
# set laststatus=2 "命令行为两行
# set fenc=utf-8 "文件编码

# "Python
# set filetype=python
# au BufNewFile,BufRead .py,.pyw setf python
# set autoindent "设置自动缩进
# set smartindent "自动下一行缩进
# "set textwidth=99 "行最大宽度
# set expandtab "tab替换为空格键
# set tabstop=4 "设置table长度
# set softtabstop=4 "软制表符宽度为4
# set shiftwidth=4 "设置缩进的空格数为4
# set fileformat=unix "设置以unix的格式保存文件

# "vim中F5直接调试
# map <F5> :call RunPython()<CR>
# func! RunPython()
# exec "w"
# if &filetype == 'python' "第一行#!/bin/python 运行python编译器
# exec "!time python %"
# elseif &filetype == 'sh' "第一行#!/bin/bash 运行shell编译器
# :!time bash %
# endif
# endfunc


# "-------------------------- 插件 ------------------------

# "添加nerdtree
# Bundle 'scrooloose/nerdtree'
# "设置按F2启动NerdTree
# map <F2> :NERDTreeToggle<CR>
# "隐藏目录树中的.pyc文件
# let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree


# "添加YouCompleteMe代码补全插件
# Plugin 'Valloric/YouCompleteMe'
# let g:ycm_server_python_interpreter='/usr/bin/python'
# let g:ycm_global_ycm_extra_conf='~/.vim/.ycm_extra_conf.py'
# "youcompleteme  默认tab  s-tab 和自动补全冲突
# "let g:ycm_key_list_select_completion=['<c-n>']
# "let g:ycm_key_list_select_completion = ['<Down>']
# "let g:ycm_key_list_previous_completion=['<c-p>']
# "let g:ycm_key_list_previous_completion = ['<Up>']
# ""关闭加载.ycm_extra_conf.py提示
# let g:ycm_confirm_extra_conf=0
# " 开启 YCM 基于标签引擎
# let g:ycm_collect_identifiers_from_tags_files=1
# " " 从第2个键入字符就开始罗列匹配项
# let g:ycm_min_num_of_chars_for_completion=2
# " " 禁止缓存匹配项,每次都重新生成匹配项
# let g:ycm_cache_omnifunc=0
# " " 语法关键字补全
# let g:ycm_seed_identifiers_with_syntax=1
# " "force recomile with syntastic
# nnoremap <F5> :YcmForceCompileAndDiagnostics<CR>
# " "nnoremap <leader>lo :lopen<CR> "open locationlist
# " "nnoremap <leader>lc :lclose<CR>    "close locationlist
# inoremap <leader><leader> <C-x><C-o>
# " "在注释输入中也能补全
# let g:ycm_complete_in_comments = 1
# " "在字符串输入中也能补全
# let g:ycm_complete_in_strings = 1
# " "注释和字符串中的文字也会被收入补全
# let g:ycm_collect_identifiers_from_comments_and_strings = 0

# "python语法检测
# Plugin 'scrooloose/syntastic'
# "添加PEP8代码风格检查
# Plugin 'nvie/vim-flake8'

# "代码折叠插件
# Plugin 'tmhedberg/SimpylFold'
# "开启代码折叠
# set foldmethod=indent
# set foldlevel=99
# ""设置快捷键为空格
# noremap <space> za
# "显示折叠代码的文档字符串
# let g:SimpylFold_docstring_preview=1

# "AI 补全， 基于YouCompleteMe"
# Plugin 'zxqfl/tabnine-vim'