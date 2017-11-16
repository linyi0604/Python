'''
实际上 子进程和父进程会复制同一份代码，所以各自拥有各自的代码互不影响
'''
import os
from time import sleep
num = 100
pid = os.fork()
#子进程当中
if pid == 0 :
    print("这里是子进程：")
    print(num)
    num = 10
    print( num )
#主进程中
else:
    print("这里是主进程+    sleep(3)")
    print( num )
