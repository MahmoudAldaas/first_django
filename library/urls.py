# library/urls.py — Maps URL patterns to view functions
from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    # name="..." lets us reference these routes in templates with {% url 'name' %}
    path('', views.home, name='home'),                        # /
    path('books/', views.books, name='books'),                # /books/
    path('dashboard/', views.dashboard, name='dashboard'),    # /dashboard/
    path('books/<int:id>/', views.book_detail, name='book_detail'),  # /books/1/
]
