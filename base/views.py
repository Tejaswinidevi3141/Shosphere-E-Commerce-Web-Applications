from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category
from django.db.models import Q
from django.contrib import messages
def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        all_products=Product.objects.filter(pname_icontains=q) & Q (is_delete=False) | Q (category=Category) & Q (is_delete=False).order_by('?')
        if all_products==0:
            messages.error(request,'NO PRODUCTS')
            return redirect(('home'))
        elif 'cat' in request.GET:
            cat=request.GET['Cat']
            cat_data=Category.objects.get(cname=cat)
            all_products=Product.objects.filter(category=cat_data.id)
    else:
        all_products=Product.objects.filter(is_delete=False).order_by('?')
        return render(request,'home.html',{'all_products':all_products})

def details(request,pk):
    product=get_object_or_404(product,id=pk)
    category_products=product.objects.filter(category=product.category)
    return render (request,'details.html',{'product':product,'category_products':category_products})