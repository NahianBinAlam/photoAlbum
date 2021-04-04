from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.
def index(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'myphotos/index.html', context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'myphotos/photo.html',{'photo':photo})
    
def addphoto(request):
    return render(request, 'myphotos/addphoto.html')
