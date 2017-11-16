# coding:utf8

'''
首先安装包
    pip install redis


StrictRedis对象方法：
    通过init创建对象，指定参数host、port与指定的服务器和端口连接，host默认为localhost，port默认为6379
    根据不同的类型，拥有不同的实例方法可以调用，与前面学的redis命令对应，方法需要的参数与命令的参数一致

string
    set     set key value   增加或者修改键值对
    setex   setex key value seconds 增加修改键值对 添加过期时间
    mset    mset key1 value1 key2 value2...     添加多个键值对
    append  append key value    向key的值后面追加value字符串
    get     get key     获取key的值
    mget    mget key1 key2 key3 获取多个键的值

key
    keys    keys * 利用通配符查询键
    exists  exists key 查询键是否存在
    type    type key 查询key对应value的类型
    delete  delete key 删除键值对
    expire  expire key seconds 为key添加过期时间
    getrange
    ttl     ttl key  查看键值对的过期时间   -2 代表已经过期

hash
    hset    hset key field value    为键设置属性和属性值
    hmset   hmset key field1 value1 field2 value2 ...   为键设置多个属性和属性值
    hkeys   hkeys key   查看键所有的属性名称
    hget    hget key field  获取键的某个属性的属性值
    hmget   hmget key field1 field2 ... 获取键的多个属性的值
    hvals   hvals key   查询键所有的属性值
    hdel    hdel key field  删除键的某个属性和属性值

list
    lpush   lpush key value 向键从左侧插入元素
    rpush   rpush key value 向键从右侧插入元素
    linsert linsert key after/before value newvalue 向键的谋值前或者后插入一个新的值
    lrange  lrange key start end    对键进行按照下表查询，start从0开始 end是-1代表最后一个元素
    lset    lset key index value    按照下标修改列表对应位置的值
    lrem    lrem count value  搜索前count个位置 出现value的值全都删除，value<0代表从后向前

set
    sadd     sadd key value1 value2 ... 向键内添加元素
    smembers smembers key   获取键对应集合内所有元素
    srem     srem key value 删除键对应集合内某个值

zset
    zadd    zadd key score1 value1 score value2 ... 向键对应集合内 添加权重对应值
    zrange  zrange start end 按照下标进行查询，start从0开始 end -1代表最后一个元素
    zrangebyscore   zrangebyscore min max 查询权值从min到max
    zscore  zscore  key value 查询key对应集合内value的权值
    zrem    zrem key value 删除指定元素
    zremrangebyscore    zremrangebyscore key min max 将权值从min到max的值删除

'''
'''
string类型的增加、修改方法：
    set key value 添加键值，如果键已经存在 则修改键的值
        如果成功返回true 否则返回false
'''
# from redis import *
# if __name__ == '__main__':
#     try:
#         # 1 获取StricRedis对象 传入主机和端口，省略默认是本地主机和默认端口
#         sr = StrictRedis(host="localhost",port="6379")
#         # 2 业务逻辑 添加键值对 如果存在就修改，返回是否执行成功 成功返回true 否则返回false
#         res = sr.set("py1","gj")
#         # 3 提示执行借诶过
#         print(res)
#     except Exception as e:
#         print(e)


'''
string获取方法：
    get key 获取键对应的值，如果键存在则返回对应的值，如果键不存在则返回None
'''
# from redis import *
# if __name__ == '__main__':
#     try:
#         # 1 获取StricRedis对象 传入主机和端口，省略默认是本地主机和默认端口
#         sr = StrictRedis()
#         # 2 业务逻辑 获取
#         res = sr.get("py1")
#         # 3 提示获取到的结果
#         print(res.decode())
#
#     except Exception as e:
#         print(e);

'''
string类型数据的删除
    delete key  删除键值对 返回受影响的行数。没有删除则返回0
'''
# import redis
# if __name__ == '__main__':
#     try:
#         # 1 获取StricRedis对象 传入主机和端口，省略默认是本地主机和默认端口
#         rs = redis.StrictRedis()
#         # 2 业务逻辑 删除键值对,返回删除了数据的条数
#         res = rs.delete("py1")
#         # 3 打印执行结果
#         print(res)
#
#     except Exception as e:
#         print(e)


'''
获取键：
    keys * 利用通配符查询符合规则的键名 返回列表
        如果没有查询结果返回空列表

'''
import redis

if __name__ == '__main__':
    try:
        # 1 获取StricRedis对象 传入主机和端口，省略默认是本地主机和默认端口
        sr = redis.StrictRedis()
        # 2 业务逻辑 查询所有的键名 返回一个列表
        res = sr.keys("*")
        # 3 操作返回结果
        print(res)

    except Exception as e:
        print(e)
