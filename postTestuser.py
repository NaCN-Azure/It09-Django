import os
import django
import random
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWork.settings')

django.setup()

from application.models import Job, User,Application,Feedback  # 替换myapp为你的应用名
import requests
import json

import requests
import json

# 初始化一个会话
session = requests.Session()

# 获取 CSRF token 的 URL
login_url = "http://127.0.0.1:8000/login/"
# 用户信息更新的 URL，假设1是用户ID
update_url = "http://127.0.0.1:8000/userInfo/1/update/"

change_url = 'http://127.0.0.1:8000/userInfo/1/change_password/'

# 首先，发送一个GET请求到登录页面获取CSRF token
get_response = session.get(login_url)
csrf_token = session.cookies.get('csrftoken')

# 登录请求的数据，根据你的用户模型调整字段名
login_data = {
    "username": "847896757@qq.com",
    "password": "12345678"
}

# 登录请求的头信息
login_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-CSRFToken': csrf_token
}

# 发送登录请求
login_response = session.post(login_url, headers=login_headers, data=login_data)

# 检查登录是否成功，根据实际情况调整判断条件
if login_response.status_code == 200:
    print("登录成功")

    # 更新用户信息的数据
    # update_data = json.dumps({
    #     "email": "azure@example.com",
    #     "user_name": "nsy",
    #     "phone": "07900541656",
    #     "city": "Glasgow"
    # })
    update_data = json.dumps({
        "new_password": "12345678"
    })

    # 更新请求的头信息，再次获取CSRF token以确保是最新的
    update_headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': session.cookies.get('csrftoken')
    }

    # 发送更新用户信息的POST请求
    update_response = session.post(change_url, headers=update_headers, data=update_data)

    # 检查更新操作的结果
    if update_response.status_code == 200 :
        print("用户信息更新成功")
        print(update_response.json())
    else:
        print("用户信息更新失败")
else:
    print("登录失败")

