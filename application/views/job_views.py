from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods

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
    return render(request, 'index.html', {'jobs': jobs})

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

@require_http_methods(["DELETE"])
@login_required
def delete_job_view(request, job_id):
    job_service.delete_job(job_id)
    return JsonResponse({'message': 'Job deleted'})
   
def serialize_jobs(jobs):
    # return list(jobs.values('id', 'title', 'type','requirement', 'remote','industry','description',
    #                         'postcode','start_date','end_date','city','salary','other'))
    jobs_data = []
    for job in jobs:
        job_dict = {
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'type': job.get_type_display(),  # 使用 get_FOO_display() 获取描述性字符串
            'requirement': job.get_requirement_display(),
            'remote': job.get_remote_display(),
            'industry': job.get_industry_display(),
            'postcode': job.postcode,
            'start_date': job.start_date,
            'end_date': job.end_date,
            'city': job.city,
            'salary': job.salary,
            'other': job.other,
        }
        jobs_data.append(job_dict)
    return jobs_data



