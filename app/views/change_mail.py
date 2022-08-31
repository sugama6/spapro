from django.shortcuts import render, redirect
from app.models import Users
from app.forms.chage_mail import changeMailForm

from .common import *


@user_login_required
def G210_change_mail(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'form': changeMailForm()
    }
    if request.method == 'POST':
        params = {
            'user': user,
            'form': changeMailForm(request.POST)
        }
    return render(request, 'change_mail/G210_change_mail.html', params)


@user_login_required
def G220_change_mail_conf(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'request': request.POST
    }
    if request.method == 'GET':
        return redirect('/G210_change_mail')
    if request.method == 'POST':
        form = changeMailForm(request.POST)
        error_params = {
            'user': user,
            'form': form
        }        
        # バリデーションチェック
        if form.is_valid():
            # ログインユーザーのメールアドレスが一致した時
            if Users.objects.filter(id=login_id, mail_address=request.POST['old_mail_address']).count() == 1:
                # 新しいメールアドレスと確認用メールアドレスが一致した時
                if request.POST['new_mail_address'] == request.POST['new_mail_address_conf']:
                    # 新しいメールアドレスの時が現在のメールアドレスと違う時
                    if request.POST['new_mail_address'] != request.POST['old_mail_address']:
                        params['mail_address'] = request.POST['new_mail_address']
                    else:
                        error_params['error_message'] = '現在のメールアドレスとは別のメールアドレスを入力してください。'
                        return render(request, 'change_mail/G210_change_mail.html', error_params)
                else:
                    error_params['error_message'] = '入力されたメールアドレスが一致しません。'
                    return render(request, 'change_mail/G210_change_mail.html', error_params)
            else:
                error_params['error_message'] = '入力されたメールアドレスに誤りがあります。'
                return render(request, 'change_mail/G210_change_mail.html', error_params)
        else:
            error_params['error_message'] = '入力されたメールアドレスに誤りがあります。'
            return render(request, 'change_mail/G210_change_mail.html', error_params)

    return render(request, 'change_mail/G220_change_mail_conf.html', params)


@user_login_required
def G230_change_mail_comp(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    if request.method == 'GET':
        return redirect('/G210_change_mail')
    if request.method == 'POST':
        user.mail_address = request.POST['new_mail_address']
        user.save()
        params = {
            'user': user,
            'redirect_url': 'G100_member_top'
        }
    return render(request, 'change_mail/G230_change_mail_comp.html', params)
