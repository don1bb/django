from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from . import models, forms

def book_view(request):
    book = models.Post.objects.all()
    return render(request, 'book.html', {'book': book})
def book_detailview(request, id):
    book_id = get_object_or_404(models.Post, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})


def create_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.bookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2> Фильм успешно добавлен! </h>')

    else:
        form = forms.bookForm()

    return render(request, 'add_book.html', {'form': form})



def update_book_view(request, id):
    book_object = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        form = forms.bookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Фильм успешно обновлен!</h2>')
    else:
        form = forms.bookForm(instance=book_object)

    return render(request, 'update_book.html', {
                                                    'form': form,
                                                    'object': book_object
                                                   })


def delete_book_view(request, id):
    book_object = get_object_or_404(models.Post, id=id)
    book_object.delete()
    return HttpResponse('<h2>Фильм успешно удален!!!</h2>')