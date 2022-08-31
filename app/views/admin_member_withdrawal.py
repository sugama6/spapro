from django.shortcuts import render, redirect
from app.forms.admin_member import AdminUserEditForm
from app.models import Users
from django.db.models import Q

from .common import *



@admin_login_required
def G530_admin_member_withdrawal_list(request):
    user = Users.objects.filter(withdrawal=1).order_by('-update_time')
    params = {
        'users': user
    }
    if request.method == 'POST':
        output = request.POST['output']
        selector = request.POST['selector']

        # 氏名
        if request.POST['selector'] == '0':
            users = Users.objects.filter(Q(first_name__icontains=output)|Q(last_name__icontains=output), withdrawal=1).order_by('-update_time')
        # メールアドレス
        elif request.POST['selector'] == '1':
            users = Users.objects.filter(mail_address__icontains=output, withdrawal=1).order_by('-update_time')
        # 性別
        elif request.POST['selector'] == '2':
            users = Users.objects.filter(sex__icontains=output, withdrawal=1).order_by('-update_time')
        # 電話番号
        elif request.POST['selector'] == '3':
            users = Users.objects.filter(tel__icontains=output, withdrawal=1).order_by('-update_time')
        # 郵便番号
        elif request.rPOST['selector'] == '4':
            users = Users.objects.filter(postal_code__icontains=output, withdrawal=1).order_by('-update_time')
        # 住所
        elif request.POST['selector'] == '5':
            users = Users.objects.filter(address__icontains=output, withdrawal=1).order_by('-update_time')
        params = {
            'users': users
        }
    return render(request, 'admin_member_withdrawal/G530_admin_member_withdrawal_list.html', params)


@admin_login_required
def G540_admin_member_withdrawal_detail(request, id):
    user = Users.objects.get(id=id, withdrawal=1)
    params = {
        'user': user
    }
    return render(request, 'admin_member_withdrawal/G540_admin_member_withdrawal_detail.html', params)
