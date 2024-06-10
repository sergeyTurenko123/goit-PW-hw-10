from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quotes

# Create your views here.
def main(request):
    notes = Author.objects.all()
    return render(request, 'authorapp/index.html', {"author": author})


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
    fullname = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_author = Quotes.objects.filter(name__in=request.POST.getlist('author'))
            for author in choice_author.iterator():
                new_note.tags.add(author)

            return redirect(to='authorapp:main')
        else:
            return render(request, 'authorapp/quote.html', {"author": fullname, 'form': form})

    return render(request, 'authorapp/quote.html', {"author": fullname, 'form': QuoteForm()})


def detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'authorapp/detail.html', {"author": author})

# def set_done(request, author_id):
#     Author.objects.filter(pk=author_id).update(done=True)
#     return redirect(to='authorapp:main')

# def delete_note(request, author_id):
#     Author.objects.get(pk=author_id).delete()
#     return redirect(to='authorapp:main')

