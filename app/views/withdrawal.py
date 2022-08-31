from django.shortcuts import render, redirect
from app.models import Users
from app.forms.withdrawal import WithdrawalForm

from .common import *


@user_login_required
def G260_withdrawal(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    return render(request, 'withdrawal/G260_withdrawal.html', params)
    

@user_login_required
def G270_withdrawal_conf(request):
    if request.method == 'GET':
        return redirect('/G200_settings')
    if request.method == 'POST':
        login_id = request.session.get('login_id')
        user = Users.objects.get(id=login_id)
        params = {
            'user': user,
            'form': WithdrawalForm()
        }
    return render(request, 'withdrawal/G270_withdrawal_conf.html', params)
    

@user_login_required
def G280_withdrawal_comp(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    if request.method == 'GET':
        return redirect('/G200_settings')
    if request.method == 'POST':
        params = {
            'user': user,
            'form': WithdrawalForm(request.POST),
            'redirect_url': ''
        }
        request_password = common_hashing(request.POST['password'], 'sha256')
        if user.password == request_password:
            user.withdrawal = 1
            user.save()
            request.session.clear()
        else:
            params['error_message'] = '入力されたパスワードに誤りがあります。'
            return render(request, 'withdrawal/G270_withdrawal_conf.html', params)
    return render(request, 'withdrawal/G280_withdrawal_comp.html', params)
    