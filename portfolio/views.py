from django.shortcuts import render, HttpResponse
from . import urls



def home(request):
        return render(request,'index.html')