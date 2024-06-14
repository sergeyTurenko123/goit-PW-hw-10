from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quotes

# Create your views here.
def main(request):
    authors = Author.objects.all()
    return render(request, 'authorapp/index.html', {"authors": authors})


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


def detail(request, quote_id):
    quote = get_object_or_404(Quotes, pk=quote_id)
    return render(request, 'authorapp/detail.html', {"quote": quote})

def set_done(request, quote_id):
    Quotes.objects.filter(pk=quote_id).update(done=True)
    return redirect(to='authorapp:main')

def delete_quote(request, quote_id):
    Quotes.objects.get(pk=quote_id).delete()
    return redirect(to='authorapp:main')
