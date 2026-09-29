from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def add_to_cart(request,pk):
    product = get_object_or_404(product,id=pk)
    try:
        cart_product = get_object_or_404(Cart,product = product)
        cart_product.quantity+=1
        cart_product.save()
    except:
        Cart.objects.create(
            user=request.user,
            product=product.id,
            total_price=product.price
    )
    return redirect ('hello')
    return HttpResponse('hello')

def cartpage(request):
    cart_product=Cart.objects.filter(user=request.user)
    TA=0
    for i in Cart.objects.filter(user=request.user):
        TA += i.product.price
    return render (request,'cartpage.html',{'cart_products':cart_product})
def remove(request,pk):
    get_object_or_404(Cart,id=pk).delete()
    return redirect('cartpage')
def plus(request,pk):
    cart_product=get_object_or_404(Cart,id=pk)
    cart_product.quantity+=1
    cart_product.total.price+=cart_product.price
    cart_product.save()
    return redirect('cartpage')
def minus(request,pk):
    cart_product=get_object_or_404(Cart,id=pk)
    if cart_product.quantity>1:
        cart_product.quantity -= 1
        cart_product.total_price -= cart_product.product.price
        cart_product.save()
    else:
        cart_product.delete()
        return redirect('cartpage')
