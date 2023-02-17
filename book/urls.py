from django.urls import path
from . import views

urlpatterns = [
    path('book_link', views.book_view, name='book'),
    path('book/<int:id>', views.book_view, name='details'),
]