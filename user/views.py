from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import CustomUser


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('email')
            # messages.success(request, f'Welcome {username}.')
            return render(request, 'user/login.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


@login_required
def profile_page(request):
    user = request.user
    custom_user = CustomUser.objects.get(email=user.email)
    return render(request, 'user/profile.html', {'user': user, 'custom_user': custom_user})


