from django.urls import path
from restaurant_app import views

urlpatterns = [
    path('test/',views.test,name='test'),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.service,name='services'),
    path('menu/<str:category>/',views.menu,name='menu'),

]
