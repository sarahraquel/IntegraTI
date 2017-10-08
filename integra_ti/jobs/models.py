from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=50)
    company_adress=models.CharField(max_length=100)
    role= models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    earnings=models.DecimalField(max_digits=6, decimal_places=2)
    link= models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
