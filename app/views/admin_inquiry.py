from django.shortcuts import render, redirect
from app.models import Inquiry, AdminUsers
from app.forms.admin_inquiry import InquiryResponseForm

from .common import *


@admin_login_required
def G650_admin_inquiry_list(request):
    inquirys = Inquiry.objects.select_related('user_id').all().order_by('-insert_time')
    params = {
        'inquirys': inquirys
    }
    return render(request, 'admin_inquiry/G650_admin_inquiry_list.html', params)


@admin_login_required
def G660_admin_inquiry_detail(request, id):
    inquiry = Inquiry.objects.select_related('user_id').get(id=id)
    inquiry.read_flg = 1
    inquiry.save()
    params = {
        'inquiry': inquiry,
        'form': InquiryResponseForm()
    }

    if request.method == 'POST':
        params['form'] = InquiryResponseForm(request.POST)
    return render(request, 'admin_inquiry/G660_admin_inquiry_detail.html', params)


@admin_login_required
def G670_admin_inquiry_res(request, id):
    return render(request, 'admin_inquiry/G670_admin_inquiry_res.html')


@admin_login_required
def G680_admin_inquiry_res_conf(request, id):
    if request.method == 'GET':
        return redirect('/G650_admin_inquiry_list')
    if request.method == 'POST':
        inquiry = Inquiry.objects.select_related('user_id').get(id=id)
        params = {
            'inquiry': inquiry,
            'content': request.POST['content']
        }
    return render(request, 'admin_inquiry/G680_admin_inquiry_res_conf.html', params)


@admin_login_required
def G690_admin_inquiry_res_comp(request, id):
    if request.method == 'GET':
        return redirect('/G650_admin_inquiry_list')

    inquiry = Inquiry.objects.select_related('user_id').get(id=id)
    params = {
        'redirect_url': 'G650_admin_inquiry_list',
        'inquiry': inquiry,
    }
    if request.method == 'POST':
        admin_login_id = request.session.get('admin_login_id')
        admin_user = AdminUsers.objects.get(id=admin_login_id)

        if inquiry.answer_flg == False:
            post_content = request.POST['content']
            line = '============================'
            reply_content = f'▼お問い合わせ内容▼\n{inquiry.content}\n\n{line}\n\n{post_content}\n\n{line}\n\n担当 {admin_user.last_name}'

            common_send_email(
                to_email_address=inquiry.user_id.mail_address,
                subject='お問い合わせいただいた内容について',
                contents=reply_content
            )

            inquiry.answer_flg = True
            inquiry.save()

            params['result'] = 'success'

        else:
            params['result'] = 'already'
            return render(request, 'admin_inquiry/G690_admin_inquiry_res_comp.html', params)
    return render(request, 'admin_inquiry/G690_admin_inquiry_res_comp.html', params)
