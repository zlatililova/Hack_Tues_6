from django.shortcuts import render
from board.models import Post, MyPos
from board.parking_search import nearest
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        obj = Post(address=request.POST.get("address"),
                   rating=request.POST.get("rating"))
        obj.save()
        return render(request, "success.html")
    return render(request, "create.html")
 
def find(request):
    if request.method == "POST":
        obj = MyPos(lat=request.POST.get("lat"),
                    lon=request.POST.get("lon"))
        obj.save()
        return nearest(obj.lat, obj.lon)
    return render(request, "badpage.html")
