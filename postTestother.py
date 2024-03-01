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

    job_data = json.dumps({
            'title': 'Test Job',
            'description': 'Test Description',
            'type': 1,  # 假设对应的是'Part-Time'
            'requirement': 1,  # 假设对应的是'Foundation Degree'
            'remote': 1,  # 假设对应的是'In-Person'
            'industry': 1,  # 假设对应的是'Retail'
            'postcode': '12345',
            'start_date':'2024-02-20',
            'end_date':'2024-09-20',
            'salary': 50000,
            'city':None,
            'other': 'Test Other Info',
            'employer_id': 1,  # 使用创建的测试用户ID
        })
    

# 发送创建工作职位的POST请求
    job_create_url = "http://127.0.0.1:8000/job/createJob/"  # 假设这是创建工作职位的URL
    job_response = session.post(job_create_url, headers=login_headers, data=job_data)

    # 检查创建工作职位的响应
    if job_response.status_code == 200:
        print("工作职位创建成功：", job_response.json())
    else:
        print("工作职位创建失败：", job_response.text)

# 检查响应
    if create_response.status_code == 200:
        print("申请创建成功：", create_response.json())
    else:
        print("申请创建失败：")
else:
    print("登录失败")


