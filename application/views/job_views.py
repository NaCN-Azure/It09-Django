from django.shortcuts import render
from django.shortcuts import HttpResponse

def index_view(request):
    return render(request, 'index.html')


