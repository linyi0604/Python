#coding:utf8
import redis
def redis_database():
    try:
        # 1 创建连接对象
        sr = redis.StrictRedis()
        # 2 调用string方法完成数据的增删改差
        # 增加和修改都用这个操作，如果name已经存在则是更新 否则是增加
        sr.set("name","小王")
        res = sr.get("name")
        print(res)
        # 删除 按照键删除
        sr.delete("name")
    except Exception as e:
        print(e)
