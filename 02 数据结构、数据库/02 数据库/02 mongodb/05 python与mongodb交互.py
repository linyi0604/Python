#coding:utf8
'''
首先引入包：
    pip install pymongo

需要用到如下对象:
    MongoClient对象：用于与MongoDB服务器建立连接
        client=MongoClient('主机ip',端口)

    DataBase对象：对应着MongoDB中的数据库
        db=client.数据库名称

    Collection对象：对应着MongoDB中的集合
        col=db.集合名称

    Cursor对象：查询方法find()返回的对象，用于进行多行数据的遍历
        当调用集合对象的find()方法时，会返回Cursor对象
        结合for...in...遍历cursor对象


主要方法:
    insert_one：加入一条文档对象
    insert_many：加入多条文档对象
    find_one：查找一条文档对象
    find：查找多条文档对象
    update_one：更新一条文档对象
    update_many：更新多条文档对象
    delete_one：删除一条文档对象
    delete_many：删除多条文档对象


'''

from pymongo import *
'''
插入方法：
    insert_one() 传入一个字典，表示插入一个文档
    insert_many() 传入一个列表，列表的元素为字典，插入多条文档
'''
def insert():
    try:
        # 1 创建连接对象
        client = MongoClient(host="localhost", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.demo    # 使用demo数据库
        # 向stu集合插入数据
        # 插入一条
        db.stu.insert_one({"name": "zs", "age": 20})
        # 插入多条
        db.stu.insert_many([{"name": 1}, {"name": 2}])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    insert()



from pymongo import *
'''
查询方法：
    find_one()返回满足条件的文档集中第一条数据，类型为字典
                如果没有查询结果返回None
    方法find()返回满足条件的所有文档，类型为Cursor对象，可以使用for...in遍历，每项为字典对象
            如果没有查询结果返一个空的Cursor对象
'''
def select():
    try:
        # 1 创建连接对象
        client = MongoClient(host="localhost", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.demo    # 使用demo数据库
        # 从stu查询数据
        # 查询一条,返回一个字典，如果没有结果返回None
        res = db.stu.find_one({"age": 18})
        print(res)
        # 查询全部结果，返回一个Cursor可迭代对象，每一个元素是字典
        # 如果没有查询结果会返回一个空的Cursor对象
        res = db.stu.find({"age": {"$gt": 18}})
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    select()





from pymongo import *
'''
修改方法：
    update_one()修改满足条件的文档集中的第一条文档
    update_many()修改满足条件的文档集中的所有文档
    注意：使用$set操作符修改特定属性的值，否则会修改整个文档
'''
def update():
    try:
        # 1 创建连接对象
        client = MongoClient(host="localhost", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.demo    # 使用demo数据库
        # 修改数据
        # 修改第一条符合条件的数据，传入条件和修改结果
        db.stu.update_one({"age": 18},{"$set": {"age": 100}})  # 把年龄是18的第一条年龄改成100
        # 所有符合条件数据都修改
        # db.stu.update_many({"age": 18},{"$set": {"age": 100}}) # 年龄18的所有数据年龄改成100
    except Exception as e:
        print(e)


if __name__ == '__main__':
    update()




from pymongo import *
'''
删除方法：
    delete_one()删除满足条件的文档集中第一条文档
    delete_many()删除满足条件的所有文档
    注意：使用$set操作符修改特定属性的值，否则会修改整个文档
'''
def delete():
    try:
        # 1 创建连接对象
        client = MongoClient(host="localhost", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.demo    # 使用demo数据库
        # 修改数据
        # 修改第一条符合条件的文档删除
        db.stu.delete_one({"age": 18})  # 把年龄是18的第一条文档删除
        # 所有符合条件数据都删除
        db.stu.delete_many({"age": 18}) # 年龄18的所有文档删除
    except Exception as e:
        print(e)


if __name__ == '__main__':
    delete()



'''

案例:
    使用python向集合t3中插入1000条文档，文档的属性包括_id、name
    _id的值为0、1、2、3...999
    name的值为'py0'、'py1'...
    查询显示出_id为100的整倍数的文档，如100、200、300...，并将name输出

'''
import pymongo
if __name__ == '__main__':
    try:
        # 1 获得连接对象
        client = pymongo.MongoClient(host="localhost", port=27017)
        # 2 获取数据库
        db = client.demo
        # 3 执行业务逻辑 数据库操作
        # 插入1000条数据

        for id in range(0,1000):
            db.t3.insert_one({"_id": id, "name": "py%s"% id})

        # 取出符合条件的数据
        match = {
            "$where": "function(){return this._id%100 == 0 }",
            }
        res = db.t3.find(match, {"_id": 0, "name": 1})
        for info in res:
            print(info)


    except Exception as e:
        print(e)