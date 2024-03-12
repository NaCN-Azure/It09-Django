from django.contrib import messages
from django.utils import timezone
from django.db.models import Case, When, Value, IntegerField,F
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from application.models import Job,User
from django.core.exceptions import ObjectDoesNotExist
import json

#Employer side functions


def create_job(request, employer_id, job_data):
    try:
        job = Job.objects.create(
            title=job_data.get('title'),
            description=job_data.get('description'),
            type=job_data.get('type'),
            requirement=job_data.get('requirement'),
            remote=job_data.get('remote'),
            industry=job_data.get('industry'),
            postcode=job_data.get('postcode'),
            start_date=job_data.get('start_date'),
            end_date=job_data.get('end_date'),
            city=job_data.get('city') or User.objects.get(pk=employer_id).city,  # If city is not provided, attempt to retrieve it from the employer
            salary=job_data.get('salary'),
            other=job_data.get('other'),
            employer=User.objects.get(pk=employer_id),
        )
        job.save()
        messages.success(request, "Job created")
        return True
    except User.DoesNotExist:
        messages.error(request, "Employer not found")
        return False
    except Exception as e:
        print(e)
        messages.error(request, "Job creation failed due to an error")
        return False
       

def update_job_info(job_id, data):
    try:
        job = Job.objects.get(pk=job_id)
        job.title=data.get("title", job.title)
        job.description=data.get("description", job.description)
        job.type=data.get("type", job.type)
        job.requirement=data.get("requirement", job.requirement)
        job.remote=data.get("remote", job.remote)
        job.industry=data.get("industry", job.industry)
        job.postcode=data.get("postcode", job.postcode)
        job.start_date=data.get("start_date", job.start_date)
        job.end_date=data.get("end_date", job.end_date)
        job.city=data.get("city", job.city)
        job.salary=data.get("salary", job.salary)
        job.other=data.get("other", job.other)
        job.save()
        return True
    except Job.DoesNotExist:
        return False
    
def get_jobs_by_employer(employer_id):
    return Job.objects.filter(employer_id=employer_id)

#all user side function

def get_job_by_jobID(job_id):
    try:
        return Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        return None
    
def get_all_jobs():
    return Job.objects.all().annotate(employer_email=F('employer__email')).order_by('title')

def delete_job(job_id):
    job=Job.objects.get(pk=job_id)
    job.delete()


        
    
    
    
    
    
    