from django.shortcuts import redirect, render
from .models import Teacher

# Create your views here.

def index(request):
    context = {
        "tset" : Teacher.objects.all()
    }
    return render(request, "teachhtml/index.html", context)

def main(request):
    context = {
        "tset" : Teacher.objects.all()
    }
    return render(request, "teachhtml/detail.html", context)

def showinfo(request, pk):
    t = Teacher.objects.get(id=pk)
    context={
        "t" : t
    }
    
    return render(request, "teachhtml/show.html", context)

def detail(request, nameurl):
    t = Teacher.objects.get(name=nameurl)
    context={
        "t" : t
    }
    
    return render(request, "teachhtml/show.html", context)

def delete(request, deleteurl):
    t = Teacher.objects.get(id=deleteurl)
    t.delete()
    return redirect("index")
    
