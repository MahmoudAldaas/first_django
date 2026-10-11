# library/views.py — View functions handle requests and return responses
from django.shortcuts import render
from django.http import Http404

# ───── Hard-coded book data (no database needed) ─────
BOOKS = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year': 1960,
        'description': 'A novel about racial injustice in the Deep South.',
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'year': 1949,
        'description': 'A dystopian novel about totalitarianism and surveillance.',
    },
    {
        'id': 3,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'year': 1925,
        'description': 'A story of wealth, love, and the American Dream in the Jazz Age.',
    },
]


def home(request):
    """Home page — shows a welcome message and total book count."""
    context = {
        'total_books': len(BOOKS),  # Pass data to the template via "context"
    }
    return render(request, 'home.html', context)


def books(request):
    """Books list page — shows all books."""
    context = {
        'books': BOOKS,  # The template will loop over this list
    }
    return render(request, 'books.html', context)


def dashboard(request):
    """Dashboard page — shows library statistics."""
    # Calculate some simple stats
    authors = set(book['author'] for book in BOOKS)
    context = {
        'total_books': len(BOOKS),
        'total_authors': len(authors),
        'newest_book': max(BOOKS, key=lambda b: b['year']),
        'oldest_book': min(BOOKS, key=lambda b: b['year']),
    }
    return render(request, 'dashboard.html', context)


def book_detail(request, id):
    """Single book detail page — finds a book by its id."""
    # Search for the book with the matching id
    book = None
    for b in BOOKS:
        if b['id'] == id:
            book = b
            break

    # If no book was found, return a 404 error
    if book is None:
        raise Http404(f"Book with id {id} does not exist.")

    context = {
        'book': book,
    }
    return render(request, 'book_detail.html', context)
