from django.contrib import admin
from product.models import Category,Product,Images,Comment,Post

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price','amount','image_tag','status']
    list_filter = ['status']
    inlines = [ProductImageInline]
    readonly_fields = ('image_tag',)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag']
    readonly_fields = ('image_tag',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','product','rate','id')

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','keywords','image_tag','create_at']


admin.site.register(Post,PostAdmin)   
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)
