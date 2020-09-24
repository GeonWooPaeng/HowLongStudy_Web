from django import forms 
from .models import User 
from django.contrib.auth.hashers import make_password, check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        },
        max_length=32, label="사용자 이름")

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        #비밀번호가 일치하는지 확인
        cleaned_data = super().clean() 
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            
            except User.DoesNotExist:
                self.add_error('username','아이디가 없습니다.')
                return 

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')

            else:
                self.user_id = user.id 



class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        },
        max_length=32, label="사용자 이름")
    
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        }, 
        widget=forms.PasswordInput, label="비밀번호")

    re_password = forms.CharField(
        error_messages={
            'required': '확인 비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label="확인 비밀번호")
    
    def clean(self):
        cleaned_data = super().clean() 
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if username and password and re_password:
            if password != re_password:
                self.add_error('re_password', '확인 비밀번호랑 비밀번호가 같지 않습니다.')

            else:
                user = User(
                    username=username,
                    password=make_password(password)
                )
                user.save() 

