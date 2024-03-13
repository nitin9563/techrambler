from django.shortcuts import render,HttpResponse
from website.models import *
from random import choice

# Create your views here.
def index(request):
    videos_data = Content.objects.all()

    query = request.GET
    specific = ""

    data_role = "main"

    data = videos_data

    if "playlist" in query:
        playlist_data = Playlist.objects.all()
        data = playlist_data
        data_role = "play"

    if "category" in query:
        category_data = Category.objects.all()
        data = category_data
        data_role = "cat"

    if "category_name" in query:
        obj = Category.objects.get(category_name = query["category_name"])
        videos_specific = Content.objects.filter(category = obj)
        specific = f"category > {query['category_name']}"
        data = videos_specific
        data_role = "main"

    if "playlist_name" in query:
        obj = Playlist.objects.get(playlist_name = query["playlist_name"])
        videos_specific = Content.objects.filter(playlist = obj)
        specific = f"Playlist > {query['playlist_name']}"
        data = videos_specific
        data_role = "main"
    
    return render(request,"index.html",{"data" : data,"specific" : specific, "data_role" :data_role})

def dataadd(request):

    a = Category.objects.all()
    b = Playlist.objects.all()
    c = Content.objects.all()

    # for i in c:
    #     Content.objects.filter(id=i.id).delete()

    for i in range(50):
        playlist=choice(b)
        category = choice(a)

        x = Content(title = f"playlist : {playlist} and with category : {category}",description = "Unlock the magic of Python with this tutorial on creating star patterns effortlessly.#pythonpattern #python", playlist=playlist,category = category,thumbnail = "thumbnails\Thumbnail-dj-2.jpg")
        x.save()
        
    return HttpResponse("done check")


def code(request,id):
    code=Content.objects.get(id=id)
    return render(request,"code.html",{"post":code})