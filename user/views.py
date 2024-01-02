import bcrypt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as UserMain
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate

# Create your views here.


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome {username}.')
#             return render(request, 'user/login.html')
#     else:
#         form = RegisterForm()
#     return render(request, 'user/register.html', {'form': form})


@login_required
def profile_page(request):
    return render(request, 'user/profile.html')


def register(request):

    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        repeat_pass = request.POST.get('Repeat_Password')
        name = request.POST.get('Name')
        lastname = request.POST.get('LastName')
        email = request.POST.get('Email')
        address = request.POST.get('Address')
        mobile_number = request.POST.get('Mobile_Number')

        if User.objects.filter(username=username).first():
            messages.error(request, "This username is Invalid")
            return render(request, 'user/register.html')
        else:
            if password == repeat_pass:
                password_byte = str(password).encode('utf-8')
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password=password_byte, salt=salt)
                hashed_password1 = hashed_password.decode('utf-8')
                user = User(username=username, password=hashed_password1, name=name, lastname=lastname,
                            email=email, address=address, mobile_number=mobile_number)
                user.save()
                user_main = UserMain.objects.create_user(username, email, password)
                user_main.save()
            return render(request, 'user/login.html')
    return render(request, 'user/register.html')


def user_log_in(request):

    if request.method == "POST":
        username = request.GET.get('Username')
        password = request.GET.get('Password')
        main_user = authenticate(username=username, password=password)
        if main_user is not None:
            user = User.objects.get(username=username)
            return render(request, 'user/profile.html', {'user': user})
        else:
            messages.error(request, "Wrong username or password")
            return render(request, 'user/login.html')
    return render(request, 'user/login.html')


