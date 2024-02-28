from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages
from application.models import Job, User, Feedback
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

def add_feedback(request, user_id, job_id):
    data = request.POST
    feedback = Feedback(
        job = job_id,
        user = user_id,
        rate = data.get('rate'),
        comment = data.get('comment'),
        date = timezone.now()
        )
    feedback.save()
    messages.success(request, "Your feedback has been added.")
    return feedback

def delete_feedback(feedback_id):
    feedback=Feedback.objects.get(pk=feedback_id)
    feedback.delete()
    return JsonResponse({'message': 'Feedback deleted successfully'})

from django.http import JsonResponse

def job_average_rate(request, job_id):
    average_rate = get_average_rate_by_job(job_id)
    if average_rate is not None:
        return average_rate
    else:
        return JsonResponse({'error': 'No feedback found for this job.'}, status=404)
    
def get_average_rate_by_job(job):
    average_rate = Feedback.objects.filter(job=job).aggregate(average_rate=Avg('rate'))
    return average_rate['average_rate']

def get_feedbacks_by_user(use):
    return Feedback.objects.filter(user=user).orderby('date')

