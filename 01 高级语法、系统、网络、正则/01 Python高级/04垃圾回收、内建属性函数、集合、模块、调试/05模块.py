'''
builtins 内建模块
os 操作系统接口
sys python自身运行工具
functools 常用工具
json 编码和解码
loggiing 记录日志 调试
multiprocessing 多进程
threading 多线程
copy 拷贝
time 时间
datetime 日期和时间
calendar 日历
hashlib 加密算法
re 正则
random 生成随机数
socket 标准bsd sockets api
shutil 文件和目录管理
glob 文件通配符搜索

'''
'''
hashlib 加密的应用
'''
import hashlib
password = "123456"
#将字符串转换为字节码
encod_password = password.encode("utf-8")
print(encod_password)
#加密算法加密
pass_hash = hashlib.sha256(encod_password)
print(pass_hash)
#获取hash加密后的密文
print( pass_hash.hexdigest() )
