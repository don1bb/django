from django.shortcuts import render, get_object_or_404
from . import models

def tv_showview(request):
    show = models.TVshow.objects.all()
    return render(request, 'tvshow.html',{'show': show})

def tv_show_detailview(request, id):
    show_id = get_object_or_404(models.TVshow, id=id)
    return render(request, 'tvshow_detail.html', {'show_id': show_id})