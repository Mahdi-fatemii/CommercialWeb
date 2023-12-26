from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator
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


def checkout(request):

    if request.method == "POST":
        name = request.POST.get('name', "")
        lastname = request.POST.get('LastName', "")
        email = request.POST.get('Email', "")
        address = request.POST.get('Address', "")
        city = request.POST.get('City', "")
        state = request.POST.get('State', "")
        zipcode = request.POST.get('ZipCode', "")

        order = Order(name=name, lastname=lastname, email=email, address=address, city=city, state=state, zipcode=zipcode)
        order.save()

    return render(request, 'shop/checkout.html')
