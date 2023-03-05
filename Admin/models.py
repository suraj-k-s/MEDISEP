from django.db import models

# Create your models here.

class Admin(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(unique=True,max_length=50)

class DISTRICT(models.Model):
    district=models.CharField(max_length=50)
    
    def __str__(self):
        return self.district 

class PLACE(models.Model):
    place=models.CharField(max_length=50)
    district=models.ForeignKey(DISTRICT,on_delete=models.CASCADE)     #foreign key preesentation of district 
    
    def __str__(self):
        return self.place


class CMPTYPE(models.Model):
    cmptype=models.CharField(max_length=50)

    def __str__(self):
        return self.cmptype

class HSPTLTYPE(models.Model):
    hsptltype=models.CharField(max_length=50)

    def __str__(self):
        return self.hsptltype

class DR_DEPARTMENT(models.Model):
    Dr_deptname=models.CharField(max_length=50)

    def __str__(self):
        return self.Dr_deptname

class EMP_DEPARTMENT(models.Model):
    Emp_deptname=models.CharField(max_length=50) 

    def __str__(self):
        return self.Emp_deptname

class EMP_SUBDEPT(models.Model):
    Emp_subdept_name=models.CharField(max_length=50) 
    Emp_deptid=models.ForeignKey(EMP_DEPARTMENT,on_delete=models.CASCADE)

    def __str__(self):
        return self.Emp_subdept_name

class EMP_GRADEPOST(models.Model):
    Emp_gradepost=models.CharField(max_length=50) 
    Emp_subdept=models.ForeignKey(EMP_SUBDEPT,on_delete=models.CASCADE)

    def __str__(self):
        return self.Emp_gradepost


class EMP_REGISTRATION(models.Model):
    Emp_name=models.CharField(max_length=50)
    Emp_address=models.CharField(max_length=50)
    Emp_contact=models.CharField(max_length=50)
    Emp_emailid=models.CharField(max_length=50)
    Emp_gender=models.CharField(max_length=50)
    Emp_age=models.CharField(max_length=50)
    Emp_photo=models.FileField(upload_to='EmployeeDocs/')
    Emp_gradepost=models.ForeignKey(EMP_GRADEPOST,on_delete=models.CASCADE)  
    doj=models.DateField(auto_now_add=True)
    PEN_NO=models.CharField(max_length=50)
    Medisep_insurance_id=models.CharField(max_length=50)
    Num_fam_members=models.CharField(max_length=50)
    Emp_password=models.CharField(unique=True,max_length=50)
    emp_sts=models.IntegerField(default=0)

    def __str__(self):
        return self.Emp_name



class HOS_REGISTRATION(models.Model):
    Hos_name=models.CharField(max_length=50)
    Hos_address=models.TextField(null=True)
    Hos_contact=models.CharField(max_length=50)
    Hos_emailid=models.EmailField(unique=True)
    Hos_Place=models.ForeignKey(PLACE,on_delete=models.CASCADE)  
    Hospital_type=models.ForeignKey(HSPTLTYPE,on_delete=models.CASCADE)
    Hos_logo=models.FileField(upload_to='HospitalDocs/')
    Hos_proof=models.FileField(upload_to='HospitalDocs/')
    Hos_password=models.CharField(unique=True,max_length=50)
    Hos_isactive=models.CharField(max_length=50)
    Hos_establishment=models.DateField()
    Hos_veri_status=models.CharField(max_length=50)   
    
    def __str__(self):
        return self.Hos_name
    
class Medisep_Insurance(models.Model):
    Insurance_amount=models.CharField(max_length=50)
    Employee=models.ForeignKey(EMP_REGISTRATION,on_delete=models.CASCADE)
    Emp_PENo=models.CharField(max_length=50) 
    Insurance_PaymentAmount=models.CharField(max_length=50,null=True)