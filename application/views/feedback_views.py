from django.shortcuts import render
from django.shortcuts import HttpResponse
def index(request):
    # request.POST
    # request.GET
    return HttpResponse("Yeah!")
# Create your views here.

def index_view(request):
    return render(request, 'index.html')
