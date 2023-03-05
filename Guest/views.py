from django.shortcuts import render,redirect
from Admin.models import *
from Hospital.models import *
from Employee.models import *

# Create your views here.

def home(request):
    return render(request,'Guest/home.html')

def ajaxplc(request):
    disob=request.GET.get('DIST')
    plcob=PLACE.objects.filter(district=disob).order_by('place')
    return render(request,"Guest/AjaxPlace.html",{'Place':plcob})

def login(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_pwd')
        Admin_log=Admin.objects.filter(email=Email,password=Password).count()
        Emp_log=EMP_REGISTRATION.objects.filter(Emp_emailid=Email,Emp_password=Password,emp_sts=0).count()
        Hsptl_log=HOS_REGISTRATION.objects.filter(Hos_emailid=Email,Hos_password=Password).count()
        Doctor_log=DOCTOR_REGISTRATION.objects.filter(Doctor_emailid=Email,Doctor_password=Password).count()
        Mem_log=MEM_REGISTRATION.objects.filter(Mem_emailid=Email,Mem_password=Password).count()
        consult=CONSULTANCY_REGISTRATION.objects.filter(Consultancy_name=Email,Consultancy_pswd=Password).count()
        if Admin_log > 0:
            admin=Admin.objects.get(email=Email,password=Password)
            request.session['aid']=admin.id
            return redirect('webadmin:Admin_Home')
        elif Emp_log > 0:
            emp=EMP_REGISTRATION.objects.get(Emp_emailid=Email,Emp_password=Password)
            request.session['eid']=emp.id
            return redirect('employee:Emp_Home')
        elif Hsptl_log > 0:
            hsptl=HOS_REGISTRATION.objects.get(Hos_emailid=Email,Hos_password=Password)
            request.session['hid']=hsptl.id
            return redirect('hospital:HS_Home')
        elif Doctor_log > 0:
            doctor=DOCTOR_REGISTRATION.objects.get(Doctor_emailid=Email,Doctor_password=Password)
            request.session['did']=doctor.id
            return redirect('doctor:DR_Home')
        
        elif Mem_log > 0:
            mem=MEM_REGISTRATION.objects.get(Mem_emailid=Email,Mem_password=Password)
            request.session['mid']=mem.id
            return redirect('patient:MEM_Home')
        elif consult >0:
            con=CONSULTANCY_REGISTRATION.objects.get(Consultancy_name=Email,Consultancy_pswd=Password)
            request.session['cid']=con.id
            request.session['hos']=con.Consultancy_hospital_id
            return redirect('consultancy:CN_Home')
        else:
            error="Invalid Details!!!"
            return render(request,"Guest/Login.html",{'ERROR':error})
    else:
        return render(request,"Guest/Login.html")