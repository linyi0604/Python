'''
在python中导入包，实际上有一个搜索路径的问题
每当新开启一个python程序的时候，这个程序就会独立维护一个sys文件，
sys.path是一个列表文件，里面保存着一系列的路径，都是import包的搜索路径。
'''
#sys.path是一个列表，存着import 包时候搜索的路径，每一个python程序独立维护一个sys文件
import sys
print(sys.path)
'''
当我们在自己的项目中想要导入包的时候，实际上需要自己在sys.path里面添加自己写的包的目录
'''
#因为是我们自己的包，所以插入在最前面，让系统默认的放在后面
sys.path.insert(1,"../packege_a")
#这样我们就可以导入自己写的包的东西
import a
a.a()

'''
当导入包之后，包会在当前程序的缓冲区当中，
如果包内的函数发生改变后，再次import 包 的时候 python会认为已经加载过了，不会再加载
这个时候需要用到 包的重载才会重新载入包里的内容
重载： imp.reload(包)
'''
import imp
imp.reload(a) #把我们要重新导入的模块a进行重新导入
a.a()

