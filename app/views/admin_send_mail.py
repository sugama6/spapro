from django.shortcuts import render

from .common import *


@admin_login_required
def G470_admin_send_mail(request):
    return render(request, 'admin_send_mail/G470_admin_send_mail.html')


@admin_login_required
def G480_admin_send_mail_conf(request):
    return render(request, 'admin_send_mail/G480_admin_send_mail_conf.html')


@admin_login_required
def G490_admin_send_mail_comp(request):
    return render(request, 'admin_send_mail/G490_admin_send_mail_comp.html')
