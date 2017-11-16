#encoding=utf-8
'''
用类来模拟一个元类  创建一个类的时候调用我们自己写的元类
'''
#我们自己写的元类
class TypeDemo( type ):
    def __new__(cls,clsName , clsFathers , clsProperty ):
        print("哈哈哈")
        #在这里我们捣乱一下，把所有的变量改成大写返回去
        new_clsProperty={}
        for key,value in clsProperty.items():
            if  key.startswith("_")  and key.endswith("_") :
                new_clsProperty[key] = value

            else :
                new_clsProperty[key.upper()] = value
        #在这里 必须要调用父类的方法帮助我们创建一个类 以下几种方式
        return type( clsName , clsFathers , new_clsProperty)
        #return type.__new__(cls, clsName , clsFathers , new_clsProperty)
        #return super().__new__( cls, clsName , clsFathers , new_clsProperty )
        #return super( TypeDemo ,cls).__new__( cls, clsName , clsFathers , new_clsProperty )



#在python3中需要在类的父类列表当中置顶metaclass属性
#指定了metaclass变量 相当于调用 TypeDemo( "Person" , (object , ) , { "name":"张三" } )
class Person( object, metaclass=TypeDemo ):
    name = "张三"
    b = 15

print(Person.B)

#在python2当中需要置顶变量__metaclass__
class Dog( object ):
    __metaclass__ = TypeDemo  # 使用我们自己写的类当作元类
    a = 100



print( hasattr(Dog , "a" ) )
print( hasattr(Dog , "A" ) )