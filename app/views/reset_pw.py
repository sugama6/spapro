from django.shortcuts import render

def G030_reset_pw(request):
    return render(request, 'reset_pw/G030_reset_pw.html')
    
def G040_reset_pw_send_mail_comp(request):
    return render(request, 'reset_pw/G040_reset_pw_send_mail_comp.html')
    
def G050_resetting_pw(request):
    return render(request, 'reset_pw/G050_resetting_pw.html')
    
def G060_resetting_pw_comp(request):
    return render(request, 'reset_pw/G060_resetting_pw_comp.html')
    