from django.shortcuts import render, redirect
from app.forms.member_reg import UserRegForm, UserEditForm
from app.models import Users

from django.db.models import Max

from .common import *


def G070_reg(request):
    # login_id = request.session.get('login_id')
    # user = Users.objects.get(id=login_id)
    params = {
        'form': UserRegForm(),
        # 'user': user
    }
    if request.method == 'POST':
        params['form'] = UserRegForm(request.POST)
    return render(request, 'member_reg/G070_reg.html', params)


def G080_reg_conf(request):
    if request.method == 'GET':
        return redirect('/G070_reg')
    params = {
        'request': request.POST,
        'form': UserRegForm(),
    }
    if request.method == 'POST':
        params['form'] = UserRegForm(request.POST)
        form = UserRegForm(request.POST)
        if form.is_valid():
            #パスワードが一致しない時、エラー
            if request.POST['password'] != request.POST['password2']:
                params ['pass_error'] = 'パスワードが一致しません'
                return render(request, 'member_reg/G070_reg.html', params)
            #入力が正しい時
            # params = {'request': request.POST,}
            return render(request, 'member_reg/G080_reg_conf.html', params)
        #バリデーションエラー時
        else :
            # params['form'] = UserRegForm(request.POST)}
            return render(request, 'member_reg/G070_reg.html', params)
    return render(request, 'member_reg/G080_reg_conf.html', params)


def G090_reg_comp(request):
    if request.method == 'GET':
        return redirect('/G070_reg')

    if request.method == 'GET':
        return redirect('/G100_member_top')

    if request.method == 'POST':
        # if Users.objects.all().count() == 0:
        #     max_id = 1
        # else:
        #     max_id = Users.objects.all().aggregate(Max('id'))['id__max']
        
        while True:
            login_id = common_random_id()
            login_id_check = Users.objects.filter(login_id=login_id).count()
            if login_id_check == 0:
                break
            else:
                pass
        try:
            user = Users(
                last_name=request.POST['last_name'],
                first_name=request.POST['first_name'],
                mail_address=request.POST['mail_address'],
                login_id=login_id,
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
                'data': request.POST,
                'login_id': login_id,
            }
            common_send_email(
                to_email_address=request.POST['mail_address'],
                subject='【スパプロ塾】会員登録完了',
                contents=f'この度はスパプロ塾にご登録いただき誠にありがとうございます。\n下記のIDはログインの際に必要になりますので、必ず無くさないようにしてください。\nログインID: {login_id}\n\n↓↓ ログインはこちら ↓↓\n\http://localhost:8000/G020_login'
            )

        #情報に誤りがあるとき
        except Exception as e:
            print(f'ERROR\n{e}')
        return render(request, 'member_reg/G090_reg_comp.html')


@user_login_required
def G100_member_top(request):
    user_id = request.session.get('login_id')
    user = Users.objects.get(id=user_id)
    params = {
        'user': user
    }
    return render(request, 'member_reg/G100_member_top.html', params)
    

@user_login_required
def G110_edit(request):
    user_id = request.session.get('login_id')
    user = Users.objects.get(id=user_id)
    params = {
        'form': UserEditForm(instance=user),
        'user': user
    }
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect('/G100_member_top')
            # params['form'] = UserEditForm(request.POST, instance=obj)
        else:
            params['form'] = UserEditForm(request.POST)
    return render(request, 'member_reg/G110_edit.html', params)
    