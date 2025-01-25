from django.urls import path
from restaurant_app import views

urlpatterns = [
    path('test/',views.test,name='test'),
    path('',views.home,name='home'),
]
