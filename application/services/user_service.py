from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from application.models import User
from django.contrib.auth.models import update_last_login


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
                    'avatar':str(user.avatar),
                }}
    except User.DoesNotExist:
        return None


def update_user_info(user_id, data):
    print(data)
    try:
        user = User.objects.get(pk=user_id)
        user.user_name = data.get('username', user.user_name)
        user.email= data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        user.city = data.get('city', user.city)
        user.save()
        # Update the last login time
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

def email_exists(email):
    try:
        User.objects.get(email=email)
        return True
    except ObjectDoesNotExist:
        return False