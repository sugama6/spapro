from django.shortcuts import render, redirect
from app.forms.admin_reg import AdminUserRegForm
from app.models import AdminUsers

from .common import *

import traceback


@admin_login_required
def G410_admin_reg(request):
    # admin_login_id = request.session.get('admin_login_id')
    # admin_user = AdminUsers.objects.get(id=admin_login_id)
    
    params = {
        'form': AdminUserRegForm()
    }
    if request.method == 'POST':
        params = {
            'form': AdminUserRegForm(request.POST)
        }
    return render(request, 'admin_reg/G410_admin_reg.html', params)
    

@admin_login_required
def G420_admin_reg_conf(request):
    # admin_login_id = request.session.get('admin_login_id')
    # admin_user = AdminUsers.objects.get(id=admin_login_id)
    
    params = {
        'request': request.POST,
        'form': AdminUserRegForm()
    }
    if request.method == 'POST':
        params = {
            'request': request.POST,
            'form': AdminUserRegForm(request.POST)
        }
        form = AdminUserRegForm(request.POST)
        if form.is_valid():
            #パスワードが一致しない時、エラー
            if request.POST['password'] != request.POST['password2']:
                params = {
                    'form': AdminUserRegForm(request.POST),
                    'pass_error': 'パスワードが一致しません'
                }
                return render(request, 'admin_reg/G410_admin_reg.html', params)
            #入力が正しい時
            params = {'request': request.POST,}
            return render(request, 'admin_reg/G420_admin_reg_conf.html', params)
        #バリデーションエラー時
        else :
            params = {'form': AdminUserRegForm(request.POST)}
            return render(request, 'admin_reg/G410_admin_reg.html', params)
    return render(request, 'admin_reg/G420_admin_reg_conf.html', params)
    

@admin_login_required
def G430_admin_reg_comp(request):
    # admin_login_id = request.session.get('admin_login_id')
    # admin_user = AdminUsers.objects.get(id=admin_login_id)
    
    if request.method == 'GET':
        return redirect('/G550_admin_list')

    if request.method == 'POST':
        try:
            user = AdminUsers(
                last_name=request.POST['last_name'],
                first_name=request.POST['first_name'],
                mail_address=request.POST['mail_address'],
                password=common_hashing(request.POST['password'], 'sha256'),
                sex=request.POST['sex'],
                tel=request.POST['tel'],
                postal_code=request.POST['postal_code'],
                prefectures=request.POST['prefectures'],
                municipalities=request.POST['municipalities'],
                address=request.POST['address'],
                apartment_mansion=request.POST['apartment_mansion'],
                join_time = common_get_datetime(),
                update_time = common_get_datetime(),
            )
            user.save()
            params = {
                'admin_name': request.POST['last_name'] + request.POST['first_name'],
                'redirect_url': 'G440_admin_member_list'
            }
            common_send_email(
                to_email_address=request.POST['mail_address'],
                subject='【スパプロ塾】管理者登録完了',
                contents='あなたのアカウントがスパプロ塾の管理者として登録されました。\n下記からログインしてください。\n\n・ログインID: {0}\n・{1}\n\n↓↓ ログインはこちら ↓↓\n\http://localhost:8000/G400_admin_login'\
                    .format(request.POST['mail_address'], request.POST['password'])
            )

        #情報に誤りがあるとき
        except Exception as e:
            traceback.print_exc()
            print(f'ERROR\n{e}')
    return render(request, 'admin_reg/G430_admin_reg_comp.html', params)