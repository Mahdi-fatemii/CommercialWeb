from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
# from .forms import RegisterForm

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

        user_check = User.objects.filter(username=username).first()
        if password == repeat_pass:
            # password_byte = str(password).encode()
            # salt = bcrypt.gensalt(rounds=12)
            # hashed_password = bcrypt.hashpw(password=password_byte, salt=salt)

            user = User(username=username, password=password, name=name, lastname=lastname,
                        email=email, address=address, mobile_number=mobile_number)
            user.save()
        return render(request, 'user/login.html')

    return render(request, 'user/register.html')


def user_log_in(request):

    def check_user(username):
        try:
            check = User.objects.get(username=username)
        except User.DoesNotExist:
            return False

    if request.method == "POST":
        username = request.GET.get('Username')
        password = request.GET.get('Password')

        user_check = check_user(username)
        if user_check is not False:

            user = User.objects.get(username=username)
            psw_check = bcrypt.checkpw(password, hashed_password=user.password)
            if psw_check is True:
                return render(request, 'user/profile.html', {'user': user})

    return render(request, 'user/login.html')
