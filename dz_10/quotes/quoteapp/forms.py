from django.forms import ModelForm, CharField, TextInput, DateTimeField
from .models import Tag, Author, Quote

class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    
    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags', 'created_at']

class AuthorForm(ModelForm):

    fullname = CharField(max_length=50)
    born_date = CharField(max_length=50)
    born_location = CharField(max_length=150)
    description = TextInput()

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        exclude = ['created_at']