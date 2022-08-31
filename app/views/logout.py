from django.shortcuts import render, redirect

from .common import *

def logout(request, login_id):
    request.session[login_id] = None
    if login_id == 'login_id':
        return redirect('/G020_login')
    else:
        return redirect('/G400_admin_login')