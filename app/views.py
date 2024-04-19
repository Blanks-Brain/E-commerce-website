from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product, Cart, OrderPlaced
from .forms import CustomRegistrationForm,CustomProfileForm
from django.contrib import messages
from django.db.models import Q

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
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 
 Cart(user = user , product = product).save()
 return redirect('/cart')
 

def show_cart(request):
   if request.user.is_authenticated:
      user = request.user
      cart = Cart.objects.filter(user = user)
      amount = 0.0
      shipping_amount =50.0
      total_amount = 0.0
      cart_product = [p for p in Cart.objects.filter(user = user)]
      if cart_product:
         for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount+=tempamount

      total_amount= amount+shipping_amount

      return render(request, 'app/addtocart.html' , {'carts':cart, 'totalamount': total_amount,'shippingammount':shipping_amount, 'amount':amount })

def plusCart(request):
   if request.method == 'GET':
      prod_id = request.GET['prod_id']

      c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
  
      c.quantity+=1
      c.save()
      amount = 0.0
      shipping_amount =50.0
      total_amount = 0.0
      cart_product = [p for p in Cart.objects.filter(user = request.user)]
      if cart_product:
         for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount+=tempamount

      total_amount= amount+shipping_amount
      data = {
         'quantity': c.quantity,
         'amount': amount,
         'totalamount': total_amount
      }
      return JsonResponse(data)
   
def minusCart(request):
   if request.method == 'GET':
      prod_id = request.GET['prod_id']

      c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
  
      c.quantity-=1
      c.save()
      amount = 0.0
      shipping_amount =50.0
      total_amount = 0.0
      cart_product = [p for p in Cart.objects.filter(user = request.user)]
      if cart_product:
         for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount+=tempamount

      total_amount= amount+shipping_amount
      data = {
         'quantity': c.quantity,
         'amount': amount,
         'totalamount': total_amount
      }
      return JsonResponse(data)

def removeCart(request):
   if request.method == 'GET':
      prod_id = request.GET['prod_id']

      c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
  
      c.delete()
      amount = 0.0
      shipping_amount =50.0
      total_amount = 0.0
      cart_product = [p for p in Cart.objects.filter(user = request.user)]
      if cart_product:
         for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount+=tempamount

      total_amount= amount+shipping_amount
      data = {
         'amount': amount,
         'totalamount': total_amount
      }
      return JsonResponse(data)



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
 user  = request.user
 address = Customer.objects.filter(user = user)
 cart_item = Cart.objects.filter(user = user )
 print(cart_item)
 amount = 0.0
 shipping_amount =50.0
 total_amount = 0.0
 cart_product = [p for p in Cart.objects.filter(user = request.user)]
 price=[]
 if cart_product:
   for p in cart_product:
      tempamount = (p.quantity * p.product.selling_price)
      price.append(tempamount)
      amount+=tempamount

 total_amount= amount+shipping_amount
 return render(request, 'app/checkout.html', {'address':address, 'totalamount':total_amount,'cart_item':cart_item,'price':price})
