from django.urls import path
from restaurant_app import views

app_name='restaurant_app'

urlpatterns = [
    path('test/',views.test,name='test'),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.service,name='services'),
    path('menu/<str:category>/',views.menu,name='menu'),
    path('m/<str:category>/',views.menu_new,name='menu_new'),
    path('contact/',views.contact,name='contact'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('order/', views.cart, name='cart'),
    path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove_cart_item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),

    path('dashboard/', views.dashboard, name='dashboard'),
    
 
    # Drinks
    path('add-drink/', views.add_drink, name='add_drinks'),
    path('edit-drink/<int:drink_id>/', views.edit_drink, name='edit_drink'),
    path('delete-drink/<int:drink_id>/', views.delete_drink, name='delete_drink'),

    # Salads
    path('add-salad/', views.add_salad, name='add_salads'),
    path('edit-salad/<int:salad_id>/', views.edit_salad, name='edit_salad'),
    path('delete-salad/<int:salad_id>/', views.delete_salad, name='delete_salad'),

    # Meals
    path('add-meal/', views.add_meal, name='add_meals'),
    path('edit-meal/<int:meal_id>/', views.edit_meal, name='edit_meal'),
    path('delete-meal/<int:meal_id>/', views.delete_meal, name='delete_meal'),

    # Sandwiches
    path('add-sandwich/', views.add_sandwich, name='add_sandwiches'),
    path('edit-sandwich/<int:sandwich_id>/', views.edit_sandwich, name='edit_sandwiche'),
    path('delete-sandwich/<int:sandwich_id>/', views.delete_sandwich, name='delete_sandwiche'),

    # Grills
    path('add-grill/', views.add_grill, name='add_grills'),
    path('edit-grill/<int:grill_id>/', views.edit_grill, name='edit_grill'),
    path('delete-grill/<int:grill_id>/', views.delete_grill, name='delete_grill'),

    # Sweets
    path('add-sweet/', views.add_sweet, name='add_sweets'),
    path('edit-sweet/<int:sweet_id>/', views.edit_sweet, name='edit_sweet'),
    path('delete-sweet/<int:sweet_id>/', views.delete_sweet, name='delete_sweet'),

    path('add-chef/',views.add_chef,name='add_chef'),
    path('edit-chef/<int:chef_id>/',views.edit_chef,name='edit_chef'),
    path('delete-chef/<int:chef_id>/',views.delete_chef,name='delete_chef'),

    path('add-comment/',views.add_comment,name='add_comment'),
    path('delete-comment/<int:comment_id>/',views.delete_comment,name='delete_comment'),
    path('approve-comment/<int:comment_id>/', views.update_comment_status, {'status': 'approved'}, name='approve_comment'),
    path('reject-comment/<int:comment_id>/', views.update_comment_status, {'status': 'rejected'}, name='reject_comment'),

    path('edit-contact/<int:contact_id>/',views.edit_contact,name='edit_contact'),
    path('edit-rest-detail/', views.edit_rest_detail, name='edit_rest_detail'),

    path('create-payment/', views.create_payment, name='create_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),

    path('view_order/<int:order_id>/', views.view_order, name='view_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('get-cart-item-count/', views.get_cart_item_count, name='get_cart_item_count'),
    

    path('services/add/', views.add_service, name='add_service'),
    path('services/edit/<int:service_id>/', views.edit_service, name='edit_service'),
    path('services/delete/<int:service_id>/', views.delete_service, name='delete_service'),

]


