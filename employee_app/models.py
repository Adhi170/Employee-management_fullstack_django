from django.db import models

# Create your models here.
class employee_models(models.Model):
    emp_no=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    emp_salary=models.IntegerField()
    emp_address=models.TextField()