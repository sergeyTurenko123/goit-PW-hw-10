from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from .forms import TagForm, QuoteForm

def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quoteapp/index.html', context={'quotes': quotes_on_page})

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})

def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote=form.save(commit=False)

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            author_id = request.POST.get('author')
            author = Author.objects.get(id=author_id)
            new_quote.author = author

            new_quote.save()

            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, "authors":authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors":authors, 'form': QuoteForm()})
