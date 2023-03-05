from django.db import models
from Hospital.models import *
from Consultancy.models import *
from Employee.models import *



# Create your models here.

class CheckUp_Details(models.Model):
    check_description=models.TextField(null=True)
    token=models.ForeignKey(Doc_Token,on_delete=models.CASCADE,related_name='doc_token')
    member_id=models.ForeignKey(MEM_REGISTRATION,on_delete=models.CASCADE)
    checkd_bookingdate=models.DateField(auto_now=True)
    checkd_reply=models.TextField(null=True)
    checkd_status=models.IntegerField(default=0)
    
class MedicineReport(models.Model):
    checkdetails=models.ForeignKey(CheckUp_Details,on_delete=models.CASCADE)
    medicine_title=models.CharField(max_length=50)
    medicine_remark=models.TextField(null=True)
    medicine=models.CharField(max_length=100)
    is_major=models.CharField(max_length=50)
    major_details=models.TextField(null=True)
    medicine_report=models.FileField(upload_to='MedicineReport/')
    med_sts=models.IntegerField(default=0)

