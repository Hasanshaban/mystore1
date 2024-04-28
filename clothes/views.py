from django.shortcuts import render
from .models import Clothing
from django.contrib.auth.models import User



# Create your views here.
def home_view(request):
    return render(request,'clothes/index.html')
def clothes_listview(request):
    clothes=Clothing.objects.all()
    context={
        "clothes":clothes,
    }
    return render(request,'clothes/products.html',context)

