from django.db import models
from Admin.models import *
from Hospital.models import *
from Employee.models import *
from Doctors.models import MedicineReport

# Create your models here.

class Feedback(models.Model):
    description=models.TextField(null=True)
    date=models.DateField(auto_now=True)
    hospital=models.ForeignKey(HOS_REGISTRATION,on_delete=models.SET_NULL,null=True)
    doctor=models.ForeignKey(DOCTOR_REGISTRATION,on_delete=models.SET_NULL,null=True)
    consultancy=models.ForeignKey(CONSULTANCY_REGISTRATION,on_delete=models.SET_NULL,null=True)
    Member=models.ForeignKey(MEM_REGISTRATION,on_delete=models.SET_NULL,null=True)
    
class Complaint(models.Model):
    complainttype=models.ForeignKey(CMPTYPE,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField(null=True)
    date=models.DateField(auto_now=True)
    reply=models.TextField(null=True)
    hospital=models.ForeignKey(HOS_REGISTRATION,on_delete=models.SET_NULL,null=True)
    consultancy=models.ForeignKey(CONSULTANCY_REGISTRATION,on_delete=models.SET_NULL,null=True)
    Member=models.ForeignKey(MEM_REGISTRATION,on_delete=models.SET_NULL,null=True)
    c_status=models.IntegerField(default=0)
    
class Claim(models.Model):
    medicine_id=models.ForeignKey(MedicineReport,on_delete=models.CASCADE)
    Emp_PEno=models.CharField(max_length=50)
    claim_amount=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    consultancy_id=models.ForeignKey(CONSULTANCY_REGISTRATION,on_delete=models.CASCADE)
    