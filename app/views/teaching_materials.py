from django.shortcuts import render, redirect
from app.models import Users, TeachingMaterials

from .common import *



@user_login_required
def G130_teaching_materials(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    teaching = TeachingMaterials.objects.filter(release_flg=1)
    params = {
        'user': user,
        'teaching_materials': teaching
    }
    return render(request, 'teaching_materials/G130_teaching_materials.html', params)
    
    

@user_login_required
def G140_teaching_detail(request, id):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    teaching = TeachingMaterials.objects.get(id=id)
    params = {
        'id': id,
        'user': user,
        'teaching': teaching
    }
    return render(request, 'teaching_materials/G140_teaching_detail.html', params)
    