from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from .forms import TagForm, QuoteForm, AuthorForm
from django.contrib.auth.decorators import login_required

def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quoteapp/index.html', context={'quotes': quotes_on_page})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})

@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})

@login_required
def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote=form.save(commit=False)
            author_id = request.POST.get('author')
            author = Author.objects.get(id=author_id)
            new_quote.author = author

            new_quote.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"authors": authors, "tags":tags, 'form': form})

    return render(request, 'quoteapp/quote.html', {"authors": authors, "tags":tags, 'form': QuoteForm()})

def detail_author(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quoteapp/detail_author.html', {"quote": quote})

@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quoteapp:main')

def detail_tag(request, tag):
    quotes = Quote.objects.all()
    for quote in quotes:
        for tags in quote.tags:
        # tags = [quote.name for quote in quotes.tags]
            if tag in tags.name:
                return render(request, 'quoteapp/detail_tag.html', {"quote": quotes})
                


