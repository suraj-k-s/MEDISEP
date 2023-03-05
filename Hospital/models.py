from django.db import models
from Admin.models import *

# Create your models here.

class DOCTOR_REGISTRATION(models.Model):
    Doctor_name=models.CharField(max_length=50)
    Doctor_address=models.TextField(null=True)
    Doctor_contact=models.CharField(max_length=50)
    Doctor_emailid=models.EmailField(unique=True)
    Doctor_gender=models.CharField(max_length=50)
    Doctor_age=models.CharField(max_length=50)
    Doctor_photo=models.FileField(upload_to='MemberDocs/')
    Doctor_qualification=models.CharField(max_length=50)
    Doctor_place=models.ForeignKey(PLACE,on_delete=models.CASCADE)
    Doctor_hospital=models.ForeignKey(HOS_REGISTRATION,on_delete=models.CASCADE)
    Doctor_department=models.ForeignKey(DR_DEPARTMENT,on_delete=models.CASCADE)
    Doctor_password=models.CharField(unique=True,max_length=50)
    Doctor_isactive=models.CharField(max_length=50,null=True)
    Doctor_doj=models.DateField(auto_now_add=True)
   
    
    def __str__(self):
        return self.Doctor_name


class CONSULTANCY_REGISTRATION(models.Model):
    Consultancy_name=models.CharField(max_length=50)
    Consultancy_hospital=models.ForeignKey(HOS_REGISTRATION,on_delete=models.CASCADE)
    Consultancy_head=models.CharField(max_length=50)
    Consultancy_logo=models.FileField(upload_to='ConsultancyDocs/')
    Consultancy_pswd=models.CharField(unique=True,max_length=50)

    def __str__(self):
        return self.Consultancy_name