from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required':'아이디를 입력해주세요.'
        },
        max_length=32, label = '사용자 이름')
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label ='비밀번호')

# 비밀번호 일치 여부를 확인.
    def clean(self):
        cleaned_data = super().clean() #입력하지 않았다면, 여기서 거절됨.
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '해당 아이디가 존재하지 않습니다.')
                return
                
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
            else:
                self.user_id = fcuser.id