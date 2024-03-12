import json

from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages
from application.models import Job, User, Feedback
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

def add_feedback(request, user_id, job_id):
    data = json.loads(request.body.decode('utf-8'))
    feedback = Feedback(
        job_id = job_id,
        user_id = user_id,
        rate = data.get('rate'),
        comment = data.get('comment'),
        date = timezone.now()
        )
    feedback.save()
    return feedback

def delete_feedback(feedback_id):
    feedback=Feedback.objects.get(pk=feedback_id)
    feedback.delete()

def job_average_rate(request, job_id):
    average_rate = get_average_rate_by_job(job_id)
    return average_rate
    
def get_average_rate_by_job(job):
    average_rate = Feedback.objects.filter(job=job).aggregate(average_rate=Avg('rate'))
    if(average_rate['average_rate'] is None):
        return 0
    return average_rate['average_rate']

def get_feedbacks_by_user(user):
    return Feedback.objects.filter(user=user).order_by('date')

def get_feedbacks_by_job(job):
    return Feedback.objects.filter(job=job).order_by('date')

