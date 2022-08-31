from django.shortcuts import render
from app.forms.admin_top import AdminLoginForm
from app.models import AdminUsers

from .common import *
    
def G400_admin_login(request):
    params = {
        'form': AdminLoginForm()
    }
    if request.method == 'POST':
        mail_address = request.POST['mail_address']
        password = common_hashing(request.POST['password'], mode='sha256')
        
        if AdminUsers.objects.filter(mail_address=mail_address, password=password, del_flg=0).count() == 1:
            # request.session.clear()
            request.session['admin_login_id'] = AdminUsers.objects.get(mail_address=mail_address, password=password, del_flg=0).id
            return redirect('/G440_admin_member_list')
        params = {
            'form': AdminLoginForm(request.POST),
            'error': 'ログインID または パスワードが違います'
            ,'admin': AdminUsers.objects.get(id=1)
        }

    return render(request, 'admin_top/G400_admin_login.html', params)