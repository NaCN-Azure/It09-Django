from django.utils import timezone
from application.models import Application
from django.db.models import Case, When, Value, IntegerField

def create_application(user_id, job_id):
    application = Application(
        user_id=user_id,
        job_id=job_id,
        apply_date=timezone.now(),
        status=1  # default is 'applying'
    )
    application.save()
    return application

def update_application_status(pk, new_status):
    application = Application.objects.get(pk=pk)
    application.status = new_status
    application.save()
    return True

def get_applications_by_user(user_id):
    return Application.objects.filter(user_id=user_id).order_by('status')

def get_applications_by_user_ordered(user_id, status=None):
    applications = Application.objects.filter(user_id=user_id)
    if status is not None:
        applications = applications.filter(status=status)
    ordering = get_order()
    return applications.annotate(custom_order=ordering).order_by('custom_order')

def get_applications_by_job_ordered(job_id):
    ordering = get_order()
    return Application.objects.filter(job_id=job_id).annotate(custom_order=ordering).order_by('custom_order')

def get_order():
    return Case(
        When(status=3, then=Value(1)),
        When(status=1, then=Value(2)),
        When(status=2, then=Value(3)),
        When(status=4, then=Value(4)),
        default=Value(5),
        output_field=IntegerField(),
    )

def check_applications(job_id,user_id):
    return Application.objects.filter(job_id=job_id, user_id=user_id, status=1).exists()

def delete_application(application_id):
    application=Application.objects.get(pk=application_id)
    application.delete()