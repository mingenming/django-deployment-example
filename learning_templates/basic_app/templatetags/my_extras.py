from django import template

register=template.Library()

@register.filter(name='jian')
def jian(value,arg):
    """
    this cut out all value of 'arg' from string!
    """
    return value.replace(arg,'')

# register.filter('jian',jian)
