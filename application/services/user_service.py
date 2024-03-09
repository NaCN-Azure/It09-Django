from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import JsonResponse

from application.models import User
from django.contrib.auth.models import update_last_login


# def register_user(request, form, type):
#     if form.is_valid():
#         form['type'] = type
#         form.save()
#         messages.success(request, "Registration successful.")
#         return True
#     else:
#         messages.error(request, "Registration failed.")
#         return False


def login_user(request, form):
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Login successful.")
        return True
    else:
        messages.error(request, "Login failed.")
        return False


def get_user_info(user_id):
    try:
        user = User.objects.get(pk=user_id)
        return {
            'userInfo':
                {
                    'email': user.email,
                    'user_name': user.user_name,
                    'phone': user.phone,
                    'date': user.date,
                    'city': user.city,
                    'type': user.USER_TYPE_CHOICES[user.type],
                    'last_login': user.last_login,
                }}
    except User.DoesNotExist:
        return None


def update_user_info(user_id, data):
    try:
        user = User.objects.get(pk=user_id)
        user.user_name = data.get('user_name', user.user_name)
        user.email= data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        user.city = data.get('city', user.city)
        user.save()
        # 更新最后登录时间
        update_last_login(None, user)
        return True
    except User.DoesNotExist:
        return False


def change_password(user_id, new_password):
    user = User.objects.get(pk=user_id)
    user.set_password(new_password)
    user.save()
    update_last_login(None, user)
    return True


def logout_user(request):
    logout(request)
