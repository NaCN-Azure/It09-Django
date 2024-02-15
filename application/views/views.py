from django.shortcuts import render
from django.shortcuts import HttpResponse
def index(request):
    # request.POST
    # request.GET
    return HttpResponse("Yeah!")
# Create your views here.
