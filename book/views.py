from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

# def book_view(request):
#     book = models.Post.objects.all()
#     return render(request, 'book.html', {'book': book})
class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Post.objects.all()

    def get_queryset(self):
        return models.Post.objects.all()





# def book_detailview(request, id):
#     book_id = get_object_or_404(models.Post, id=id)
#     return render(request, 'book_detail.html', {'book_id': book_id})

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=book_id)








# def create_book_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.bookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2> Фильм успешно добавлен! </h>')
#
#     else:
#         form = forms.bookForm()
#
#     return render(request, 'add_book.html', {'form': form})



class BookCreateView(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.bookForm
    queryset = models.Post.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)





# def update_book_view(request, id):
#     book_object = get_object_or_404(models.Post, id=id)
#     if request.method == 'POST':
#         form = forms.bookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>Фильм успешно обновлен!</h2>')
#     else:
#         form = forms.bookForm(instance=book_object)
#
#     return render(request, 'update_book.html', {
#                                                     'form': form,
#                                                     'object': book_object
#                                                    })
#

class BookUpdateView(generic.UpdateView):
    template_name = 'update_book.html'
    form_class = forms.bookForm
    success_url = '/book/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=book_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)





# def delete_book_view(request, id):
#     book_object = get_object_or_404(models.Post, id=id)
#     book_object.delete()
#     return HttpResponse('<h2>Фильм успешно удален!!!</h2>')


class BookDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/book/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=book_id)




class AddRatingView(generic.CreateView):
    template_name = 'book_detail.html'
    form_class = forms.CommentForm
    queryset = models.Rating.objects.all()
    success_url = '/book/<int:id>/'

    def form_valid(self, form):
        return super(AddRatingView, self).form_valid(form=form)

