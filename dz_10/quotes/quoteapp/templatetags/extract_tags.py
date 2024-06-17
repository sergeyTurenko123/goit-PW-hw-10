from django import template
from ..models import Quote
from bson.objectid import ObjectId

register = template.Library()


def tags(tags_all):
    tags = [name for name in tags_all.all()]
    return tags

def quotes(tag):
    for quote in Quote.objects.all():
        if tag in quote.tags:
            return quote.quote

register.filter('tags', tags)
register.filter('tag', quotes)