from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm 
    success_url = '/'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm 
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.email
        return super().form_valid(form)