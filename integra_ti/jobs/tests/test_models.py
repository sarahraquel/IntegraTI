from django.test import TestCase
from jobs.models import Job
from rest_framework import status

class JobModelTest(TestCase):
    def setUp(self):
        self.job = Job(company="UFRN - IMD", 
        company_adress="Av. Bernardo Vieira", role="Web developer", 
        description="You will be working in all aspects of architecting and developing our Boardroom application.",
        earnings=1200.00, link="http://teste.com", phone="99991-5000")

    def test_model_can_create_a_job(self):
        old_count = Job.objects.count()
        self.job.save()
        new_count = Job.objects.count()
        self.assertNotEqual(old_count, new_count)
