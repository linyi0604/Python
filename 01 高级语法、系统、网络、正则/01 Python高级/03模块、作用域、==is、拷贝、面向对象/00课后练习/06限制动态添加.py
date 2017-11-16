'''
python动态语言的特性 允许随意添加变量和方法
    为了限制这种情况，设置__slots__变量(插槽)，是一个元组，里面写上变量名，这样在添加其他变量的时候就会失败

'''
class Person(object):
    __slots__=("name","age")

p = Person()

p.name="哈哈"
p.age=23
print(p.name)
print(p.age)
#p.height = 175 #会报异常，不允许添加这个属性