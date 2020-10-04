from django.shortcuts import render
from django.views.generic import CreateView
from .models import Location

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def find(request):
    if request.method == "POST":
        obj = MyPos(lat=request.POST.get("lat"),
                    lon=request.POST.get("lon"))
        obj.save()
        return nearest(obj.lat, obj.lon)
    return render(request, "badpage.html") 

class AddPlaceView(CreateView):
    model = Location
    template_name = "create.html"
    success_url = "/index/"
    fields = ("location",)