from django.shortcuts import render
from .models import Fcuser
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        #입력값이 공란일 떄, 생성되지 않도록 예외처리한다.
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        

        res_data = {}
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        else:
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
        )

            fcuser.save()
            res_data['clear'] = '회원등록이 완료되었습니다.'

        return render(request, 'register.html', res_data) 