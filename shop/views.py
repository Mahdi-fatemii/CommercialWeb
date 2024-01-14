from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import *


from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
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


def payment_finder(cart):
    try:
        payment = Payment.objects.get(cart_id=cart)
    except Payment.DoesNotExist:
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
            cart = Cart(user=user, cart_status="pending", total_price=0)
            cart.save()
        else:
            cart_item = cart_item_finder(id)
            cart = Cart.objects.get(user=user)
            product_objects = Product.objects.get(id=id)
            if cart_item is False:
                cart_items = CartItem(product_id=product_objects, cart_id=cart, quantity=1)
                cart_items.save()
                return render(request, 'shop/detail.html', {'product_objects': product_objects})
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
            return render(request, 'shop/index.html')
        else:
            user_cart = Cart.objects.get(user=user)
            cart_item = CartItem.objects.filter(cart_id=user_cart)
            total = 0
            payment_status = payment_finder(user_cart)
            for item in cart_item:
                cart_item_price_t = item.quantity * item.product_id.price
                total += cart_item_price_t
                user_cart.total_price = total
                user_cart.save()

            if payment_status is False:
                payment = Payment(cart_id=user_cart, payment_status='pending', price=total)
                payment.save()

            else:
                payment = Payment.objects.get(cart_id=user_cart)
                payment.price = total
                payment.save()

            if request.method == 'POST':
                form = PaymentInfoForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('payment')
            else:
                form = PaymentInfoForm()
            return render(request, 'shop/cart.html', {'user_cart': user_cart, 'cart_item': cart_item, 'form': form})
    else:
        return redirect('login')


@login_required()
def checkout(request):
    # user = request.user
    # if user.is_authenticated:
    #     cart_status = cart_finder(user)
    #     if cart_status is True:
    #         user_cart = Cart.objects.filter(user=user, cart_status='pending').first()
    #
    #         r = request.POST('https://sandbox.shepa.com/api/v1/token', data={
    #             'api': "sandbox",
    #             'amount': user_cart.total_price,
    #             'callback': "http://localhost:5000/verify"
    #         })
    #         token = r.json()['result']['token']
    #         url = r.json()['result']['url']
    #
    #         payment = Payment.objects.get(cart_id=user_cart)
    #         payment.token = token
    #         payment.save()
    #
    #         return redirect(url)
    return render(request, 'shop/payment.html')

#
# def verify(request):
#     user = request.user
#     if user.is_authenticated:
#         cart_status = cart_finder(user)
#         if cart_status is True:
#             user_cart = Cart.objects.filter(user=user, cart_status='pending').first()
#             payment = Payment.objects.get(cart_id=user_cart)
#             token = request.args.get('token')
#             payment = Payment.objects.filter(token=token).first_or_404()
#
#             r = request.POST('https://sandbox.shepa.com/api/v1/verify', data={
#                     'api': 'sandbox',
#                     'amount': payment.price,
#                     'token': token
#             })
#
#             pay_status = bool(r.json()['success'])
#
#             if pay_status:
#                 transaction_id = r.json()['result']['transaction_id']
#                 refid = r.json()['result']['refid']
#                 card_pan = r.json()['result']['card_pan']
#
#                 payment.card_pan = card_pan
#                 payment.transaction_id = transaction_id
#                 payment.refid = refid
#                 payment.status = 'success'
#                 payment.cart.status = 'purchased'
#                     # flash('payment was successful')
#             else:
#                     # flash('payment was not successful')
#                 payment.status = 'failed'
#
#             payment.save()
#
#             return redirect('profile')
