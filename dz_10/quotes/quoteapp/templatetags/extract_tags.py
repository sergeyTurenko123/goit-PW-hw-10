from django import template
from ..models import Author
from bson.objectid import ObjectId

register = template.Library()


def tags(tags_all):
    tags = [name for name in tags_all.all()]
    return tags

register.filter('tags', tags)
