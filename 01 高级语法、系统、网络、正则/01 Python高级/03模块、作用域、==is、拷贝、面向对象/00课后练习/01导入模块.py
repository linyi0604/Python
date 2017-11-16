'''
每一个启动的python程序都独立维护一个sys文件，sys.path是一个列表，里面依次存着工程导入包的时候搜寻包的路径
'''
import sys
print(sys.path)
'''
如果我们自己写的包没有发布到系统当中，就需要和执行的文件放在同级目录，否则导入会搜索不到路径
这个时候需要我们自己向sys.path当中添加路径
'''
sys.path.insert(1,"../01模块导入/")
import packege_a.a
packege_a.a.a()

'''
如果python已经运行，此时修改包内的内容，python已经加载过包，所以文件内不会看到变化。
即使再次import 包，也是python认为已经导入过，所以实际不会导入
我们此时需要用imp.reload() 对包进行重载
'''
import imp
imp.reload(packege_a.a)
packege_a.a.a()
