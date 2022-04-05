from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('brand_details', views.brand_details, name='brand_details'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('shop_details', views.shop_details, name='shop_details'),
    path('add_malls', views.add_malls, name='add_malls'),
    path('add_brands', views.add_brands, name='add_brands'),
    path('malls', views.malls, name='malls'),
    path('brands', views.brands, name='brands'),
    
]