from django.shortcuts import render,redirect 
from Admin.models import *
from Employee.models import *

# Create your views here.

def emp_home(request):
    Emp=EMP_REGISTRATION.objects.get(id=request.session['eid'])
    return render(request,"Employee/Emp_Home.html",{'EMP':Emp})

def emp_profile(request):
    emp_prof=EMP_REGISTRATION.objects.get(id=request.session["eid"])
    return render(request,"Employee/Emp_Profile.html",{'EmpPF':emp_prof})

def emp_upProf(request,upid):
    if "eid" in request.session:
        selemp=EMP_REGISTRATION.objects.get(id=upid)
        if request.method=="POST":
            selemp.Emp_name=request.POST.get('txt_emp_name')
            selemp.Emp_contact=request.POST.get('txt_emp_contact')
            selemp.Emp_emailid=request.POST.get('txt_emp_emailid')
            selemp.Emp_address=request.POST.get('txt_emp_address')
            selemp.Emp_age=request.POST.get('txt_emp_age')
            selemp.save()
            return redirect('employee:Emp_Profile')
        else:
            return render(request,"Employee/Emp_EditProfile.html",{'UpEmp':selemp})
    else:
        return redirect('guest:login')
    
def emp_changepass(request,cuid):
    change=EMP_REGISTRATION.objects.get(id=cuid)
    pwd=change.Emp_password
    if request.method=="POST":
        old=request.POST.get('cpwd')
        if old!=pwd:
            error="Password Not Correct"
            return render(request,"Employee/Emp_ChangePwd.html",{'Error':error})
        else:
            new=request.POST.get('npwd')
            change=EMP_REGISTRATION.objects.get(id=cuid)
            change.Emp_password=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,"Employee/Emp_ChangePwd.html")


def mem_reg(request):
    dis=DISTRICT.objects.all()
   
    if request.method=="POST" and request.FILES:
        empid=EMP_REGISTRATION.objects.get(id=request.session['eid'])
        memb=MEM_REGISTRATION.objects.filter(Emp_reg_id=empid).count()
        counst=int(empid.Num_fam_members)
        plcid=request.POST.get('sel_place')
        plc=PLACE.objects.get(id=plcid)
        Display_memregob=MEM_REGISTRATION.objects.filter(Emp_reg=request.session["eid"])
        if counst>0:
            if memb<counst:
                MEM_REGISTRATION.objects.create(Mem_name=request.POST.get('txt_mem_name'),Mem_address=request.POST.get('txt_mem_address'),
                    Mem_contact=request.POST.get('txt_mem_contact'),Mem_emailid=request.POST.get('txt_mem_emailid'),Mem_gender=request.POST.get('gender'),
                    Mem_age=request.POST.get('txt_mem_age'),Mem_photo=request.FILES.get('txt_memfile'),Mem_password=request.POST.get('txt_mem_pswd'),
                    Mem_place=plc,Patient_op=request.POST.get('txt_mem_patient'),Emp_reg=empid)  
                return redirect("employee:MEM_REG")
            else:   
                return render(request,"Employee/MEMBER_REG.html",{'emp_reg':Display_memregob,'DIS':dis})
        else:   
                return render(request,"Employee/MEMBER_REG.html",{'emp_reg':Display_memregob,'DIS':dis})
    else: 
        Display_memregob=MEM_REGISTRATION.objects.filter(Emp_reg=request.session["eid"])  
        return render(request,"Employee/MEMBER_REG.html",{'emp_reg':Display_memregob,'DIS':dis})

def dltmem(request,dmid):
    MEM_REGISTRATION.objects.get(id=dmid).delete()
    return redirect('employee:MEM_REG')



def viewclaimreport(request):
    emp=EMP_REGISTRATION.objects.get(id=request.session['eid'])
    num=emp.PEN_NO

    res=Medisep_Insurance.objects.filter(Emp_PENo=num)
    return render(request,"Employee/ViewClaims.html",{'res':res})




def view_memreg_details(request,vmid):
    member=MEM_REGISTRATION.objects.get(id=vmid)
    if request.method=="POST":
        VIEW_MEMBERDETAILS.objects.create(Mem_relation=request.POST.get('txt_mem_relation'),Mem_id=member)
        Mem=VIEW_MEMBERDETAILS.objects.filter(Mem_id_id__Emp_reg_id=request.session["eid"])
        return render(request,"Employee/VIEW_memberdetails.html",{'MEM':Mem})
    else:
        Mem=VIEW_MEMBERDETAILS.objects.filter(Mem_id_id__Emp_reg_id=request.session["eid"])
        return render(request,"Employee/VIEW_memberdetails.html",{'MEM':Mem})


def dltmemd(request,dmmid):
    VIEW_MEMBERDETAILS.objects.get(id=dmmid).delete()
    return redirect('employee:MEM_REG')

def upMEM_DETAILSfn(request,uppid):                                    # updation function of district working
    mem_detailob=VIEW_MEMBERDETAILS.objects.get(id=uppid)                
    if request.method=="POST":
        mem_detailob.Mem_relation=request.POST.get('txt_mem_relation')
        mem_detailob.save()
        return redirect('employee:MEM_REG')
    else:
        return render(request,"Employee/EDITVIEW_memberdetails.html",{'MD':mem_detailob})



