from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from application.services import apply_service
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
'''
Get user is and job id from the form, and create an instance
'''
@require_http_methods(["POST"])
@login_required
def create_application_view(request):
    data = json.loads(request.body.decode('utf-8'))
    user_id = data.get('user_id')
    job_id = data.get('job_id')
    application = apply_service.create_application(user_id, job_id)
    return JsonResponse({'message': 'Application created successfully', 'id': application.id})


'''
Update status
'''
@require_http_methods(["POST"])
@login_required
def update_application_status_view(request, application_id):
    data = json.loads(request.body.decode('utf-8'))
    new_status = data.get('status')
    success = apply_service.update_application_status(application_id, new_status)
    if success:
        return JsonResponse({'message': 'Application status updated successfully'})
    else:
        return JsonResponse({'error': 'Application not found'}, status=404)


'''
Return all applications created by the user according to user id
'''
@require_http_methods(["GET"])
@login_required
def get_applications_by_user_view(request, user_id):
    status = request.GET.get('status', None)
    applications = apply_service.get_applications_by_user_ordered(user_id,status)
    applications_data = serialize_applications(applications)
    return JsonResponse({'applications': applications_data})

'''
Return all applications under one job 
'''
@require_http_methods(["GET"])
@login_required
def get_applications_by_job_view(request, job_id):
    applications = apply_service.get_applications_by_job_ordered(job_id)
    applications_data = serialize_applications(applications)
    return JsonResponse({'applications': applications_data})


'''
Check a specific applications info
'''
@require_http_methods(["GET"])
@login_required
def check_applications(request,job_id,user_id):
    result = apply_service.check_applications(job_id,user_id)
    return JsonResponse({'exists':result})


'''
Delete a specific application
'''
@require_http_methods(["DELETE"])
@login_required
def delete_application_view(request, application_id):
    apply_service.delete_application(application_id)
    return JsonResponse({'message': 'Application deleted'})


def serialize_applications(applications):
    return list(applications.values('id', 'job__title', 'apply_date', 'status','job_id','user__user_name','user__email'))
