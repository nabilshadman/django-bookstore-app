from django.shortcuts import render

from django.http import HttpResponse
from backend.models import Book

def index(request):
    books=Book.objects.all()
    return render(request,'frontend/display.html',{'books':books})
