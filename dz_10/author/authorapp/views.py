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
    fullname =  Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_author = Author.objects.filter(fullname__in=request.POST.getlist('fullname'))
            for author in choice_author.iterator():
                new_note.fullname.add(author)

            return redirect(to='authorapp:main')
        else:
            return render(request, 'authorapp/quotes.html', {"authors": fullname, 'form': form})

    return render(request, 'authorapp/quotes.html', {"authors": fullname, 'form': QuoteForm()})


def detail(request, quotes_id):
    quote = get_object_or_404(Quotes, pk=quotes_id)
    return render(request, 'authorapp/detail.html', {"quote": quote})
