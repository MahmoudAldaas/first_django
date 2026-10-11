# Library Management Website

A mini Django project to practice the flow: **URL → View → Context → Template → Static Files**.  
No database — all book data is hard-coded in `views.py`.

---

## How It Works: URL → View → Template

Here's what happens when you open **`/books/`** in your browser:

```
1. BROWSER  →  sends GET /books/
2. URL ROUTING
   └─ library_project/urls.py  →  path('', include('library.urls'))
   └─ library/urls.py          →  path('books/', views.books, name='books')
3. VIEW (library/views.py)
   └─ The books() function runs
   └─ Creates context = {'books': BOOKS}  (the hard-coded list)
   └─ Calls render(request, 'books.html', context)
4. TEMPLATE (templates/books.html)
   └─ {% extends 'main.html' %}  →  loads the base layout
   └─ {% for book in books %}    →  loops through context['books']
   └─ {% url 'book_detail' book.id %}  →  builds link /books/1/
5. STATIC FILES
   └─ {% static 'css/style.css' %}  →  /static/css/style.css
   └─ {% static 'js/main.js' %}    →  /static/js/main.js
6. BROWSER  ←  receives the fully rendered HTML page
```

---

## Project Structure

```
python project/
├── library_project/          # Project configuration
│   ├── settings.py           # INSTALLED_APPS, TEMPLATES, STATIC config
│   ├── urls.py               # Root URL router → includes library.urls
│   └── ...
├── library/                  # Our app
│   ├── urls.py               # 4 named routes
│   └── views.py              # 4 view functions + hard-coded books
├── templates/                # HTML templates
│   ├── main.html             # Base template (navbar, footer, static links)
│   ├── components/
│   │   ├── navbar.html       # Navigation bar ({% include %})
│   │   └── footer.html       # Footer ({% include %})
│   ├── home.html             # Home page
│   ├── books.html            # Book list ({% for book in books %})
│   ├── book_detail.html      # Single book detail
│   └── dashboard.html        # Library statistics
├── static/                   # Static files
│   ├── css/style.css         # Custom CSS
│   ├── js/main.js            # Custom JavaScript
│   └── images/logo.png       # Site logo
├── manage.py
└── README.md
```

---

## URLs

| URL             | View          | Template          | Description        |
|-----------------|---------------|-------------------|--------------------|
| `/`             | `home`        | `home.html`       | Welcome page       |
| `/books/`       | `books`       | `books.html`      | All books list     |
| `/books/<id>/`  | `book_detail` | `book_detail.html` | Single book detail |
| `/dashboard/`   | `dashboard`   | `dashboard.html`  | Library statistics |

---

## How to Run

```bash
# Activate the virtual environment
source .venv/bin/activate

# Check for errors
python manage.py check

# Start the dev server
python manage.py runserver

# Open in browser:
#   http://127.0.0.1:8000/
#   http://127.0.0.1:8000/books/
#   http://127.0.0.1:8000/books/1/
#   http://127.0.0.1:8000/dashboard/
```
