from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'created', 'updated', 'published')
    list_display_links = ('pk', 'name')
    list_editable = ('published',)
    list_filter = ('created', 'updated', 'published')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'slug', 'price', 'quantity', 'created', 'updated', 'published', 'get_image')
    list_display_links = ('pk', 'name')
    list_editable = ('published', 'quantity', 'category')
    list_filter = ('category', 'created', 'updated', 'published')
    search_fields = ('description', 'name')

    def get_image(self, product):
        if product.image:
            url = product.image.url
        else:
            url = "https://qph.cf2.quoracdn.net/main-qimg-1a4bafe2085452fdc55f646e3e31279c-lq"
        return mark_safe(f'<img src="{url}" alt="no image" width="80px" style="border-radius: 8px">')

    get_image.short_description = "image"
    prepopulated_fields = {'slug': ('name', 'quantity')}
