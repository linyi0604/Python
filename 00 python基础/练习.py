'''
用至少2种方法实现Python单例（tip:__new__方法，装饰器）
'''

###################### 方法1 __new__ ###########################
# 方法1  __new__ 实现单利
class Singleton(object):
    __instance = None
    __first_init = False
    def __new__(cls, name , age):
        if not cls.__instance :
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,  name , age):
        if not self.__first_init :
            self.age = age
            self.name = name
            Singleton.__first_init = True


#后创建的 不会被实例化
s1 = Singleton("张三" ,18 )
s2 = Singleton("李四" , 20 )
print( id(s1) )
print( id(s2) )
print(s2.name)
print(s1.name)


####################################方法2  装饰器#####################################
print("-"*100)

#方法2  装饰器实现
#装饰器函数 判断是否被实例化过 如果没有则新建实例返回 否则返回原来的实例
def decoration( cls , *args , **kwargs ):
    #如果被实例化过对象了
    if cls.is_new :
        return cls.is_new
    #还没有被实例化
    else :
        return Singleton_decoration( *args , **kwargs)


@decoration     #Singleton_decoration = decoration( Singleton_decoration )
class Singleton_decoration(object):
    #标记实例化的对象
    __first_new = None
    #是否被实例化过
    @classmethod
    def is_new(cls):
        return cls.__first_new

    def __init__(self , name , age):
        self.age = age
        self.name = name
        Singleton_decoration.__first_new = self


s3 = Singleton( "王五" , 20 )
s4 = Singleton( "溜溜" , 30 )
print(id(s3))
print(id(s4))
print(s3.name)
print(s4.name)