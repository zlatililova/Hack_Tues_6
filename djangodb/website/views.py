from django.shortcuts import render
from.models import Park


def home(request):
	all_parks = Park.objects.all
	return render(request,'home.html',{'all':all_parks})
	
def searchbar(request):
	if request.method == "GET":
		search = request.GET.get('search')
		post = Park.objects.all().filter(neigh = search)
		return render(request, 'searchbar.html',{'post':post})

# Create your views here.
