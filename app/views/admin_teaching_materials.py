from django.shortcuts import render, redirect
from app.forms.admin_teaching_materials import TeachinRegForm
from app.models import Users, TeachingMaterials

from .common import *


@admin_login_required
def G590_admin_teaching_materials_list(request):
    teaching_materials = TeachingMaterials.objects.all()
    params = {
        'teaching_materials': teaching_materials
    }
    return render(request, 'admin_teaching_materials/G590_admin_teaching_materials_list.html', params)


@admin_login_required
def G600_admin_teaching_materials_reg(request):
    params = {
        'form': TeachinRegForm()
    }
    if request.method == 'POST':
        params = {
            'form': TeachinRegForm(request.POST),
            'request_image': request.POST['image']
        }
    return render(request, 'admin_teaching_materials/G600_admin_teaching_materials_reg.html', params)


@admin_login_required
def G610_admin_teaching_materials_reg_conf(request):
    if request.method == 'GET':
        return redirect('/G600_admin_teaching_materials_reg')

    if request.method == 'POST':
        form = TeachinRegForm(request.POST)

        if request.FILES.get('image'):
            image_path = '/'
            image = common_uploaded_file(request.FILES['image'], image_path)
        else:
            image = ''

        if form.is_valid():
            print(True)
            params = {
                'request': request.POST,
                'request_image': image
            }
            return render(request, 'admin_teaching_materials/G610_admin_teaching_materials_reg_conf.html', params)
        else:
            print(False)
            params = {
                'form': TeachinRegForm(request.POST),
                # 'image': product.image,
            }
            return render(request, 'admin_teaching_materials/G600_admin_teaching_materials_reg.html', params)
    return render(request, 'admin_teaching_materials/G610_admin_teaching_materials_reg_conf.html', params)


@admin_login_required
def G620_admin_teaching_materials_reg_comp(request):
    if request.method == 'GET':
        return redirect('/G600_admin_teaching_materials_reg')
    if request.method == 'POST':
        teaching = TeachingMaterials(
            title=request.POST['title'],
            content=request.POST['content'],
            url=request.POST['url'],
            image=request.POST['image'],
            programming_language=request.POST['programming_language'],
            release_flg=request.POST['release_flg'],
            insert_time=common_get_datetime(mode='day'),
            update_time=common_get_datetime(mode='day')
        )
        teaching.save()
        params = {
            'teaching_title': request.POST['title'],
            'redirect_url': 'G590_admin_teaching_materials_list'
        }
        return render(request, 'admin_teaching_materials/G620_admin_teaching_materials_reg_comp.html', params)
    return render(request, 'admin_teaching_materials/G620_admin_teaching_materials_reg_comp.html')


@admin_login_required
def G621_admin_teaching_materials_detail(request, id):
    teaching = TeachingMaterials.objects.get(id=id)
    params = {
        'teaching': teaching,
        'id': id
    }
    return render(request, 'admin_teaching_materials/G621_admin_teaching_materials_detail.html', params)


@admin_login_required
def G622_admin_teaching_materials_edit(request, id):
    teaching = TeachingMaterials.objects.get(id=id)
    params = {
        'id': id,
        'teaching': teaching,
        'form': TeachinRegForm(instance=teaching)
    }
    if request.method == 'POST':
        form = TeachinRegForm(request.POST, instance=teaching)
        import re
        if form.is_valid():
            if request.FILES.get('image'):
                if re.search('.*[.png|.jpeg|.jpg|.gif]$', request.FILES.get('image').name):
                    image = common_uploaded_file(file=request.FILES['image'], new_dir_path='/')
                else:
                    params = {
                        'id': id,
                        'form': form,
                        'image_error': '画像は png jpeg jpg gifのいずれかでアップロードしてください。' 
                    }
                    return render(request, 'admin_teaching_materials/G622_admin_teaching_materials_edit.html', params)
            else:
                image = teaching.image

            form = form.save(commit=False)
            form.image = image
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect(f'/G621_admin_teaching_materials_detail/{id}')
        else:
            params['form'] = TeachinRegForm(request.POST)
    return render(request, 'admin_teaching_materials/G622_admin_teaching_materials_edit.html', params)


@admin_login_required
def G630_admin_teaching_materials_del_conf(request):
    return render(request, 'admin_teaching_materials/G630_admin_teaching_materials_del_conf.html')


@admin_login_required
def G640_admin_teaching_materials_del_comp(request):
    return render(request, 'admin_teaching_materials/G640_admin_teaching_materials_del_comp.html')
