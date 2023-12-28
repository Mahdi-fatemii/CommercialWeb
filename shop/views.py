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


def user_sign_up(request):

    def check_user(username):
        try:
            check = User.objects.get(username=username)
        except User.DoesNotExist:
            return False

    if request.method == "POST":
        username = request.GET.get('price')
        password = request.GET.get('price')
        name = request.GET.get('price')
        lastname = request.GET.get('price')
        email = request.GET.get('price')
        address = request.GET.get('price')
        mobile_number = request.GET.get('price')

        # user_check = User.objects.filter(username=username).first()
        user_check = check_user(username)
        if user_check is not False:
            salt = bcrypt.gensalt(rounds=12)
            hashed_password = bcrypt.hashpw(password=password, salt=salt)

            user = User(username=username, password=hashed_password, name=name, lastname=lastname,
                        email=email, address=address, mobile_number=mobile_number)
            user.save()
        else:
            return render(request, 'user/signup.html')
    return render(request, 'user/login.html')


# def add_to_cart(request, id):


def user_log_in(request):

    def check_user(username):
        try:
            check = User.objects.get(username=username)
        except User.DoesNotExist:
            return False

    if request.method == "POST":
        username = request.GET.get('price')
        password = request.GET.get('price')

        user_check = check_user(username)
        if user_check is not False:

            user = User.objects.get(username=username)
            psw_check = bcrypt.checkpw(password, hashed_password=user.password)
            if psw_check is True:
                return render(request, 'user/profile.html', {'user': user})
            else:
                return render(request, 'user/login.html')


def payment(request):

    if request.method == "POST":
        price = request.GET.get('price')
        payment_status = request.GET.get('payment_status')

        payment = Payment(payment_status=payment_status, price=price)
        payment.save()

    return render(request, 'shop/checkout.html')
