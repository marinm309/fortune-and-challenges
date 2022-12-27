from django.views import generic as views
from . forms import CustomAuthenticationForm, SignUpForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin


UserModel = get_user_model()

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)
    


class UserCreationView(SuccessMessageMixin, views.CreateView):
    template_name = 'users/register.html'
    form_class = SignUpForm
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(UserCreationView, self).dispatch(request, *args, **kwargs)

    
class UserLogoutView(LogoutView):
    pass

