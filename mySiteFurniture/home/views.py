from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactForm, ContactFormMessage,Blog
from django.contrib import messages
from order.models import ShopCart
from product.models import Category, Product, Images, Comment
from home.forms import SearchForm,SignUpForm

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def index(request):
    blogs= Blog.objects.all()
    current_user = request.user
    setting = Setting.objects.get()
    popularproductdata = Product.objects.all().order_by('?')[:3] 
    products = Product.objects.all()
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    context = {'setting': setting, 'page':'home','popularproductdata':popularproductdata,'products':products,'blogs':blogs}
    return render(request, 'index.html', context)

def home(request):
    blogs= Blog.objects.all()
    setting = Setting.objects.get()
    products = Product.objects.all()
    context = {'setting': setting, 'page':'home','products':products,'blogs':blogs}
    return render(request, 'index.html', context)

def newarrivals(request):
    products = Product.objects.all()
    setting = Setting.objects.get()
    context = {'setting': setting, 'page':'new-arrivals', 'products':products}
    return render(request, 'new-arrivals.html', context)

def blog(request):
    blogs= Blog.objects.all()
    products = Product.objects.all()
    setting = Setting.objects.get()
    context = {'setting': setting, 'page':'blog','products':products,'blogs':blogs}
    return render(request, 'blog.html', context)

def feature(request):
    products = Product.objects.all()
    setting = Setting.objects.get()
    context = {'setting': setting, 'page':'feature','products':products}
    return render(request, 'feature.html', context)

def contact(request):
    products = Product.objects.all()
    setting = Setting.objects.get()
    context = {'setting': setting, 'page':'contact','products':products}
    return render(request, "contact.html",context)

def aboutus(request):
    products = Product.objects.all()
    setting = Setting.objects.get()
    context = {'setting': setting, 'page':'aboutus','products':products}
    return render(request, "aboutus.html",context )

def contactus(request):
    
    #category = categoryTree(0,'',currentlang)
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contactus')


    setting = Setting.objects.get()
 

    form = ContactForm
    context={'setting':setting,'form':form, 'page':'contactus'  }
    return render(request, 'contactus.html', context)

def product_detail(request, id,slug):
    product = Product.objects.get(pk=id)
    comments = Comment.objects.filter(product_id=id,status='True')
    context = {
        'product': product,
        'comments': comments,
    }
    return render(request,'product_detail.html',context)
def blog_detail(request, id):
    blogs = Blog.objects.get(pk=id)
    
    
    context = {
        'blogs':blogs
    }
    return render(request,'blog_detail.html',context)

def product_search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data  
            products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            context = {'products': products, 'query':query,
                       }
            return render(request, 'products_search.html', context)

    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST': # check post
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
         # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.error(request,"Giris hatali!! Bilgileri kontrol et")
            return HttpResponseRedirect('/login')
    setting = Setting.objects.get()
    context = {'setting':setting}
    return render(request, 'login.html',context)

def signup_view(request):
    if request.method == 'POST': # check post
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
            
    form = SignUpForm()    
    setting = Setting.objects.get()
    context = {'setting':setting,
               'form':form,
               }
    return render(request, 'signup.html',context)
