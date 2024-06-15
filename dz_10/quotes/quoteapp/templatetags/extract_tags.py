from django import template
from ..utils import get_mongodb
from bson.objectid import ObjectId

register = template.Library()


def author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']


register.filter('author', author)

