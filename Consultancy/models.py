from email.policy import default
from django.db import models
from Hospital.models import *


# Create your models here.

class DR_Availability(models.Model):
    doctor=models.ForeignKey(DOCTOR_REGISTRATION,on_delete=models.CASCADE)
    avail_fromTime=models.TimeField()
    avail_toTime=models.TimeField()
    avail_date=models.DateField()
    consultancy=models.ForeignKey(CONSULTANCY_REGISTRATION,on_delete=models.CASCADE)
    
class Doc_Token(models.Model):
    token_no=models.CharField(max_length=50)
    Dr_availability=models.ForeignKey(DR_Availability,on_delete=models.CASCADE)
    Token_Booking_status=models.IntegerField(default=0)
    
