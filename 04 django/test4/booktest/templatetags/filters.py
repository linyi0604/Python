from django.template import Library

register = Library()

#一个偶数为真的过滤器
@register.filter(name='odd')
def odd(num ):
    return num%2==0