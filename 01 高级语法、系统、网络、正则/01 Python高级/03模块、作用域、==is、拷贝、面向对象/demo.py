import sys

if __name__ == '__main__':
    sys.path.insert(0, ".\\" )

    file_path = sys.path
    for i in file_path:
        print(i)
'''
执行结果：

.\
D:\Workspaces\PycharmProjects
C:\Users\Mr.Cold\AppData\Local\Programs\Python\Python35\python35.zip
C:\Users\Mr.Cold\AppData\Local\Programs\Python\Python35\DLLs
C:\Users\Mr.Cold\AppData\Local\Programs\Python\Python35\lib
C:\Users\Mr.Cold\AppData\Local\Programs\Python\Python35
C:\Users\Mr.Cold\AppData\Local\Programs\Python\Python35\lib\site-packages
'''