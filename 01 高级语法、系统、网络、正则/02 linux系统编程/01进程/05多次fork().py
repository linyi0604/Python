'''
在程序中多次调用fork()

当一个进程调用了fork() 都会生成另一个子进程 然后在这条语句向下执行

'''

import os

os.fork()  #主进程会产生一个子进程，两个进程从这里开始继续向下进行

os.fork() #两个进程到这里，分别会给自己创建一个子进程，结果 会有四个进程从这里继续向下

os.fork() # 四个进程到这里，每个进程都会给自己再创建一个子进程。结果会形成八个进程

print("哈哈哈")    #会打印出八条哈哈哈