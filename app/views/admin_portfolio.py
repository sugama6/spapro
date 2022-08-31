from django.shortcuts import render, redirect
from app.forms.admin_portfolio import AdminPortfolioEditForm
from app.models import Users, Portfolio

import re

from .common import *


@admin_login_required
def G700_admin_portfolio_list(request, sort='normal'):
    if sort == 'normal':
        portfolio = Portfolio.objects.select_related('user_id').all().order_by('-insert_time')
        # portfolio = Portfolio.objects.select_related('user_id').filter(del_flg=0).order_by('-insert_time')
        order_by = 'reverse'
    elif sort == 'reverse':
        portfolio = Portfolio.objects.select_related('user_id').all().order_by('insert_time')
        # portfolio = Portfolio.objects.select_related('user_id').filter(del_flg=0).order_by('insert_time')
        order_by = 'normal'
    
    params = {
        'portfolio': portfolio,
        'order_by': order_by
    }
    return render(request, 'admin_portfolio/G700_admin_portfolio_list.html', params)


@admin_login_required
def G701_admin_portfolio_detail(request, id):
    portfolio = Portfolio.objects.get(id=id)
    params = {
        'portfolio': portfolio
    }
    return render(request, 'admin_portfolio/G701_admin_portfolio_detail.html', params)


@admin_login_required
def G710_admin_portfolio_edit(request, id):
    portfolio = Portfolio.objects.select_related('user_id').get(id=id)
    params = {
        'portfolio': portfolio,
        'form': AdminPortfolioEditForm(instance=portfolio)
    }
    if request.method == 'POST':
        form = AdminPortfolioEditForm(request.POST, instance=portfolio)
        if form.is_valid():
            form = form.save(commit=False)

            if request.FILES.get('image'):
                if re.search('.*[.png|.jpeg|.jpg|.gif]$', request.FILES.get('image').name):
                    form.image = common_uploaded_file(file=request.FILES['image'], new_dir_path='/')
                else:
                    params['image_error'] = '画像は png jpeg jpg gifのいずれかでアップロードしてください。' 
                    return render(request, 'admin_portfolio/G710_admin_portfolio_edit.html', params)
            else:
                form.image = portfolio.image
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect(f'/G701_admin_portfolio_detail/{id}')
        else:
            params['form'] = AdminPortfolioEditForm(request.POST) 
    return render(request, 'admin_portfolio/G710_admin_portfolio_edit.html', params)


@admin_login_required
def G711_admin_portfolio_delete_conf(request, id):
    portfolio = Portfolio.objects.select_related('user_id').get(id=id)
    params = {
        'portfolio': portfolio
    }
    return render(request, 'admin_portfolio/G711_admin_portfolio_delete_conf.html', params)


@admin_login_required
def G712_admin_portfolio_delete_comp(request, id):
    portfolio = Portfolio.objects.select_related('user_id').get(id=id)
    params = {
        'portfolio': portfolio,
        'redirect_url': 'G700_admin_portfolio_list'
    }
    if request.method == 'GET':
        return redirect('/G700_admin_portfolio_list/normal')

    if request.method == 'POST':
        portfolio.del_flg = 1
        portfolio.save()
    return render(request, 'admin_portfolio/G711_admin_portfolio_delete_conf.html', params)