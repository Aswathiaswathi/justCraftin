from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:8]
    new_arrivals=Product.objects.order_by('-id')[:4]
    context={'featured_products':featured_products,'new_arrivals':new_arrivals}
    return render(request,'index.html',context)
def products_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,4)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)
def product_details(request,pk):
    product=Product.objects.get(pk=pk)
    featured_products=Product.objects.order_by('priority')[:4]
    context={'product':product,'featured_products':featured_products}
    return render(request,'product_details.html',context)
def blog_page(request):
    return render(request,'blog.html')
def about_page(request):
    return render(request,'about.html')
def contact_page(request):
    return render(request,'contact.html')


