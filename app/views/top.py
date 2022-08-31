from django.shortcuts import render, redirect
from app.forms.top import LoginForm
from app.models import Users
from .common import *


def G010_top(request):
    return render(request, 'top/G010_top.html')
    
def G020_login(request):
    params = {
        'form': LoginForm(),
        'users': Users.objects.all()
    }
    if request.method == 'POST':
        login_id = request.POST['login_id']
        password = common_hashing(request.POST['password'], mode='sha256')
        
        if Users.objects.filter(login_id=login_id, password=password, withdrawal=0).count() == 1:
            request.session.clear()
            request.session['login_id'] = Users.objects.get(login_id=login_id, password=password).id
            return redirect('/G100_member_top')
        else:
            params = {
                'users': Users.objects.all(),
                'form': LoginForm(request.POST),
                'error': 'ログインID または パスワードが違います'
            }
            return render(request, 'top/G020_login.html', params)
    return render(request, 'top/G020_login.html', params)
    