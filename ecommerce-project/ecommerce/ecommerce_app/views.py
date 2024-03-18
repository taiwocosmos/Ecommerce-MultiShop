from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# from django.http import HttpResponse
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, shipped=False)
        items= order.orderitem_set.all()
        cart_items = order.get_cart_item
        cart_total = order.get_cart_total
    else:
        items = []
        cart_items = 0
        cart_total = 0
        # order = {'get_cart_item':0, 'get_cart_total':0}

    context = {'items': items, 'cart_items': cart_items, 'cart_total': cart_total}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, shipped=False)
        items= order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_item':0, 'get_cart_total':0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def shop(request):
    return render(request, 'shop.html')

def SearchPanel(request):
    if request.method == 'GET':
        searched = request.GET.get('query')
        if searched:
            products = Product.objects.filter(product_name__icontains=searched)
            return render(request, 'searchpanel.html', {'products':products})
        else:
            print('Product not found')
            return render(request, 'searchpanel.html', {})
        

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user

    product = Product.objects.get(id=productId)


    order, created = Order.objects.get_or_create(customer=customer, shipped=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    elif action == 'delete':
        orderItem.quantity = 0

    orderItem.quantity = max(orderItem.quantity, 0)
    orderItem.save()

    if orderItem.quantity == 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False) 