# coding:utf8
'''
python中连接mysql数据库和简单的操作

在linux系统当中，需要下载python的连接mysql第三方工具包pymysql
终端执行： sudo pip install pymysql


python连接mysql连接步骤如下:
    1 获取连接数据库的对象conn
    2 获取操作数据库的对象cursor
    3 执行sql语句，返回语句影响的行数
    4a (查询语句)获得查询结果
    4b (非查询语句)commit提交事物
    5 关闭操作对象cursor和连接对象conn


Connection 连接对象,用于连接数据库。
    conn = pymysql.connect(参数列表):
        获取一个建立数据库链接的对象
        参数:
            host: 连接mysql主机 如果是本机就用 localhost
            port: 连接mysql主机的端口 默认是3306
            database: 数据库名称
            user: 用户名
            password: 密码
            charset: 通信采用的编码方式 推荐utf8
    conn对象方法：
        close() 关闭连接
        commit() 提交
        rollback() 回滚
        cursor() 返回cursor对象 执行sql语句


Cursor 对象:用于执行sql语句。
    获取cursor对象:
        cs = conn.cursor()
    cursor对象方法:
        close() 关闭
        execute( operation [,paramiters] ) 执行语句 返回受影响的行数
            主要用于执行insert update delete，也可以执行create alter drop
        fetchone() 获取查询结果集的第一个行数据，返回一个元组
        fetchall() 获取查询结果所有行的元组，每行一个元组
    cursor对象属性:
        rowcount 只读属性，最近一次execute()受影响的行数
        connection 获取当前连接对象

'''

'''
python对数据库的增删改操作:
'''
'''
import pymysql
# 数据库的增删改
# 增删改都术语更新语句，使用connection默认为我们开启了事务，对表的修改需要我们自己提交事务

# 增删改操作


def do_sql():
    # 数据库属于连接外部的操作，如果通讯状态不好或者sql语句有错误 会抛出异常
    try:
        # 1 获得一个数据库的连接对象
        # 传入 主机、mysql的端口、登陆mysql的用户名、密码、使用的数据库、通信的字符集类型
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="demo", charset="utf8")

        # 2 获得一个执行操作的cursor对象
        cs = conn.cursor()

        # 3 编写sql语句并执行
        insert_sql = " insert into classes (id,name) values (5,'哈哈哈') ;"  #插入操作
        update_sql = " update classes set name='嘻嘻嘻' where id = 5 ;" #修改操作
        delete_sql = " delete from classes where id = 5"    # 删除操作
        # 传入要执行的sql语句，返回一个整数这条sql语句影响的行数
        count = cs.execute(insert_sql)
        print(count)  # 打印大于0 说明刚刚sql执行成功，如果count是0说明刚刚sql语句执行失败了

        # 4 提交事务 connection自动帮我们添加了事务
        conn.commit()
        # 5 关闭cursor 和 connection对象
        cs.close()
        conn.close()
    # 如果抛出异常,就我们捕获一下
    except Exception as e:
        print(e)

if __name__ == '__main__':
    do_sql()

'''

'''
查询分为返回一行和多行的情况，需要用不同的函数获取查询结果
cursor.fetchone() 获取一行查询结果的元组，如果没有查询结果返回None
cursor.fetchall() 获取多行查询结果的元组，元组内每个元组是行结果，如果没有查询结果返回空元组()
'''
'''
# 查询操作 
import pymysql
def insert():
    # 数据库属于连接外部的操作，如果通讯状态不好或者sql语句有错误 会抛出异常
    try:
        # 1 获得一个数据库的连接对象
        # 传入 主机、mysql的端口、登陆mysql的用户名、密码、使用的数据库、通信的字符集类型
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="demo",charset="utf8")

        # 2 获得一个执行操作的cursor对象
        cs = conn.cursor()

        # 3 编写sql语句并执行

        # 一条查询结果
        select_one = "select id,name from classes where id = 3 ; "
        # 传入要执行的sql语句，返回一个整数这条sql语句影响的行数
        count = cs.execute(select_one)  # 只有一条查询结果 所以count是1，如果id不存在也可能是0
        print(count)  # 打印查询到多少条结果
        # 用fetchone()方法能够获取上次操作得到的一条查询结果的元组，如果没有结果返回None
        res = cs.fetchone()
        print(res)  # 打印一下查询结果

        # 多条查询结果
        select_all = "select id,name from classes where 1=1 ; "
        count = cs.execute(select_all)  # 查询多条数据，返回大于1的数据
        print(count)  # 打印查询到多少条结果
        # 用fetchall()方法能够获取上次操作得到的所有查询结果的元组，元组内每一行结果都是一个小元组，如果没有结果返回空元组()
        res = cs.fetchall()
        print(res)  # 打印一下查询结果

        # 4 查询数据不设计修改数据库内容，所以不需要提交事务
        # conn.commit()

        # 5 关闭cursor 和 connection对象
        cs.close()
        conn.close()
    # 如果抛出异常,就我们捕获一下
    except Exception as e:
        print(e)

if __name__ == '__main__':
    insert()

'''

'''
参数化执行sql语句，防止sql注入:
    通常我们需要制定字段或者制定值进行一些sql操作。我们可以把想要变化的字段或者值设置一个参数
    cursor.execute(sql语句[,参数列表]) 可以传入一个参数的列表，列表元素是要传入的参数，参数位置相对应用%s在sql语句中占位 
    使用这种方式，不仅实现了参数变化，而且execute方法会帮助我们匹配是否有sql注入，并不执行sql注入的语句。
'''
# 参数化执行sql语句
import pymysql
def insert(name):
    # 数据库属于连接外部的操作，如果通讯状态不好或者sql语句有错误 会抛出异常
    try:
        # 1 获得一个数据库的连接对象
        # 传入 主机、mysql的端口、登陆mysql的用户名、密码、使用的数据库、通信的字符集类型
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="demo",
                               charset="utf8")

        # 2 获得一个执行操作的cursor对象
        cs = conn.cursor()

        # 3 编写sql语句并执行
        insert_sql = " insert into classes (name) values (%s) ;"  # 插入操作
        params = [name]
        # 传入要执行的sql语句，返回一个整数这条sql语句影响的行数
        # 传入的参数在列表中位置一一对应的在sql语句中用%s占位
        # execute帮助我们实现参数一一位置对应放入sql语句，并且帮我们检测sql注入
        count = cs.execute(insert_sql, params)
        print(count)  # 打印大于0 说明刚刚sql执行成功，如果count是0说明刚刚sql语句执行失败了

        # 4 提交事务 connection自动帮我们添加了事务
        conn.commit()
        # 5 关闭cursor 和 connection对象
        cs.close()
        conn.close()
    # 如果抛出异常,就我们捕获一下
    except Exception as e:
        print(e)


if __name__ == '__main__':
    name = input("请输入要插入的班级名称:")
    insert(name)  # 指定值的插入数据
