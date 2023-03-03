from django.urls import path
from . import views

urlpatterns = [
    # path('book_link/', views.book_view, name='book'),
    path('book/', views.BookView.as_view(), name='book'),
    # path('book/<int:id>/', views.book_detailview, name='details'),
    path('book/<int:id>/', views.BookDetailView.as_view(), name='detail'),
    # path('book/<int:id>/update/', views.update_book_view, name='update'),
    path('book/<int:id>/update/', views.BookUpdateView.as_view(), name='update'),
    # path('book/<int:id>/delete/',views.delete_book_view, name='delete'),
    path('book/<int:id>/delete/', views.BookDeleteView.as_view(), name='delete'),
    # path('add-book/', views.create_book_view, name='create'),
    path('add-book/', views.BookCreateView.as_view(), name='create'),
    path('add-comment/', views.AddRatingView.as_view(), name='com'),
]


























