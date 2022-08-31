from django.shortcuts import render, redirect
from app.forms.portfolio import PortfolioRegForm
from app.models import Users, Portfolio

import re

from .common import *

@user_login_required
def G290_portfolio(request, sort='normal'):
    login_id = request.session.get('login_id')

    user = Users.objects.get(id=login_id)
    # portfolio = Portfolio.objects.filter(del_flg=0)
    if sort == 'normal':
        portfolio = Portfolio.objects.all().order_by('-insert_time')
        order_by = 'reverse'
    elif sort == 'reverse':
        portfolio = Portfolio.objects.all().order_by('insert_time')
        order_by = 'normal'
    params = {
        'user': user,
        'portfolio': portfolio,
        'order_by': order_by

    }
    return render(request, 'portfolio/G290_portfolio.html', params)
    

@user_login_required
def G300_portfolio_reg(request):

    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'form': PortfolioRegForm()
    }

    if request.method == 'POST':
        params = {
            'user': user,
            'form': PortfolioRegForm(request.POST)
        }
    return render(request, 'portfolio/G300_portfolio_reg.html', params)
    

@user_login_required
def G310_portfolio_conf(request):

    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)

    if request.method == 'GET':
        return redirect('/G290_portfolio/normal')

    params = {}
    if request.method == 'POST':
        form = PortfolioRegForm(request.POST)
        if form.is_valid():
            params = {
                'user': user,
                'request': request.POST,
                # 'request': 
            }
            if request.FILES.get('image'):
                if re.search('.*[.png|.jpeg|.jpg|.gif]$', request.FILES.get('image').name):
                    params['image'] = common_uploaded_file(file=request.FILES['image'], new_dir_path='/')
                else:
                    params['image_error'] = '画像は png jpeg jpg gifのいずれかでアップロードしてください。' 
                    return render(request, 'portfolio/G300_portfolio_reg.html', params)
            return render(request, 'portfolio/G310_portfolio_conf.html', params)
        else:
            params = {
                'user': user,
                'form': PortfolioRegForm(request.POST)
            }
            return render(request, 'portfolio/G300_portfolio_reg.html', params)
    return render(request, 'portfolio/G310_portfolio_conf.html', params)
    

@user_login_required
def G320_portfolio_comp(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    if request.method == 'GET':
        return redirect('/G020_login')
    
    if request.method == 'POST':
        portfolio = Portfolio(
            user_id=user,
            url=request.POST['url'],
            image=request.POST['image'],
            title=request.POST['title'],
            content=request.POST['content'],
            release_flg=request.POST['release_flg'],
            insert_time=common_get_datetime(mode='day'),
            update_time=common_get_datetime(mode='day')
        )
        portfolio.save()
        params = {
            'portfolio_title': request.POST['title'],
            'redirect_url': 'G290_portfolio/normal'
        }
    return render(request, 'portfolio/G320_portfolio_comp.html', params)
    

@user_login_required
def G321_my_portfolio_list(request, sort='normal'):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    if sort == 'normal':
        my_portfolio = Portfolio.objects.filter(user_id=login_id).order_by('-insert_time')
        order_by = 'reverse'
    elif sort == 'reverse':
        my_portfolio = Portfolio.objects.filter(user_id=login_id).order_by('insert_time')
        order_by = 'normal'
    params = {
        'user': user,
        'portfolio': my_portfolio,
        'order_by': order_by
    }
    return render(request, 'portfolio/G321_my_portfolio_list.html', params)
    

@user_login_required
def G330_portfolio_edit(request, id):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    portfolio = Portfolio.objects.get(id=id)
    params = {
        'user': user,
        'portfolio': portfolio,
        'form': PortfolioRegForm(instance=portfolio)
    }
    if request.method == 'POST':
        form = PortfolioRegForm(request.POST, instance=portfolio)
        if form.is_valid():
            form = form.save(commit=False)

            if request.FILES.get('image'):
                if re.search('.*[.png|.jpeg|.jpg|.gif]$', request.FILES.get('image').name):
                    form.image = common_uploaded_file(file=request.FILES['image'], new_dir_path='/')
                else:
                    params['image_error'] = '画像は png jpeg jpg gifのいずれかでアップロードしてください。' 
                    return render(request, 'portfolio/G330_portfolio_edit.html', params)
            else:
                form.image = portfolio.image
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect('/G321_my_portfolio_list')
        else:
            params['form'] = PortfolioRegForm(request.POST)
    return render(request, 'portfolio/G330_portfolio_edit.html', params)
    