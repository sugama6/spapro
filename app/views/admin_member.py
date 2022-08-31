from django.shortcuts import render, redirect
from app.forms.admin_member import AdminUserEditForm
from app.models import Users, AdminUsers
from django.db.models import Q

from .common import *


@admin_login_required
def G440_admin_member_list(request):
    admin_login_id = request.session.get('admin_login_id')
    admin_user = AdminUsers.objects.get(id=admin_login_id)

    users = Users.objects.filter(withdrawal=0).order_by('-join_time')
    params = {
        'users': users
    }
    if request.method == 'POST':
        output = request.POST['output']
        selector = request.POST['selector']
        # 氏名
        if request.POST['selector'] == '0':
            users = Users.objects.filter(Q(first_name__icontains=output)|Q(last_name__icontains=output), withdrawal=0).order_by('-join_time')
        # メールアドレス
        elif request.POST['selector'] == '1':
            users = Users.objects.filter(mail_address__icontains=output, withdrawal=0).order_by('-join_time')
        # 性別
        elif request.POST['selector'] == '2':
            users = Users.objects.filter(sex__icontains=output, withdrawal=0).order_by('-join_time')
        # 電話番号
        elif request.POST['selector'] == '3':
            users = Users.objects.filter(tel__icontains=output, withdrawal=0).order_by('-join_time')
        # 郵便番号
        elif request.rPOST['selector'] == '4':
            users = Users.objects.filter(postal_code__icontains=output, withdrawal=0).order_by('-join_time')
        # 住所
        elif request.POST['selector'] == '5':
            users = Users.objects.filter(address__icontains=output, withdrawal=0).order_by('-join_time')
        params = {
            'users': users
        }
    return render(request, 'admin_member/G440_admin_member_list.html', params)


@admin_login_required
def G450_admin_member_detail(request, id):
    admin_login_id = request.session.get('admin_login_id')
    admin_user = AdminUsers.objects.get(id=admin_login_id)

    user = Users.objects.get(id=id)
    params = {
        'user': user
    }
    return render(request, 'admin_member/G450_admin_member_detail.html', params)


@admin_login_required
def G460_admin_member_edit(request, id):
    admin_login_id = request.session.get('admin_login_id')
    admin_user = AdminUsers.objects.get(id=admin_login_id)

    user = Users.objects.get(id=id)
    params = {
        'user': user,
        'form': AdminUserEditForm(instance=user)
    }
    if request.method == 'POST':
        form = AdminUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect(f'/G450_admin_member_detail/{id}')
        else:
            params['form'] = AdminEditForm(request.POST)
    return render(request, 'admin_member/G460_admin_member_edit.html', params)
