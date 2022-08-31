from django.shortcuts import render, redirect
from app.forms.admin_news import NewsRegForm
from app.models import AdminUsers, News

import re

from .common import *
    

@admin_login_required
def G720_admin_news_list(request):
    admin_login_id = request.session.get('admin_login_id')
    admin_user = AdminUsers.objects.get(id=admin_login_id)

    news = News.objects.select_related('admin_user_id').all().order_by('-insert_time')
    # news = News.objects.select_related('admin_user_id').filter(del_flg=0).order_by('-insert_time')
    params = {
        'news': news
    }
    return render(request, 'admin_news/G720_admin_news_list.html', params)


@admin_login_required
def G730_admin_news_reg(request):
    admin_login_id = request.session.get('admin_login_id')
    admin_user = AdminUsers.objects.get(id=admin_login_id)
    params = {
            'form': NewsRegForm()
        }
    if request.method == 'POST':
        params['form'] = NewsRegForm(request.POST)
    return render(request, 'admin_news/G730_admin_news_reg.html', params)


@admin_login_required
def G740_admin_news_reg_conf(request):
    admin_login_id = request.session.get('admin_login_id')
    admin_user = AdminUsers.objects.get(id=admin_login_id)

    if request.method == 'GET':
        return redirect('/G720_admin_news_list')
    
    if request.method == 'POST':
        form = NewsRegForm(request.POST)
        if form.is_valid():
            params = {
                'request': request.POST
            }
            if request.FILES.get('image'):
                if re.search('.*[.png|.jpeg|.jpg|.gif]$', request.FILES.get('image').name):
                    params['image'] = common_uploaded_file(file=request.FILES['image'], new_dir_path='/')
                else:
                    params['image_error'] = '画像は png jpeg jpg gifのいずれかでアップロードしてください。' 
                    return render(request, 'admin_news/G730_admin_news_reg.html', params)
        else:
            pramas = {
                'form': NewsRegForm(request.POST),
            }
            return render(request, 'admin_news/G730_admin_news_reg.html', params)
    return render(request, 'admin_news/G740_admin_news_reg_conf.html', params)


@admin_login_required
def G750_admin_news_reg_comp(request):
    admin_login_id = request.session.get('admin_login_id')
    admin_user = AdminUsers.objects.get(id=admin_login_id)
    
    if request.method == 'GET':
        return redirect('/G720_admin_news_list')
    if request.method == 'POST':
        news = News(
            admin_user_id=AdminUsers.objects.get(id=admin_login_id),
            title=request.POST['title'],
            content=request.POST['content'],
            image=request.POST['image'],
            insert_time=common_get_datetime(mode='day'),
            update_time=common_get_datetime(mode='day')
        )
        news.save()
        params = {
            'news_title': request.POST['title'],
            'redirect_url': 'G720_admin_news_list'
        }
    return render(request, 'admin_news/G750_admin_news_reg_comp.html', params)


@admin_login_required
def G760_admin_news_detail(request, id):
    news = News.objects.select_related('admin_user_id').get(id=id)
    params = {
        'news': news
    }
    return render(request, 'admin_news/G760_admin_news_detail.html', params)


@admin_login_required
def G770_admin_news_edit(request, id):
    news = News.objects.get(id=id)
    params = {
        'news': news,
        'form': NewsRegForm(instance=news)
    }
    if request.method == 'POST':
        form = NewsRegForm(request.POST, instance=news)
        if form.is_valid():
            form = form.save(commit=False)
            if request.FILES.get('image'):
                if re.search('.*[.png|.jpeg|.jpg|.gif]$', request.FILES.get('image').name):
                    form.image = common_uploaded_file(file=request.FILES['image'], new_dir_path='/')
                else:
                    params['image_error'] = '画像は png jpeg jpg gifのいずれかでアップロードしてください。' 
                    return render(request, 'admin_portfolio/G770_admin_news_edit.html', params)
            else:
                form.image = news.image
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect(f'/G760_admin_news_detail/{id}')
        else:
            params = {
                'form': NewsRegForm(request.POST)
            }
    return render(request, 'admin_news/G770_admin_news_edit.html', params)


@admin_login_required
def G780_admin_news_delete_conf(request, id):
    news = News.objects.get(id=id)
    params = {
        'news': news
    }
    return render(request, 'admin_news/G780_admin_news_delete_conf.html', params)


@admin_login_required
def G790_admin_news_delete_comp(request, id):
    news = News.objects.get(id=id)
    params = {
        'news': news,
        'redirect_url': 'G720_admin_news_list'
    }
    if request.method == 'GET':
        return redirect('/G720_admin_news_list')
    if request.method == 'POST':
        news.del_flg = 1
        news.save()

    return render(request, 'admin_news/G790_admin_news_delete_comp.html', params)


