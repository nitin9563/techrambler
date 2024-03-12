from django.shortcuts import render,HttpResponse
from website.models import *
from random import choice

# Create your views here.
def index(request):
    videos = Content.objects.all()
    playlist = Playlist.objects.all()
    category = Category.objects.all()

    return render(request,"index.html",{"video":videos,"playlist":playlist,"category":category})

def dataadd(request):

    a = Category.objects.all()
    b = Playlist.objects.all()
    c = Content.objects.all()

    # for i in c:
    #     Content.objects.filter(id=i.id).delete()

    for i in range(20):
        x = Content(title = "Python Magic: Create Pattern (6) with Ease. ",description = "Unlock the magic of Python with this tutorial on creating star patterns effortlessly.#pythonpattern #python", playlist=choice(b),category = choice(a),thumbnail = "thumbnails\Thumbnail-dj-2.jpg")
        x.save()
        
    return HttpResponse("done check")


def code(request,id):
    code=Content.objects.get(id=id)
    return render(request,"code.html",{"post":code})