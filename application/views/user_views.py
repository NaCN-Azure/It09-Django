# views/user_views.py
import os

from django.contrib.auth import login
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib import messages

from application.forms.user_form import CustomUserCreationForm, CustomLoginForm
from application.models import User
from application.services import user_service
from django.middleware.csrf import get_token
import json


'''
用户注册，获取用户的表单填写，成功与否进行跳转
'''
def register(request, user_type):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.type = user_type
            user.save()
            messages.success(request, "Registration successful!")
            return redirect(reverse('login'))
        else:
            messages.error(request, "Registration failed, please try again.")
            return render(request, 'register.html', {'form': form, 'form_submitted': True, 'user_type': request.POST.get('user_type', '')})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html',  {'form': form})

'''
用户登陆，获取用户的邮箱/密码（登陆表单），然后进行验证
'''
def login_view(request):
    form = CustomLoginForm(data=request.POST or None)
    if request.method == 'POST':
        if user_service.login_user(request, form):
            return redirect(reverse('index'))
        else:
            messages.error(request, "Incorrect email and password, please try again.")
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

@require_http_methods(['POST'])
@login_required
def upload_user_image(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST' and request.FILES['user_image']:
        user_image = request.FILES['user_image']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        file_path = os.path.join(settings.MEDIA_ROOT, 'user', f'{user_id}.jpg')
        if os.path.exists(file_path):
            os.remove(file_path)
        filename = fs.save('user/' + f'{user_id}.jpg', user_image)
        user.avatar = fs.url(filename)
        user.save()
        return JsonResponse({'message': 'User Image Updated'})
    return JsonResponse({'message': 'Update Failed'}, status=400)

'''
登出用户
'''
def logout_user(request):
    user_service.logout_user(request)
    return HttpResponseRedirect(reverse('index'))