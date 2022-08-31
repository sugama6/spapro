from django.shortcuts import render, redirect
from app.forms.admin_q_and_a import QandARegForm, QandAEditForm
from app.models import AdminUsers, QandA

import re

from .common import *


@admin_login_required
def G800_admin_q_and_a_list(request):
    q_and_a = QandA.objects.select_related('update_admin_user_id').filter(del_flg=0).order_by('sort')
    params = {
        'q_and_a_list': q_and_a
    }

    return render(request, 'admin_q_and_a/G800_admin_q_and_a_list.html', params)


@admin_login_required
def G810_admin_q_and_a_reg(request):
    params = {
        'form': QandARegForm()
    }
    if request.method == 'POST':
        params = {
            'form': QandARegForm(request.POST),
        }
    return render(request, 'admin_q_and_a/G810_admin_q_and_a_reg.html', params)


@admin_login_required
def G820_admin_q_and_a_reg_conf(request):
    if request.method == 'GET':
        return redirect('/G800_admin_q_and_a_list')
    if request.method == 'POST':
        params = {
            'request': request.POST
        }
    return render(request, 'admin_q_and_a/G820_admin_q_and_a_reg_conf.html', params)


@admin_login_required
def G830_admin_q_and_a_reg_comp(request):
    admin_login_id = request.session.get('admin_login_id')
    if request.method == 'GET':
        return redirect('/G800_admin_q_and_a_list')
    if request.method == 'POST':
        qa = QandA(
            update_admin_user_id=AdminUsers.objects.get(id=admin_login_id),
            question=request.POST['question'],
            answer=request.POST['answer'],
            sort=request.POST['sort'],
            insert_time=common_get_datetime(mode='day'),
            update_time=common_get_datetime(mode='day')
        )
        qa.save()
        params = {
            'question': request.POST['question'],
            'answer': request.POST['answer'],
            'redirect_url': 'G800_admin_q_and_a_list'
        }
        return render(request, 'admin_q_and_a/G830_admin_q_and_a_reg_comp.html', params)


@admin_login_required
def G831_admin_q_and_a_detail(request, id):
    qa = QandA.objects.get(id=id)
    params = {
        'qa': qa,
    }
    return render(request, 'admin_q_and_a/G831_admin_q_and_a_detail.html', params)


@admin_login_required
def G840_admin_q_and_a_edit(request, id):
    qa = QandA.objects.get(id=id, del_flg=0)
    admin_login_id = request.session.get('admin_login_id')
    params = {
        'qa': qa,
        'form': QandAEditForm(instance=qa)
    }
    if request.method == 'POST':
        form = QandAEditForm(request.POST, instance=qa)
        if form.is_valid():
            form = form.save(commit=False)
            form.update_admin_user_id = AdminUsers.objects.get(id=admin_login_id)
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect(f'/G831_admin_q_and_a_detail/{id}')
        else:
            params = {
                'qa': qa,
                'form': QandAEditForm(request.POST)
            }
    return render(request, 'admin_q_and_a/G840_admin_q_and_a_edit.html', params)


@admin_login_required
def G850_admin_q_and_a_del_conf(request, id): 
    qa = QandA.objects.get(id=id, del_flg=0)
    params = {
        'qa': qa
    }
    return render(request, 'admin_q_and_a/G850_admin_q_and_a_del_conf.html', params)


@admin_login_required
def G860_admin_q_and_a_del_comp(request, id):
    qa = QandA.objects.get(id=id, del_flg=0)
    params = {
        'question': qa.question,
        'redirect_url': 'G800_admin_q_and_a_list'
    }
    if request.method == 'GET':
        return redirect('/G800_admin_q_and_a_list')

    if request.method == 'POST':
        qa.del_flg = False
        qa.save()
        
    return render(request, 'admin_q_and_a/G860_admin_q_and_a_del_comp.html', params)