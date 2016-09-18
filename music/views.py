from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album_id = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album Does Not Exist')
    return render(request, 'music/details.html', {'album':album})