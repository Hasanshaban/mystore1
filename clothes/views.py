from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Clothing,Order,Size_info
from django.contrib.auth.models import User
from .forms import Orderform,signupForm,signinForm


# Create your views here.
def home_view(request):
    return render(request,'clothes/index.html')
def about_view(request):
    return render(request,'clothes/about.html')
def contact_view(request):
    return render(request,'clothes/contact.html')

@login_required(login_url='signinview')
def clothes_listview(request):
    clothes=Clothing.objects.all()
    order_list=Order.objects.all()
    context={
        "clothes":clothes,
        "order_list":order_list,
    }
    return render(request,'clothes/products.html',context)

def cloth_info_view(request):
    if request.method=='POST':
        form =Orderform(request.POST)
        if form.is_valid():
            form.instance.user_id=request.user.id
            form.save() 
            clothes=Clothing.objects.all()
       
            context={
              "clothes":clothes,
        
                 }
            return render(request,'clothes/products.html',context)
    
        
  
    
def clothes_info(request,clothes_id):
     clothes_info=Clothing.objects.get(pk=clothes_id)
     form =Orderform(request.POST) 
     size_info=Size_info.objects.all()
     context={
        "clothes_info":clothes_info,
        "form":form,
        "size_info":size_info,
    }
     return render(request,'clothes/single-product.html',context)
@login_required(login_url='signinview')
def orderview(request):
    if request.method=='POST':
        form =Orderform(request.POST)
        
        if form.is_valid():
            form.instance.user_id=request.user.id
            form.save()  
    else:
      form=Orderform()
    context={
         "form":form,
         }
    return render(request,'clothes/single-product.html',context)
def signupview(request):
    if request.method=='POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'clothes/products.html')
    else:
     form=signupForm()
    context={
             "form":form,
                }
    return render(request,'clothes/signup.html',context)

def signinview(request):
    
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('clothes_listview')
            else:
                   form=signinForm()
                   context={
                     "form":form,
                     "pass":"رمز اشتباه"
                   }
                   return render(request,'clothes/signin.html',context)
    else:
     form=signinForm()
    context={
             "form":form,
                }
    return render(request,'clothes/signin.html',context)

def user_logout(request):
    logout(request)
    return redirect('signinview')

def get_order(request):
    user_id=User.objects.all()
    order_list=Order.objects.all()
    form=Orderform()
    context={
        "order_list":order_list,
        "user":user_id,
        "form":form,
    }
    return render(request,'clothes/test.html',context)

def get_orderuser(request):
    
    order_listuser=Order.objects.filter()
    context={
        "order_list":order_listuser,
        
    }
    return render(request,'clothes/test.html',context)
@login_required(login_url='signinview')
def User_view(request):
    my_user=Order.objects.filter(user=request.user)
    print(my_user)
    context={
        'my_user':my_user,
    }
    return render (request,'clothes/myuser.html',context)