from django.shortcuts import render, redirect
from app.models import Users

from .common import *


# 使わない

@admin_login_required
def G500_admin_forced_withdrawal(request):
    return render(request, 'admin_forced_withdrawal/G500_admin_forced_withdrawal.html')


@admin_login_required
def G510_admin_forced_withdrawal_conf(request, id):
    params = {
        'user': Users.objects.get(id=id, withdrawal=0)
    }
    return render(request, 'admin_forced_withdrawal/G510_admin_forced_withdrawal_conf.html', params)


@admin_login_required
def G520_admin_forced_withdrawal_comp(request, id):
    if request.method == 'GET':
        return redirect('/G440_admin_member_list')
    user = Users.objects.get(id=id, withdrawal=0)
    params = {
        'user': user
    }
    if request.method == 'POST':
        user.withdrawal = 1
        user.save()
    return render(request, 'admin_forced_withdrawal/G520_admin_forced_withdrawal_comp.html', params)
