from django.db import models

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=50, null=False)
    born_location = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"{self.fullname}"

class Quotes(models.Model):
    tags = models.CharField(max_length=25, null=False, unique=True)
    author = models.ManyToManyField(Author)
    quote = models.CharField(max_length=150, null=False)

    def __str__(self):
        return f"{self.tags}"