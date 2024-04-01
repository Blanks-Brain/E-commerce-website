from django.shortcuts import render
from django.views import View
from .models import Customer,Product, Cart, OrderPlaced
from .forms import CustomRegistrationForm
from django.contrib import messages

class ProductView(View):
    def get(self,request):
        mobiles = Product.objects.filter(category = 'M')
        laptops = Product.objects.filter(category = 'L')
        earphones = Product.objects.filter(category = 'E')
        return render(request,'app/home.html', {'mobiles':mobiles,
                'laptops':laptops, 'earphones':earphones})

# def home(request):
#  return render(request, 'app/home.html')

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class productDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')


def mobile(request):
 return render(request, 'app/mobile.html')


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomRegistrationForm
        return render (request,'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form = CustomRegistrationForm(request.POST)
        
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully')
            form.save()     
        return render (request,'app/customerregistration.html',{'form':form})
    

def checkout(request):
 return render(request, 'app/checkout.html')
