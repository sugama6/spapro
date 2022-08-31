from django.shortcuts import render, redirect
from app.models import Users, News

import re

from .common import *


@user_login_required
def G150_news(request):
    login_id = request.session['login_id']
    user = Users.objects.get(id=login_id)
    # news = News.objects.filter(del_flg=0)
    news = News.objects.all()
    params = {
        'news': news,
        'user': user
    }
    return render(request, 'news/G150_news.html', params)
    

@user_login_required
def G160_news_detail(request, id):
    login_id = request.session['login_id']
    user = Users.objects.get(id=login_id)
    # news = News.objects.filter(del_flg=0)
    news = News.objects.get(id=id)
    params = {
        'user': user,
        'news': news
    }
    return render(request, 'news/G160_news_detail.html', params)