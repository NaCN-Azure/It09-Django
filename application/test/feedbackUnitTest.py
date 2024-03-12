# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:36:41 2024

@author: BonsaiPan
"""
import django
from django.test import TestCase
from application.models import Feedback, Job, User
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWork.settings')
django.setup()

class FeedbackModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create user and job instance for testing
        cls.user = User.objects.create_user( email = '123@11.com', user_name='testuser', phone = '1234556' ,city = 'glasgow',password='12345',type = 1)
        cls.job = Job.objects.create(title='Software Engineer',
        description='Develop and maintain software solutions.',
        postcode='12345',
        start_date='2022-01-01 10:00:00',
        end_date='2022-12-31 18:00:00',
        city='Techville',
        salary=120000.00,
        type=1,
        requirement=4,
        remote=3,
        industry=2,
        other='Relocation assistance available.')

        # create feedback instance
        Feedback.objects.create(user=cls.user, job=cls.job, rate=5, comment='Great job!', date='2022-01-01 10:00:00')

    def test_feedback_rate(self):
        feedback = Feedback.objects.get(id=1)
        self.assertEqual(feedback.rate, 5)

    def test_feedback_comment(self):
        feedback = Feedback.objects.get(id=1)
        self.assertEqual(feedback.comment, 'Great job!')

