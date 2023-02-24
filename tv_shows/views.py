from django.shortcuts import render, get_object_or_404
from . import models

def tv_showview(request):
    show = models.TVshow.objects.all()
    return render(request, 'tvshow.html',{'show': show})

def tv_show_detailview(request, id):
    show_id = get_object_or_404(models.TVshow, id=id)
    return render(request, 'tvshow_detail.html', {'show_id': show_id})


# def create_tv_show_view(request):
#     methood = request.method
#     if method == 'POST':
#         form = forms.TvShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2> Фильм успешно добавлен </h>')
#
#         else:
#             form =
