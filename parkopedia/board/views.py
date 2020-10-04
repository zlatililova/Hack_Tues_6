from django.shortcuts import render
from board.models import Post
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
 