from django.shortcuts import render, redirect
from app.forms.admin_list import AdminEditForm
from app.models import AdminUsers

from .common import *


@admin_login_required
def G550_admin_list(request):
    params = {
        'admin_users': AdminUsers.objects.filter(del_flg=0)
    }
    return render(request, 'admin_list/G550_admin_list.html', params)


@admin_login_required
def G560_admin_detail(request, id):
    params = {
        # 'id': id,
        'admin': AdminUsers.objects.get(id=id)
    }
    return render(request, 'admin_list/G560_admin_detail.html', params)


@admin_login_required
def G561_admin_edit(request, id):
    admin_user = AdminUsers.objects.get(id=id)
    params = {
        'id': id,
        'admin': admin_user,
        'form': AdminEditForm(instance=admin_user)
    }
    if request.method == 'POST':
        form = AdminEditForm(request.POST, instance=admin_user)
        if form.is_valid():
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect(f'/G560_admin_detail/{id}')
        else:
            params['form'] = AdminEditForm(request.POST)
    return render(request, 'admin_list/G561_admin_edit.html', params)


@admin_login_required
def G570_admin_del_conf(request, id):
    admin_user = AdminUsers.objects.get(id=id)
    params = {
        'id': id,
        'admin': admin_user
    }
    return render(request, 'admin_list/G570_admin_del_conf.html', params)


@admin_login_required
def G580_admin_del_comp(request, id):
    if request.method == 'GET':
        return redirect('/G550_admin_list')
    if request.method == 'POST':
        admin_user = AdminUsers.objects.get(id=id)
        params = {
            'id': id,
            'admin': admin_user,
            'redirect_url': 'G550_admin_list'
        }
        admin_user.del_flg = 1
        admin_user.save()
    
    return render(request, 'admin_list/G580_admin_del_comp.html', params)
