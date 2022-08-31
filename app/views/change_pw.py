from django.shortcuts import render, redirect
from app.models import Users
from app.forms.change_pw import changePWForm

from .common import *


@user_login_required
def G240_change_pw(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'form': changePWForm()
    }
    if request.method == 'POST':
        params = {
            'user': user,
            'form': changePWForm(request.POST)
        }
    return render(request, 'change_pw/G240_change_pw.html', params)


@user_login_required
def G241_change_pw_conf(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'request': request.POST
    }

    if request.method == 'GET':
        return redirect('/G240_change_pw')

    if request.method == 'POST':
        form = changePWForm(request.POST)
        error_params = {
            'user': user,
            'form': form
        }        
        # バリデーションチェック
        if form.is_valid():
            # ログインユーザーのパスワードが一致した時
            if Users.objects.filter(id=login_id, password=old_password).count() == 1:
                # 新しいパスワードと確認用パスワードが一致した時
                if new_password == new_password_conf:
                    # 新しいパスワードの時が現在のパスワードと違う時
                    if new_password != old_password:
                        params['password'] = new_password
                    else:
                        error_params['error_message'] = '現在のパスワードとは別のパスワードを入力してください。'
                        return render(request, 'change_pw/G240_change_pw.html', error_params)
                else:
                    error_params['error_message'] = '入力されたパスワードが一致しません。'
                    return render(request, 'change_pw/G240_change_pw.html', error_params)
            else:
                error_params['error_message'] = '入力されたパスワードに誤りがあります。'
                return render(request, 'change_pw/G240_change_pw.html', error_params)
        else:
            error_params['error_message'] = '入力されたパスワードに誤りがあります。'
            return render(request, 'change_pw/G240_change_pw.html', error_params)
    return render(request, 'change_pw/G241_change_pw_conf.html', params)
    

@user_login_required
def G250_change_pw_comp(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'request': request.POST,
        'redirect_url': 'G100_member_top'
    }

    if request.method == 'GET':
        return redirect('/G240_change_pw')

    if request.method == 'POST':
        form = changePWForm(request.POST)
        error_params = {
            'user': user,
            'form': form
        }        
        old_password = common_hashing(request.POST['old_password'], 'sha256')
        new_password = common_hashing(request.POST['new_password'], 'sha256')
        new_password_conf = common_hashing(request.POST['new_password_conf'], 'sha256')
        # バリデーションチェック
        if form.is_valid():
            # ログインユーザーのパスワードが一致した時
            if Users.objects.filter(id=login_id, password=old_password).count() == 1:
                # 新しいパスワードと確認用パスワードが一致した時
                if new_password == new_password_conf:
                    # 新しいパスワードの時が現在のパスワードと違う時
                    if new_password != old_password:
                        user.password = new_password
                        user.save()
                    else:
                        error_params['error_message'] = '現在のパスワードとは別のパスワードを入力してください。'
                        return render(request, 'change_pw/G240_change_pw.html', error_params)
                else:
                    error_params['error_message'] = '入力されたパスワードが一致しません。'
                    return render(request, 'change_pw/G240_change_pw.html', error_params)
            else:
                error_params['error_message'] = '入力されたパスワードに誤りがあります。'
                return render(request, 'change_pw/G240_change_pw.html', error_params)
        else:
            error_params['error_message'] = '入力されたパスワードに誤りがあります。'
            return render(request, 'change_pw/G240_change_pw.html', error_params)

    return render(request, 'change_pw/G250_change_pw_comp.html', params)
    