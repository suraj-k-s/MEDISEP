from django.db import models
from Admin.models import *


# Create your models here.

class MEM_REGISTRATION(models.Model):
    Mem_name=models.CharField(max_length=50)
    Mem_address=models.TextField(null=True)
    Mem_contact=models.CharField(max_length=50)
    Mem_emailid=models.EmailField(unique=True)
    Mem_gender=models.CharField(max_length=50)
    Mem_age=models.CharField(max_length=50)
    Mem_photo=models.FileField(upload_to='MemberDocs/')
    Mem_password=models.CharField(unique=True,max_length=50)
    Mem_place=models.ForeignKey(PLACE,on_delete=models.CASCADE)
    Patient_op=models.CharField(max_length=50)
    Mem_doj=models.DateField(auto_now_add=True)
    Emp_reg=models.ForeignKey(EMP_REGISTRATION,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Mem_name


class VIEW_MEMBERDETAILS(models.Model):
    Mem_relation=models.CharField(max_length=50)
    Mem_id=models.ForeignKey(MEM_REGISTRATION,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.Mem_relation
