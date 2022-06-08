from django.shortcuts import redirect, render

from shop.models import Product, Review

# Create your views here.


def index(request):
    db = Product.objects.all()
    context = {
        "db" : db
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       price = request.POST.get('price')
       count = request.POST.get('count')
       comment = request.POST.get('comment')
       Product(name = name , price = price , count = count , comment = comment).save()
       return redirect('index')
    return render(request, 'crud/create.html')

def showinfo(request, id):
    info = Product.objects.get(id = id)
    rev = info.review_set.all()
    print(rev)
    if request.method == 'POST':
        info.name = request.POST.get('name')
        info.price = request.POST.get('price')
        info.count = request.POST.get('count')
        info.comment = request.POST.get('comment')
        info.save()
        return redirect('index')
    
                           
    context = {
        "info" : info,
        "rev"  : rev
    }
    return render(request, 'crud/info.html', context)
    

def delete(request, id):
    info = Product.objects.get(id = id)
    info.delete()
    return redirect('index')
    
def creply(request, id):
    info = Product.objects.get(id = id)
    name = request.POST.get("user")
    con = request.POST.get("con")
    Review(pro = info, name = name, con = con ).save()
    return redirect('info', info.id)


def dreply(request, pro_id, rep_id):
    info = Product.objects.get(id = pro_id)
    rev = Review.objects.get(id=rep_id)
    rev.delete()
    
    return redirect('info', info.id)
    
        