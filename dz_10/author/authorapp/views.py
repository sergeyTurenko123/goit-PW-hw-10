from django.shortcuts import render, redirect
from .forms import AuthorForm, QuoteForm
from .models import Author, Quotes

# Create your views here.
def main(request):
    return render(request, 'authorapp/index.html')

def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='authorapp:main')
        else:
            return render(request, 'authorapp/author.html', {'form': form})

    return render(request, 'authorapp/author.html', {'form': AuthorForm()})

def quote(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_author = form.save()

            choice_authors = Author.objects.filter(name__in=request.POST.getlist('author'))
            for author in choice_authors.iterator():
                new_author.authors.add(author)

            return redirect(to='authorapp:main')
        else:
            return render(request, 'authorapp/quote.html', {"authors": authors, 'form': form})

    return render(request, 'authorapp/quote.html', {"autors": authors, 'form': QuoteForm()})
