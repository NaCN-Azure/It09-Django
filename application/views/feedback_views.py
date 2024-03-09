from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from application.services import feedback_service  
from django.contrib.auth.decorators import login_required
import json
'''
add feedback for the user
'''
@require_http_methods(["POST"])
@login_required
def add_feedback_view(request):
    data = json.loads(request.body.decode('utf-8'))
    job_id = data.get('job_id')
    user_id = data.get('user_id')
    feedback_service.add_feedback(request, user_id, job_id)
    return JsonResponse({'message': 'Feedback added'})
    
'''
delete feedback for user
'''
@require_http_methods(["DELETE"])
@login_required
def delete_feedback_view(request, feedback_id):
    feedback_service.delete_feedback(feedback_id)
    return JsonResponse({'message': 'Feedback deleted'})
    

'''
return the average rate for the job
'''
@require_http_methods(["GET"])
#@login_required
def job_average_rate_view(request, job_id):
    average_rate = feedback_service.job_average_rate(request, job_id)
    if average_rate is not None:
        return JsonResponse({'average_rate': average_rate})
    else:
        return JsonResponse({'error': 'No feedback found for this job'}, status=404)
    

'''
return the feedbacks list for the user
'''
@require_http_methods(["GET"])
@login_required
def get_feedbacks_by_user_view(request, user_id):
    feedbacks = feedback_service.get_feedbacks_by_user(user_id)
    feedbacks_data = list(feedbacks.values('user','job__title','rate','comment','date','job_id','user__user_name'))
    return JsonResponse({'feedbacks': feedbacks_data})

@require_http_methods(["GET"])
@login_required
def get_feedbacks_by_job_view(request, job_id):
    feedbacks = feedback_service.get_feedbacks_by_job(job_id)
    feedbacks_data = list(feedbacks.values('user','job__title','rate','comment','date','user__user_name'))
    return JsonResponse({'feedbacks': feedbacks_data})
    
    