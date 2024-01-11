from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
            cart = Cart(user=user, cart_status="pending",  total_price=0)
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


@login_required
def cart(request):
    user = request.user
    if user.is_authenticated:
        cart_status = cart_finder(user)
        if cart_status is False:
            user_cart = Cart(user=user, cart_status="pending", total_price=0)
            cart.save()
            return render(request, 'shop/cart.html', {'user_cart': user_cart})
        else:
            user_cart = Cart.objects.get(user=user)
            cart_item = CartItem.objects.filter(cart_id=user_cart)
            total = 0
            for item in cart_item:
                cart_item_price_t = item.quantity * item.product_id.price
                total += cart_item_price_t
            user_cart.total_price = total
            user_cart.save()
            return render(request, 'shop/cart.html', {'user_cart': user_cart, 'cart_item': cart_item})
    else:
        return redirect('login')


@login_required
def payment(request):
    user = request.user
    if user.is_authenticated:
        cart_status = cart_finder(user)
        if cart_status is True:
            cart = Cart.objects.get(user=user)
            cart_item = CartItem.objects.filter(cart_id=cart)
            total = 0
            for item in cart_item:
                cart_item_price_t = item.quantity * item.product_id.price
                total += cart_item_price_t
            payment = Payment(cart_id=cart, payment_status='pending', price=total)
            payment.save()
    # return render(request, 'shop/checkout.html', {'payment': payment})
