from django import template

register = template.Library()


@register.filter(name='zip')
def zip_filter(list1, list2):
    return zip(list1, list2)
