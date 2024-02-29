# views/user_views.py
from django.contrib.auth import login
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from application.forms.user_form import CustomUserCreationForm, CustomLoginForm
from application.services import user_service
from django.middleware.csrf import get_token
import json


'''
用户注册，获取用户的表单填写，成功与否进行跳转
'''
def register(request,user_type):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if user_service.register_user(request, form,user_type):
            return redirect(reverse('login'))
    return render(request, 'register.html', {'form': form})

'''
用户登陆，获取用户的邮箱/密码（登陆表单），然后进行验证
'''
def login_view(request):
    form = CustomLoginForm(data=request.POST or None)
    if request.method == 'POST':
        if user_service.login_user(request, form):
            return redirect(reverse('index'))
    return render(request, 'login.html', {'form': form})

'''
根据用户id获取用户的所有信息
'''
@login_required
def get_user_info(request, user_id):
    user_info = user_service.get_user_info(user_id)
    if user_info:
        return JsonResponse(user_info)
    else:
        return JsonResponse({'error': 'User not found'}, status=404)

'''
根据用户id更新用户信息（除密码）
'''
@require_POST
@login_required
def update_user_info(request, user_id):
    data = json.loads(request.body.decode('utf-8'))  # 正确获取 JSON 数据
    print(data)
    if user_service.update_user_info(user_id, data):
        return JsonResponse({'success': 'User information updated successfully'})
    else:
        return JsonResponse({'error': 'User not found'}, status=404)

'''
根据请求修改密码，回头根据安全性，可能需要改为请求
'''
@login_required
def change_password(request,user_id):
    data = json.loads(request.body.decode('utf-8'))
    new_password = data.get('new_password')
    if user_service.change_password(user_id, new_password):
        return JsonResponse({'success': 'Password changed successfully'})
    else:
        return JsonResponse({'error': 'Wrong password'}, status=400)


'''
登出用户
'''
def logout_user(request):
    user_service.logout_user(request)
    return HttpResponseRedirect(reverse('login')) #这个重定向回头需要改一下，暂时这样