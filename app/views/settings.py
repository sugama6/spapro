from django.shortcuts import render
from app.models import Users

from .common import *


@user_login_required
def G200_settings(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    return render(request, 'settings/G200_settings.html', params)