from django.shortcuts import render, redirect
from app.models import * 
from app.forms.goal import GoalRegForm, GoalEditForm

from .common import *

@user_login_required
def G340_goal(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    if Goal.objects.filter(user_id=login_id).count() == 0:
        mode = 'new'
        goal = 0
    else:
        goal = Goal.objects.get(user_id=login_id)
        mode = 'already'
    params = {
        'user': user,
        'goal': goal,
        'mode': mode,
        'form': GoalRegForm()
    }

    if request.method == 'POST':
        if mode == 'new':
            form = GoalRegForm(request.POST)
            if form.is_valid():
                new_goal = Goal(
                    user_id=user,
                    one_year_later=request.POST['one_year_later'],
                    ten_years_later=request.POST['ten_years_later'],
                    learning_programming_why=request.POST['learning_programming_why'],
                    selected_spapro_why=request.POST['selected_spapro_why'],
                    how_much_effort=request.POST['how_much_effort'],
                    what_i_can_do=request.POST['what_i_can_do'],
                    how_can_i_be=request.POST['how_can_i_be'],
                    how_long_want_to_be=request.POST['how_long_want_to_be'],
                    keep_a_promise=request.POST['keep_a_promise'],
                    key_man=request.POST['key_man'],
                    orientation_expected_date=request.POST['orientation_expected_date'],
                    html_css_expected_date=request.POST['html_css_expected_date'],
                    javascript_expected_date=request.POST['javascript_expected_date'],
                    python1_expected_date=request.POST['python1_expected_date'],
                    python2_expected_date=request.POST['python2_expected_date'],
                    sql_expected_date=request.POST['sql_expected_date'],
                    django_expected_date=request.POST['django_expected_date'],
                    portfolio_expected_date=request.POST['portfolio_expected_date'],
                    job_change_expected_date=request.POST['job_change_expected_date'],
                    insert_time=common_get_datetime(mode='day'),
                    update_time=common_get_datetime(mode='day'),
                )
                new_goal.save()
                
            else:
                parmas['form'] = request.POST
                return render(request, 'goal/G340_goal.html', params)

    return render(request, 'goal/G340_goal.html', params)
    

@user_login_required
def G350_goal_edit(request):
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    goal = Goal.objects.select_related('user_id').get(user_id=login_id)
    params = {
        'user': user,
        'form': GoalEditForm(instance=goal)
    }

    if request.method == 'POST':
        form = GoalEditForm(request.POST, instance=goal)

        if form.is_valid():
            form = form.save(commit=False)
            form.update_time = common_get_datetime(mode='day')
            form.save()
            return redirect('/G340_goal')
        else:
            params['form'] = form
            return render(request, 'goal/G350_goal_edit.html', params)
            
    return render(request, 'goal/G350_goal_edit.html', params)
    