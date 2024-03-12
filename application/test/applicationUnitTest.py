# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:43:58 2024

@author: BonsaiPan
"""
import django
from django.test import TestCase
from application.models import Application, Job
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWork.settings')
django.setup()

User = get_user_model()

class ApplicationModelTest(TestCase):
    @classmethod     
    def setUpTestData(cls):
        # create user and job instance for testing
        cls.user = User.objects.create_user( email = '123@11.com', user_name='testuser', phone = '1234556' ,city = 'glasgow',password='12345',type = 1)
        cls.job = Job.objects.create(title='Test Job',
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

        # create application instance
        Application.objects.create(user=cls.user, job=cls.job, apply_date='2022-01-01 10:00:00', status=1)

    def test_login(self):
        # simulate login
        login = self.client.login(username='123@11.com', password='12345')
        self.assertTrue(login)
    
    def test_application_status(self):
        application = Application.objects.get(id=1)
        self.assertEqual(application.status, 1)
        

    def test_application_relations(self):
        application = Application.objects.get(id=1)
        self.assertEqual(application.user.user_name, 'testuser')
        self.assertEqual(application.job.title, 'Test Job')

