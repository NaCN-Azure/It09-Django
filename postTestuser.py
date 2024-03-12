import os
import django
import random
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWork.settings')

django.setup()

from application.models import Job, User,Application,Feedback 
import requests
import json

import requests
import json


session = requests.Session()


login_url = "http://127.0.0.1:8000/login/"

update_url = "http://127.0.0.1:8000/userInfo/1/update/"

change_url = 'http://127.0.0.1:8000/userInfo/1/change_password/'


get_response = session.get(login_url)
csrf_token = session.cookies.get('csrftoken')

login_data = {
    "username": "847896757@qq.com",
    "password": "12345678"
}

login_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-CSRFToken': csrf_token
}


login_response = session.post(login_url, headers=login_headers, data=login_data)


if login_response.status_code == 200:
    print("login success")

    # update user data
    # update_data = json.dumps({
    #     "email": "azure@example.com",
    #     "user_name": "nsy",
    #     "phone": "07900541656",
    #     "city": "Glasgow"
    # })
    update_data = json.dumps({
        "new_password": "12345678"
    })

    update_headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': session.cookies.get('csrftoken')
    }

    update_response = session.post(change_url, headers=update_headers, data=update_data)
    # 检查更新操作的结果
    if update_response.status_code == 200 :
        print("user info update success")
        print(update_response.json())
    else:
        print("user info update failed")
else:
    print("login failed")

