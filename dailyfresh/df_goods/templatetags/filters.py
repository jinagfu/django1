#coding=utf-8
#引入注册对象
from django.template import Library
register=Library()

#使用装饰器进行注册
@register.filter
#定义求乘积函数，将value * -1
def multi(value):
    return int(value)*-1


