from django import template

register= template.Library() #固定名字


@register.filter
def fil(v1):
    s=v1+'asd'
    return s

@register.filter
def fils(v1,v2):
    s=v1+v2
    return s


@register.simple_tag()
def xmltag(v1,v2,v3):

    s=v1+'xml'+v2+v3
    return s

@register.inclusion_tag('inclusiontags.html')#python版组件
def func(l):

    return {'data':l}#相当于render传参渲染html