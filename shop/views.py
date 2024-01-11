from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    product_objects = Product.objects.all()

    # search bar
    item_name = request.GET.get('item_name')
    if item_name is not '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator
    paginator = Paginator(product_objects, 3)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_objects = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_objects': product_objects})


def cart_finder(user):
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return False
    else:
        return True


def cart_item_finder(id):
    try:
        cart = CartItem.objects.get(product_id=id)
    except CartItem.DoesNotExist:
        return False
    else:
        return True


def add_to_cart(request, id):
    user = request.user
    if user.is_authenticated:
        cart_status = cart_finder(user)
        if cart_status is False:
            cart = Cart(user=user, cart_status="pending")
            cart.save()
        else:
            cart_item = cart_item_finder(id)
            cart = Cart.objects.get(user=user)
            product_objects = Product.objects.get(id=id)
            if cart_item is False:
                cart_items = CartItem(product_id=product_objects, cart_id=cart, quantity=1)
                cart_items.save()
            else:
                cart_item = CartItem.objects.get(product_id=id)
                cart_item.quantity += 1
                cart_item.save()
            return render(request, 'shop/detail.html', {'product_objects': product_objects})
    else:
        return redirect('login')


def payment(request):
    if request.method == "POST":
        price = request.GET.get('price')
        payment_status = request.GET.get('payment_status')

        payment = Payment(payment_status=payment_status, price=price)
        payment.save()

    return render(request, 'shop/checkout.html')
