from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quotes


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    description = CharField(min_length=3, required=True, widget=TextInput())
    
    class Meta:
        model = Author
        fields = ['fullname','born_date','born_location','description']

class QuoteForm(ModelForm):

    tags = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    quote = CharField(min_length=10, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Quotes
        fields = ['tags', 'quote']
        exclude = ['author']

