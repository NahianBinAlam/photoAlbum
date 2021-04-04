from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myphotos/index.html')

def viewphoto(request, pk):
    return render(request, 'myphotos/photo.html')
    
def addphoto(request):
    return render(request, 'myphotos/addphoto.html')
