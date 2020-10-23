from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator 
from .forms import RegisterForm, LoginForm, SaveForm
from django.contrib.auth.hashers import make_password
from django.db import transaction 
from user.decorators import login_required
from .models import User
import json

from django.utils.decorators import method_decorator
from .decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html',{'email': request.session.get('user')})

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm 
    success_url = '/'

    def form_valid(self, form):
        user = User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save() 

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm 
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    
    return redirect('/')



# class SaveTime(FormView):
#     template_name = 'timer.html'
#     form_class = SaveForm
#     success_url = '/'

#     def form_valid(self, form):
#         with transaction.atomic():
#             user = User(
#                 user=User.objects.get(email=self.request.session.get('email')),
#                 # study_hour=form.data.get('study_hour'),
#                 # study_min=form.data.get('study_min'),
#                 # study_sec=json.loads(request.body)
#             )
#             user.save() 
#         return super().form_valid(form)

#     def get_form_kwargs(self, **kwargs):
#         kw = super().get_form_kwargs(**kwargs)
        
#         kw.update({
#             'request':self.request 
#         })
#         return kw 

def SaveTime(request):
    if not request.session.get('user'):
        return redirect('/login')

    # if request.method == 'POST':
    #     user = User(
    #         user=User.objects.get(email=request.session.get('user')),
    #         study_hour=form.data.get('study_hour'),
    #         study_min=form.data.get('study_min'),
    #         study_sec=int(time_data.get('study_sec',None))
    #         )
    #     user.save()
    
    return render(request, 'timer.html')