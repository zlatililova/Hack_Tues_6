from django.shortcuts import render
from django.views.generic import CreateView
from .models import Location

# Create your views here.

def index(request):
    return render(request, 'index.html')


 
class AddPlaceView(CreateView):
    model = Location
    template_name = "create.html"
    success_url = "/index/"
    fields = ("location",)