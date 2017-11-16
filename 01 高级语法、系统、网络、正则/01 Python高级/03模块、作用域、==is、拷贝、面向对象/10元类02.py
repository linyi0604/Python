'''
实际上当创建一个类的时候 
    首先调用这个类的 metaclass方法，如果当前类没有这个方法就调用父类的 最后追溯到type为止
我们自己实现一个元类，用这个元类创建一个类
'''
#用函数来模拟一个元类的实现
#我们自己定义 当创建person类的时候会调用metaclass指定的，我们把它的属性改成大写后创建
#里边传入3个参数  类名，父类元组，属性字典
def ourTypeclass(name,father,attributes):
    #在这里截获属性 把他们改成大写
    newAttrs = {}
    for key,value in attributes.items():
        if key.startswith("_") and key.endswith("_"):
            newAttrs[key] = value
        else :
            newAttrs[key.upper()] = value

    return type(name,father,newAttrs)


#在python3中 指定metaclass是创建一个类的引用
class Person(object,metaclass= ourTypeclass):
    name = ""
print(hasattr(Person,"name"))
print(hasattr(Person,"NAME"))

#在python2 当中 置顶metaclass属性
class Person2(object):
    __metaclass__ = ourTypeclass
    name = ""
print("在python2中需要置顶metaclass属性：")
print(hasattr(Person2 , "NAME"))
print(hasattr(Person2 , "name"))


'''
下面用一个类来实现元类
__new__() 方法是一个类最先执行的
'''
class TestTypeClass(type):
    def __new__(cls,name,father,attributes ):
        # 在这里截获属性 把他们改成大写
        newAttrs = {}
        for key, value in attributes.items():
            if key.startswith("_") and key.endswith("_"):
                newAttrs[key] = value
            else:
                newAttrs[key.upper()] = value
        return type(name, father, newAttrs)

class Person4(object,metaclass= TestTypeClass):
    name = ""
print(hasattr(Person4,"name"))
print(hasattr(Person4,"NAME"))