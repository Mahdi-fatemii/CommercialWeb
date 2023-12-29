from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
import bcrypt
# Create your views here.


def index(request):
    product_objects = Product.objects.all()

    # search bar
    item_name = request.GET.get('item_name')
    if item_name is not '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_objects = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_objects': product_objects})


def add_to_cart(request, id):
    user = request.user
    user_id = user.id

    def check_cart(user_id):
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return False

    cart = check_cart(user_id)
    if cart is False:
        cart = Cart(user_id=user_id)
        cart.save()
    else:
        cart = Cart.objects.get(user_id=user_id)
        product = Product.objects.get(id=id)
        quantity = request.GET.get('')
        cart_items = CartItems(product_id=product.id, cart_id=cart.id, quantity=quantity)
        cart_items.save()

    return render(request, 'shop/detail.html')


def payment(request):

    if request.method == "POST":
        price = request.GET.get('price')
        payment_status = request.GET.get('payment_status')

        payment = Payment(payment_status=payment_status, price=price)
        payment.save()

    return render(request, 'shop/checkout.html')
