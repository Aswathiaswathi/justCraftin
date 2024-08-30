from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='home'),
    path('products_list',views.products_list,name='products_list'),
    path('product_details/<pk>',views.product_details,name='product_details'),
    path('blog',views.blog_page,name='blog'),
    path('about',views.about_page,name='about'),
    path('contact',views.contact_page,name='contact'),



]