from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User 
from .forms import LoginForm
# Create your views here.



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm() 
    
    return render(request, 'login.html', {'form': form})


def register(request): #회원가입
    if request.method == 'GET':
        return render(request, 'register.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and password):
            res_data['error'] = '모든 값을 입력해 주세요'
        
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        else:
            user = User(
                username=username,
                password=make_password(password)
            )

            user.save() 

        return render(request, 'register.html', res_data)