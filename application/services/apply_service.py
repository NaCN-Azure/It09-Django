from django.utils import timezone
from application.models import Application
from django.db.models import Case, When, Value, IntegerField

def create_application(user_id, job_id):
    application = Application(
        user_id=user_id,
        job_id=job_id,
        apply_date=timezone.now(),
        status=1  # 默认为 'applying'
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

def get_applications_by_user_ordered(user_id):
    ordering = get_order()
    return Application.objects.filter(user_id=user_id).annotate(custom_order=ordering).order_by('custom_order')

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