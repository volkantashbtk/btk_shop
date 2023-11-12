from django.contrib import admin
from product.models import Category, Product, Images


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    # fields = ['status']
admin.site.register(Category, CategoryAdmin)

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields =['image_tag',]

class ProductAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'category_tag']
    list_filter = ['status','category']
    readonly_fields = ['image_tag']
    inlines = [ProductImagesInline]
admin.site.register(Product, ProductAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
admin.site.register(Images, ImagesAdmin)
    
