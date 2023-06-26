from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from home import views
from order import views as orderviews

urlpatterns = [
    path('', include('home.urls')),
    path('home/', views.home, name='home'),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
    path('feature/', views.feature, name='feature'),
    path('blog/', views.blog, name='blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('new-arrivals/', views.newarrivals, name='new-arrivals'),
    path('home/', views.home, name='home'),
    path('search/', views.product_search, name='product_search'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('shopcart/', orderviews.shopcart, name='shopcart'),


]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
