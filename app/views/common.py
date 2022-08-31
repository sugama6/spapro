from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.utils import timezone
from django.core.exceptions import PermissionDenied

from datetime import timedelta
import hashlib
import random
import string
import sys
import os


def admin_login_required(func):
    """
        非ログイン状態でアクセスしたら404を排出
    """
    def checker(request, *args, **kwargs):
        # func(request)
        if request.session.get('admin_login_id') != None:
            return func(request, *args, **kwargs)
        else:
            return redirect('/G400_admin_login')
            # raise PermissionDenied
    return checker


def user_login_required(func):
    """
        非ログイン状態でアクセスしたら404を排出
    """
    def checker(request, *args, **kwargs):
        if request.session.get('login_id') != None:
            return func(request, *args, **kwargs)
        else:
            return redirect('/G020_login')
            # raise PermissionDenied
    return checker


# 日付取得
def common_get_datetime(mode='day', num=0):
    #日付で計算
    if mode == 'day':
        time = timezone.now() + timedelta(days=num)
    #月で計算
    elif mode == 'month':
        time = timezone.now() + relativedelta(months=num)
    #計算された日時をdatetime型で返却
    return time


# 文字列ハッシュ化
def common_hashing(word, mode):
    #SHA256の文字列にエンコード
    if mode == 'sha256':
        h = hashlib.sha256(word.encode('utf-8')).hexdigest()
    #MD5の文字列にエンコード
    elif mode == 'md5':
        extension = str(word).split('.')[-1]
        h = '%s.%s' % (hashlib.md5(word.encode()).hexdigest(), extension)
    return h

import random, string


# ランダムIDを取得
def common_random_id():
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
   random_str =  ''.join(randlst)[:8]
   print(random_str)
   return random_str


# メールの送信
def common_send_email(to_email_address, subject, contents):
    #送信元
    # from_email = 'spapro.juku@gmail.com'
    from_email = 'sparta.programming@gmail.com'
    #送信リスト
    recipient_list = [to_email_address]
    #BCC
    bcc = [to_email_address]
    #メールを作成
    password_reset_mail = EmailMessage(subject, contents, from_email, recipient_list, bcc)
    #メールを送信
    password_reset_mail.send()
    return True


# 日付取得
def common_get_datetime(mode='day', num=0):
    #日付で計算
    if mode == 'day':
        time = timezone.now() + timedelta(days=num)
    #月で計算
    elif mode == 'month':
        time = timezone.now() + relativedelta(months=num)
    #計算された日時をdatetime型で返却
    return time


def common_uploaded_file(file, new_dir_path):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file.name + "\n")
    file_name = file.name
    extension = str(file_name).split('.')[-1]
    hs_filename = '%s.%s' % (hashlib.md5(file_name.encode()).hexdigest(), extension)
    
    # #ステージング用
    # dirs = '/home/www/magreach/app/static/images'
    
    #開発用
    dirs = 'app/static/images'
    
    os.makedirs(dirs + new_dir_path, exist_ok=True)
    file_path = dirs + new_dir_path + hs_filename
    sys.stderr.write(file_path + "\n")
    
    with open(file_path, 'wb+') as destination:
      for chunk in file.chunks():
        #   sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
          print(destination.write(chunk))
        #   sys.stderr.write("*** handle_uploaded_file *** eee ***\n")
          return '/static/images' + new_dir_path + hs_filename


def common_set_submit_token(request):
    submit_token = str(uuid.uuid4())
    request.session['submit_token'] = submit_token
    return submit_token


def common_exists_submit_token(request):
    token_in_request = request.POST.get('submit_token')
    token_in_session = request.session.POP('submit_token', '')

    if not token_in_request:
        return False
    if not token_in_session:
        return False

    return token_in_request == token_in_session


# def common_login_check(request, target:str):
#     if request.session.get(target) == None:
#         return False
#         # if target == 'login_id':
#         #     return redirect('/G020_login')
#         # elif target == 'admin_login_id':
#         #     return redirect('/G400_admin_login')
#     else:
#         return True
