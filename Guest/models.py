from django.db import models
from Admin.models import *

# Create your models here.
class UserReg(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=50)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    photo=models.FileField(upload_to='userdocs/')
    place=models.ForeignKey(PLACE,on_delete=models.CASCADE)     #foreign key preesentation of place 
    password=models.CharField(unique=True,max_length=50)
    doj=models.DateField(auto_now_add=True)
