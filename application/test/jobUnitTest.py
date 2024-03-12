# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:25:33 2024

@author: BonsaiPan
"""

import django
from django.test import TestCase
from application.models import Job

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWork.settings')
django.setup()

class JobModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Job.objects.create(
            title='Software Engineer',
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
            other='Relocation assistance available.'
        )

    def test_title_label(self):
        job = Job.objects.get(id=1)
        field_label = job._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        job = Job.objects.get(id=1)
        field_label = job._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_postcode_label(self):
        job = Job.objects.get(id=1)
        field_label = job._meta.get_field('postcode').verbose_name
        self.assertEquals(field_label, 'postcode')

    def test_city_label(self):
        job = Job.objects.get(id=1)
        field_label = job._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    def test_salary_label(self):
        job = Job.objects.get(id=1)
        field_label = job._meta.get_field('salary').verbose_name
        self.assertEquals(field_label, 'salary')
