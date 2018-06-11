from django import template

register = template.Library()


@register.filter(name='split')
def split(value):
    if value.split('.')[1] == 'mp4':
        return 'video'
    else:
        return 'image'
