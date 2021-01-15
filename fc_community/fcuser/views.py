from django.shortcuts import render, redirect
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse

# Create your views here.
def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username) 

    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def login(request):
    if request.method =='GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'

        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
            
                # 비밀번호가 일치, 로그인 처리   
                # 세션!
                request.session['user'] = fcuser.id
                # 홈으로 이동하는 리다이렉트 추가
                return redirect('/') #/만 사용하면 home으로 이동함.
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'


        return render(request, 'login.html', res_data)

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