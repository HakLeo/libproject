from django.shortcuts import render, get_object_or_404
from .models import Book

books = [
    {
    "title" : "1984",
     "author" : "Orwell" 
    },
    {"title" : "karamazov",
     "author" : "destl" 
    },
]


def index(request):
    query = request.GET.get('q')  # Get the search term from the query string
    if query:
        books = Book.objects.filter(title__icontains=query)  # Search by title
    else:
        books = Book.objects.all()
    return render(request, 'library\inde.html', {'books': books, 'query': query})