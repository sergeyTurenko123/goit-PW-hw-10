from django import template

register = template.Library()


def fullname(quote_tags):
    return ','.join([str(name) for name in quote_tags.all()])


register.filter('author', fullname)

