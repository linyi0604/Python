'''生成器 0-n的每个数字'''
def generator( n ):
    i=0

    while i<=n:
        yield i
        i+=1



gen = generator(5)


print( next(gen) )
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))





