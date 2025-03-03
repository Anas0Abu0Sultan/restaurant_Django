from django.contrib import admin
from .models import Drinks,Grills,Meals,Rest_detail,Sandwiches,Sweets,Salads,Chefs,Services,AboutUs, AboutUsImage, Contact,CartItem,Cart,Comment

admin.site.register(Rest_detail)
admin.site.register(Contact)
# admin.site.register(CartItem)
# admin.site.register(Cart)
admin.site.register(Comment)

@admin.register(Drinks)
class DrinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_drink', 'small_price', 'medium_price', 'large_price')
    search_fields = ('name', 'type_of_drink')
    list_filter = ('type_of_drink',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_items')
    search_fields = ('user__username',)
    list_filter = ('created_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'food_item', 'size', 'quantity')
    search_fields = ('cart__id', 'food_item__name')
    list_filter = ('size',)

# @admin.register(Drinks)
# class DrinksAdmin(admin.ModelAdmin):
#     list_display=['name','price','size','image','type_of_drink']
#     list_filter = ['size','type_of_drink']
#     search_fields = ['name']

@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):
    list_display=['name','price','image']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Sandwiches)
class SandwichesAdmin(admin.ModelAdmin):
    list_display=['name','price','image']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Grills)
class GrillsAdmin(admin.ModelAdmin):
    list_display=['name','price','image']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Sweets)
class SweetsAdmin(admin.ModelAdmin):
    list_display=['name','price','image']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Salads)
class SaladsAdmin(admin.ModelAdmin):
    list_display=['name','price','size','image']
    list_filter = ['size']
    search_fields = ['name']

# @admin.register(Clients)
# class ClientsAdmin(admin.ModelAdmin):
#     list_display=['name','description','image','message']
#     list_filter = ['name','description','message']
#     search_fields = ['name']


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display=['name','description','image','facebook','instagram','twitter']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display=['name','description','icon']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['experience_years', 'master_chefs']
    search_fields = ['experience_years', 'master_chefs']

@admin.register(AboutUsImage)
class AboutUsImageAdmin(admin.ModelAdmin):
    list_display = ['about_us', 'image']