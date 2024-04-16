from django.shortcuts import render
from django.views import View
from .models import Customer,Product, Cart, OrderPlaced
from .forms import CustomRegistrationForm,CustomProfileForm
from django.contrib import messages

class ProductView(View):
    def get(self,request):
        mobiles = Product.objects.filter(category = 'M')
        laptops = Product.objects.filter(category = 'L')
        earphones = Product.objects.filter(category = 'E')
        return render(request,'app/home.html', {'mobiles':mobiles,
                'laptops':laptops, 'earphones':earphones})


class productDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

class profileView(View):
   def get(self,request):
      form = CustomProfileForm
      return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary'})
    
   def post(self,request):
      form = CustomProfileForm(request.POST)
      if form.is_valid():
         user = request.user
         name = form.cleaned_data['name']
         locality = form.cleaned_data['locality']
         city = form.cleaned_data['city']
         state = form.cleaned_data['state']
         zipcode = form.cleaned_data['zipcode']

         reg = Customer(user=user, name=name, locality = locality, city=city, state=state, zipcode = zipcode)

         reg.save()
         messages.success(request,'Congratulation !! succussfully update profile')
      return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary'})



def address(request):
 addres = Customer.objects.filter(user = request.user)
 return render(request, 'app/address.html', {'addres': addres, 'active':'btn-primary'})

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
