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
session = requests.Session()
login_url = "http://127.0.0.1:8000/login/"
get_response = session.get(login_url)
csrf_token = session.cookies.get('csrftoken')
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


update_application_status_url = "http://127.0.0.1:8000/application/update/5/"
# 检查登录是否成功，根据实际情况调整判断条件
if login_response.status_code == 200:
    print("登录成功")
    data = json.dumps({
        "status": 2
    })
    login_headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': session.cookies.get('csrftoken')
    }
# 发送 POST 请求创建申请
    create_response = session.post(update_application_status_url, headers=login_headers, data=data)

# 检查响应
    if create_response.status_code == 200:
        print("申请创建成功：", create_response.json())
    else:
        print("申请创建失败：")
else:
    print("登录失败")


