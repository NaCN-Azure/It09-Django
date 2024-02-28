from django.shortcuts import render
from application.services import apply_service
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def create_application_view(request):
    # 获取 user_id 和 job_id，这里用表单获取
    user_id = request.POST.get('user_id')
    job_id = request.POST.get('job_id')
    application = apply_service.create_application(user_id, job_id)
    return JsonResponse({'message': 'Application created successfully', 'id': application.id})

@require_http_methods(["POST"])
def update_application_status_view(request, application_id):
    new_status = request.POST.get('status')
    success = apply_service.update_application_status(application_id, new_status)
    if success:
        return JsonResponse({'message': 'Application status updated successfully'})
    else:
        return JsonResponse({'error': 'Application not found'}, status=404)

@require_http_methods(["GET"])
def get_applications_by_user_view(request, user_id):
    applications = apply_service.get_applications_by_user_ordered(user_id)
    applications_data = serialize_applications(applications)
    return JsonResponse({'applications': applications_data})

@require_http_methods(["GET"])
def get_applications_by_job_view(request, job_id):
    applications = apply_service.get_applications_by_job_ordered(job_id)
    applications_data = serialize_applications(applications)
    return JsonResponse({'applications': applications_data})

def serialize_applications(applications):
    return list(applications.values('id', 'job__title', 'apply_date', 'status')) ##Django的语言里，貌似可以通过双下划线访问外键的键，这超级棒这个！！！
