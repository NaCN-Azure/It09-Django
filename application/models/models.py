import os.path

from django.db import models
from .user_model import User
def job_directory_path(instance,filename):
    basefilename, file_extension = os.path.splitext(filename)
    return 'job/{jobid}/{basename}{ext}'.format(jobid=instance.pk,basename=basefilename,ext=file_extension)
class Job(models.Model):
    JOB_TYPE_CHOICES = (
        (1, 'Part-Time'),
        (2, 'Temporary'),
        (3,'Volunteer')
    )
    JOB_REQUEST_CHOICES = (
        (1,'Foundation Degree'),
        (2,'GCSE'),
        (3,'Certificate of Higher Education'),
        (4,'Bachelor\'s Degree')
    )
    JOB_REMOTE_CHOICES  = (
        (1,'In-Person'),
        (2,'Hybrid'),
        (3,'Remote')
    )
    JOB_INDUSTRY_CHOICES = (
        (1,'Retail'),
        (2,'Construction, Repair and Maintenance Services'),
        (3,'Personal Customer Services'),
        (4,'Restaurants & Food Services'),
        (5,'Hotel & Travel Accommodation'),
        (6,'Others'),
    )
    employer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.PositiveSmallIntegerField(choices=JOB_TYPE_CHOICES,null=True)
    requirement = models.PositiveSmallIntegerField(choices=JOB_REQUEST_CHOICES,null=True)
    remote = models.PositiveSmallIntegerField(choices=JOB_REMOTE_CHOICES,null=True)
    industry = models.PositiveSmallIntegerField(choices=JOB_INDUSTRY_CHOICES,null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    postcode = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    city = models.CharField(max_length=255)
    salary = models.FloatField(null=True,blank=True)
    other = models.CharField(max_length=512)
    avatar = models.ImageField(upload_to=job_directory_path, blank=True, null=True)

    class Meta:
        db_table = 'job'

class Application(models.Model):
    STATUS_TYPE_CHOICES = (
        (1,'submitted'),
        (2,'success'),
        (3,'reject'),
        (4,'error')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    apply_date = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPE_CHOICES)

    class Meta:
        db_table = 'application'

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'feedback'