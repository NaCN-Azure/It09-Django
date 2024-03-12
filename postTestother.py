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
# send out login header
login_response = session.post(login_url, headers=login_headers, data=login_data)


update_application_status_url = "http://127.0.0.1:8000/application/update/5/"
# check if login is scuess, and print the output
if login_response.status_code == 200:
    print("login success")
    data = json.dumps({
        "status": 2
    })
    login_headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': session.cookies.get('csrftoken')
    }
# send POST request
    create_response = session.post(update_application_status_url, headers=login_headers, data=data)

    job_data = json.dumps({
            'title': 'Test Job',
            'description': 'Test Description',
            'type': 1,  
            'requirement': 1,  
            'remote': 1,  
            'industry': 1,  
            'postcode': '12345',
            'start_date':'2024-02-20',
            'end_date':'2024-09-20',
            'salary': 50000,
            'city':None,
            'other': 'Test Other Info',
            'employer_id': 1,  
        })
    

    job_create_url = "http://127.0.0.1:8000/job/createJob/"  
    job_response = session.post(job_create_url, headers=login_headers, data=job_data)

    # check create job response
    if job_response.status_code == 200:
        print("job create success：", job_response.json())
    else:
        print("job create failed：", job_response.text)

    if create_response.status_code == 200:
        print("application create success：", create_response.json())
    else:
        print("application create failed：")
else:
    print("login failed")


