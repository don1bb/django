from django.http import HttpResponse
from django.shortcuts import render
from . import models

def book_view(request):
    book = models.Post.objects.all()
    return render(request, 'book.html', {'book': book})
