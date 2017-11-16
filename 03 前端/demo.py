#coding:utf8
def outer(x):
    def inner(y):
        nonlocal x
        x+=y
        return x
    return inner


a = outer(10)
print(a(1))
print(a(3))











