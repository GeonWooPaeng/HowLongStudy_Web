from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.


def home(request):
    return render(request, 'home.html',{'email': request.session.get('user')})

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


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    
    return redirect('/')