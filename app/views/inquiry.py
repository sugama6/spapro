from django.shortcuts import render, redirect
from app.forms.inquiry import InquiryForm
from app.models import *
from .common import *


@user_login_required
def G170_inquiry(request):
    login_id = request.session['login_id']
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'form': InquiryForm()
    }
    if request.method == 'POST':
        params = {
            'form': InquiryForm(request.POST)
        }
    return render(request, 'inquiry/G170_inquiry.html', params)
    

@user_login_required
def G171_inquiry_conf(request):
    login_id = request.session['login_id']
    user = Users.objects.get(id=login_id)

    if request.method == 'GET':
        return redirect('/G170_inquiry')

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            params = {
                'user': user,
                'request': request.POST
            }
        else:
            params = {
                'user': user,
                'form': InquiryForm(request.POST)
            }
            return render(request, 'inquiry/G170_inquiry.html', params)
    return render(request, 'inquiry/G171_inquiry_conf.html', params)
    

@user_login_required
def G180_inquiry_comp(request):
    login_id = request.session['login_id']
    user = Users.objects.get(id=login_id)
    if request.method == 'GET':
        return redirect('/G170_inquiry')

    if request.method == 'POST':
        inquiry = Inquiry(
            user_id = Users.objects.get(id=login_id),
            title=request.POST['title'],
            content=request.POST['content'],
            read_flg=0,
            insert_time=common_get_datetime(mode='day'),
            update_time=common_get_datetime(mode='day')
        )
        inquiry.save()
        params = {
            'user': user,
            'redirect_url': 'G170_inquiry'
        }
    return render(request, 'inquiry/G180_inquiry_comp.html', params)
    

@user_login_required
def G190_q_and_a(request):
    login_id = request.session['login_id']
    user = Users.objects.get(id=login_id)
    qa = QandA.objects.filter(del_flg=0)
    params = {
        'user': user,
        'q_and_a': qa
    }
    return render(request, 'inquiry/G190_q_and_a.html', params)
    