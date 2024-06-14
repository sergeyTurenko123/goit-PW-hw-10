from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quotes

# Create your views here.
def main(request):
    quotes = Quotes.objects.all()
    return render(request, 'authorapp/index.html', {"quotes": quotes})


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='authorapp:main')
        else:
            return render(request, 'authorapp/author.html', {'form': form})

    return render(request, 'authorapp/author.html', {'form': AuthorForm()})

def quotes(request):
    authors =  Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_author = Author.objects.filter(fullname__in=request.POST.getlist('authors'))
            for author in choice_author.iterator():
                new_note.author.add(author)

            return redirect(to='authorapp:main')
        else:
            return render(request, 'authorapp/quotes.html', {"authors": authors, 'form': form})

    return render(request, 'authorapp/quotes.html', {"authors": authors, 'form': QuoteForm()})


def detail_quote(request, quote_id):
    quote = get_object_or_404(Quotes, pk=quote_id)
    return render(request, 'authorapp/detail_quote.html', {"quote": quote})

def detail_author(request, quote_id):
    author = get_object_or_404(Quotes, pk=quote_id)
    return render(request, 'authorapp/detail_author.html', {"fullname": author})

def set_done(request, quote_id):
    Quotes.objects.filter(pk=quote_id).update(done=True)
    return redirect(to='authorapp:main')

def delete_author(request, author_id):
    Author.objects.get(pk=author_id).delete()
    return redirect(to='authorapp:main')
