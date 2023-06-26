from django.shortcuts import render
from django.http import HttpResponse
from home.models import UserProfile
from order.models import Order, OrderProduct
from product.models import Product

# Create your views here.

def index(request):
    #category = Category.objects.all()
    current_user = request.user  # Access User Session information
    products = Product.objects.all()
    profile = UserProfile.objects.get(pk=current_user.id)
    context = { 
               'profile':profile,'products':products}
    return render(request,'user_profile.html',context)


def orders(request):
    #category = Category.objects.all()
    current_user = request.user
    orders=Order.objects.filter(user_id=current_user.id)
    context = {#'category': category,
               'orders': orders,
               }
    return render(request,'user_orders.html',context)