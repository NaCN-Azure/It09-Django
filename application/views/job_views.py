import os

from django.http import JsonResponse
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods

from django.conf import settings
from application.models import Job
from application.services import job_service,feedback_service
from application.forms.job_form import JobForm
from django.contrib.auth.decorators import login_required
import json
'''
Create job view for Employer
'''
def index(request):
    jobs = job_service.get_all_jobs()
    return render(request, 'index.html', {'jobs': time_serialize_jobs(jobs)})

@login_required
def job_detail(request, job_id):
    job = job_service.get_job_by_jobID(job_id)
    select = {
        'job_type_choices': Job.JOB_TYPE_CHOICES,
        'job_remote_choices':Job.JOB_REMOTE_CHOICES,
        'job_request_choices':Job.JOB_REQUEST_CHOICES,
        'job_industry_choices':Job.JOB_INDUSTRY_CHOICES
    }
    feedbacks = feedback_service.get_feedbacks_by_job(job)
    average_rate = feedback_service.job_average_rate(request,job_id)
    return render(request,'job-detail.html', {'job': job, 'feedbacks': feedbacks,'select': select,'average_rate':average_rate})

@login_required
def user_info(request):
    return render(request,'jobSeekerInfo.html')

@login_required
def employer_info(request):
    select = {
        'job_type_choices': Job.JOB_TYPE_CHOICES,
        'job_remote_choices': Job.JOB_REMOTE_CHOICES,
        'job_request_choices': Job.JOB_REQUEST_CHOICES,
        'job_industry_choices': Job.JOB_INDUSTRY_CHOICES
    }
    return render(request,'employerInfo.html',{'select':select})

'''
Create job for employer
'''
@require_http_methods(["POST"])
@login_required
def create_job_view(request):
    data = json.loads(request.body.decode('utf-8'))
    employer_id = data.get('employer_id')
    if not employer_id:
        return JsonResponse({'error': 'Employer ID is required'}, status=400)
    job = job_service.create_job(request, employer_id, data)
    if job:
        return JsonResponse({'message': 'Job created successfully'})
    else:
        return JsonResponse({'error': 'Job creation failed'}, status=400)

'''
Update job view for Employer
'''
@require_http_methods(["POST"])
@login_required
def update_job_view(request, job_id):
    data = json.loads(request.body.decode('utf-8'))
    success = job_service.update_job_info(job_id, data)
    if success:
        return JsonResponse({'message': 'Job updated successfully'})
    else:
        return JsonResponse({'error': 'Job not found'}, status=404)
    

'''
List all the job created by Employer and order by title 
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_employer(request, employer_id):
    jobs = job_service.get_jobs_by_employer(employer_id)
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
Return the job info selected by user
'''
@require_http_methods(["GET"])
#@login_required
def get_job_by_jobId_view(request, job_id):
    job = job_service.get_job_by_jobID(job_id)
    job_info = {
            'title': job.title,
            'description': job.description,
            "type": job.get_type_display(),
            "requirement": job.get_requirement_display(),
            "remote":  job.get_remote_display(),
            "industry":  job.get_industry_display(),
            "postcode":  job.postcode,
            "start_date":  job.start_date,
            "end_date":  job.end_date,
            "city":  job.city,
            "salary": job.salary,
            "other": job.other,
            "avatar":str(job.avatar),
        }
    return JsonResponse({'job_info': job_info})

'''
List all the job for user 
'''
@require_http_methods(["GET"])
#@login_required
def list_all_jobs_view(request):
    jobs = job_service.get_all_jobs()
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})


'''
Delete a job by job id
'''
@require_http_methods(["DELETE"])
@login_required
def delete_job_view(request, job_id):
    job_service.delete_job(job_id)
    return JsonResponse({'message': 'Job deleted'})


'''
Upload images for a job
'''
@require_http_methods(['POST'])
@login_required
def upload_job_image(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST' and request.FILES['job_image']:
        job_image = request.FILES['job_image']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        file_path = os.path.join(settings.MEDIA_ROOT, 'job', f'{job_id}.jpg')
        if os.path.exists(file_path):
            os.remove(file_path)
        filename = fs.save('job/' + f'{job_id}.jpg', job_image)
        job.avatar = fs.url(filename)
        job.save()
        return JsonResponse({'message': 'Job Image Updated'})
    return JsonResponse({'message': 'Update Failed'}, status=400)
 
    
'''
Serialize the job data
'''
def serialize_jobs(jobs):
    # return list(jobs.values('id', 'title', 'type','requirement', 'remote','industry','description',
    #                         'postcode','start_date','end_date','city','salary','other'))
    jobs_data = []
    for job in jobs:
        job_dict = {
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'type': job.get_type_display(), 
            'requirement': job.get_requirement_display(),
            'remote': job.get_remote_display(),
            'industry': job.get_industry_display(),
            'postcode': job.postcode,
            'start_date': job.start_date,
            'end_date': job.end_date,
            'city': job.city,
            'salary': job.salary,
            'other': job.other,
            'avatar':str(job.avatar),
        }
        jobs_data.append(job_dict)
    return jobs_data

def time_serialize_jobs(jobs):
    jobs_data = []
    for job in jobs:
        duration = (job.end_date - job.start_date).days
        job_dict = {
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'type': job.get_type_display(),  
            'requirement': job.get_requirement_display(),
            'remote': job.get_remote_display(),
            'industry': job.get_industry_display(),
            'postcode': job.postcode,
            'start_date': job.start_date.isoformat(),
            'end_date': job.end_date.isoformat(),
            'city': job.city,
            'salary': job.salary,
            'other': job.other,
            'avatar':str(job.avatar),
            'duration': duration,
            'employer_email':job.employer_email
        }
        jobs_data.append(job_dict)
    return jobs_data





