from django.shortcuts import render
from application.services import apply_service
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
'''
表单获取user_id和job_id，以此创建一个申请的对象
'''
@require_http_methods(["POST"])
def create_application_view(request):
    data = json.loads(request.body.decode('utf-8'))
    user_id = data.get('user_id')
    job_id = data.get('job_id')
    application = apply_service.create_application(user_id, job_id)
    return JsonResponse({'message': 'Application created successfully', 'id': application.id})


'''
更新表单的status字段，一般是employer要调用的
'''
@require_http_methods(["POST"])
def update_application_status_view(request, application_id):
    data = json.loads(request.body.decode('utf-8'))
    new_status = data.get('status')
    success = apply_service.update_application_status(application_id, new_status)
    if success:
        return JsonResponse({'message': 'Application status updated successfully'})
    else:
        return JsonResponse({'error': 'Application not found'}, status=404)


'''
用户浏览自己的所有申请记录
'''
@require_http_methods(["GET"])
def get_applications_by_user_view(request, user_id):
    applications = apply_service.get_applications_by_user_ordered(user_id)
    applications_data = serialize_applications(applications)
    return JsonResponse({'applications': applications_data})


'''
雇主按照工位浏览的所有申请记录
'''
@require_http_methods(["GET"])
def get_applications_by_job_view(request, job_id):
    applications = apply_service.get_applications_by_job_ordered(job_id)
    applications_data = serialize_applications(applications)
    return JsonResponse({'applications': applications_data})

def serialize_applications(applications):
    return list(applications.values('id', 'job__title', 'apply_date', 'status')) ##Django的语言里，貌似可以通过双下划线访问外键的键，这超级棒这个！！！
