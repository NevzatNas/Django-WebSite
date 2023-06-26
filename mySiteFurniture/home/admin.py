from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage,UserProfile,Blog


class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','adress','city','country','image_tag']
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','content', 'update_at']



admin.site.register(Blog,BlogAdmin)
admin.site.register(ContactFormMessage,ContactMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile,UserProfileAdmin)
