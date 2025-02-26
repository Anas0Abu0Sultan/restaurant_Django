from django.urls import path
from restaurant_app import views

app_name='restaurant_app'

urlpatterns = [
    path('test/',views.test,name='test'),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.service,name='services'),
    path('menu/<str:category>/',views.menu,name='menu'),
    path('contact/',views.contact,name='contact'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove_cart_item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
]

