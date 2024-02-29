from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from application.services import job_service
from application.forms.job_form import JobForm
from django.contrib.auth.decorators import login_required

'''
Create job view for Employer
'''
@require_http_methods(["POST"])
@login_required
def create_job_view(request):
    form = JobForm(request.POST or None)
    employer_id = request.POST.get('employer')
    job = job_service.create_job(request, form, employer_id)
    return JsonResponse({'message': 'Job created successfully'})

def index_view(request):
    return render(request, 'index.html')


'''
Update job view for Employer
'''
@require_http_methods(["POST"])
@login_required
def update_job_view(request, job_id):
    data = request.POST  
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
def list_jobs_by_employer_orderBytitle_view(request, employer_id):
    jobs = job_service.get_jobs_by_employer_orderBytitle(employer_id)
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
List all the job created by Employer and order by start date
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_employer_orderBytime_view(request, employer_id):
    jobs = job_service.get_jobs_by_employer_orderBytime(employer_id)
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
Return the job info selected by user
'''
@require_http_methods(["GET"])
@login_required
def get_job_by_jobId_view(request, job_id):
    job = job_service.get_job_by_jobID(job_id)
    return JsonResponse({'job': job})


'''
List all the job for user 
'''
@require_http_methods(["GET"])
@login_required
def list_all_jobs_view(request):
    jobs = job_service.get_all_jobs()
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
List all the job in selected city for user 
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_city_view(request, city):
    jobs = job_service.get_jobs_by_city(city)
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
List all the job in selected industry for user
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_industry_view(request, industry):
    jobs = job_service.get_jobs_by_industry(industry)
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
List all the job in selected job type for user 
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_jobtype_view(request, type):
    jobs = job_service.get_jobs_by_jobtype(type)
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
List all the job in selected work(remote) situation for user
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_remote_view(request, remote):
    jobs = job_service.get_jobs_by_remote(remote)
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
List all the job by salary in descent order for user
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_salaryHightoLow_view(request):
    jobs = job_service.get_jobs_by_salaryHightoLow()
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})

'''
List all the job by salary in increase order for user
'''
@require_http_methods(["GET"])
@login_required
def list_jobs_by_salaryLowtoHigh_view(request, city):
    jobs = job_service.get_jobs_by_salaryLowtoHigh()
    jobs_data = serialize_jobs(jobs)
    return JsonResponse({'jobs': jobs_data})
   
def serialize_jobs(jobs):
    return list(jobs.values('id', 'title', 'type','requirement', 'remote','industry','description',
                            'postcode','start_date','end_date','city','salary','other'))



