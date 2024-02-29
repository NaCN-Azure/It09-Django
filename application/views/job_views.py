from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from application.services import job_service
from application.forms.job_form import JobForm
from django.contrib.auth.decorators import login_required
import json
'''
Create job view for Employer
'''
def index(request):
    return render(request,'index.html')
def job_detail(request):
    return render(request,'job-detail.html')
def job_info(request):
    return render(request,'jobSeekerInfo.html')
def job_em(request):
    return render(request,'employerInfo.html')


@require_http_methods(["POST"])
@login_required
def create_job_view(request):
    form = JobForm(request.POST or None)
    employer_id = request.POST.get('employer')
    job = job_service.create_job(request, form, employer_id)
    return JsonResponse({'message': 'Job created successfully'})

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
@login_required
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
@login_required
def list_all_jobs_view(request):
    jobs = job_service.get_all_jobs()
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})
   
def serialize_jobs(jobs):
    # return list(jobs.values('id', 'title', 'type','requirement', 'remote','industry','description',
    #                         'postcode','start_date','end_date','city','salary','other'))
    jobs_data = []
    for job in jobs:
        job_dict = {
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



