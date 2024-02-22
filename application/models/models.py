from django.db import models
from .user_model import User

class Job(models.Model):
    JOB_TYPE_CHOICES = (
        (1, 'part-time'),
        (2, 'full-time'),
    )
    employer = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=JOB_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    city = models.CharField(max_length=255)
    salary = models.FloatField(null=True,blank=True)
    other = models.CharField(max_length=255)

    class Meta:
        db_table = 'job'

class Application(models.Model):
    STATUS_TYPE_CHOICES = (
        (1,'applying'),
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

