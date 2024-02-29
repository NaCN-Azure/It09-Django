from django.contrib import messages
from django.utils import timezone
from django.db.models import Case, When, Value, IntegerField
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from application.models import Job
from django.core.exceptions import ObjectDoesNotExist

#Employer side functions

def create_job(request, form,employer_id):
    if form.is_valid():
        job = form.save(commit=False)
        job.employer_id = employer_id
        job.save()
        messages.success(request, "Job created")
        return True

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
    
def get_jobs_by_employer_orderBytitle(employer_id):
    return Job.objects.filter(employer_id=employer_id).order_by('title')

def get_jobs_by_employer_orderBytime(employer_id):
    return Job.objects.filter(employer_id=employer_id).order_by('start_date')

#all user side function

def get_job_by_jobID(job_id):
    try:
        return Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        return None
    
def get_all_jobs():
    return Job.objects.all().order_by('title')

def get_jobs_by_city(city):
    return Job.objects.filter(city=city).order_by('title')

def get_jobs_by_industry(industry):
    return Job.objects.filter(industry=industry).order_by('title')

def get_jobs_by_jobtype(type):
    return Job.objects.filter(type=type).order_by('title')

def get_jobs_by_remote(remote):
    return Job.objects.filter(remote=remote).order_by('title')

def get_jobs_by_salaryHightoLow():
    return Job.objects.all().order_by('-salary')

def get_jobs_by_salaryLowtoHigh():
    return Job.objects.all().order_by('salary')


        
    
    
    
    
    
    