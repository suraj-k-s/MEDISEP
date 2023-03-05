from django.shortcuts import render,redirect
from .models import *
from Guest.views import *
from Patients.models import *

def adminhome(request):
    admin=Admin.objects.get(id=request.session['aid'])
    return render(request,"Admin/Admin_Home.html",{'A':admin})

def Index(request):
    return render(request,"Admin/Index.html")

def dis(request):
    if request.method=="POST":
        DISTRICT.objects.create(district=request.POST.get('txt_district'))
        disob=DISTRICT.objects.all().order_by('district')                                       # this function perform the display of entered data in list form
        return render(request,"Admin/District.html",{'Dis':disob})                    
    else:
        disob=DISTRICT.objects.all().order_by('district')                                     # this function perform the display of entered data in list form
        return render(request,"Admin/District.html",{'Dis':disob})

def dltdis(request,delid):                           # deletion function of district working
    DISTRICT.objects.get(id=delid).delete()
    return redirect('webadmin:District')

def updis(request,upid):                                    # updation function of district working
    seldis=DISTRICT.objects.get(id=upid)                
    if request.method=="POST":
        seldis.district=request.POST.get('txt_district')
        seldis.save()
        return redirect('webadmin:District')
    else:
        return render(request,"Admin/EditDistrict.html",{'SD':seldis})



def pla(request):
    disob=DISTRICT.objects.all()
    if request.method=="POST":
        disid=request.POST.get('sel_district')
        dist=DISTRICT.objects.get(id=disid)
        PLACE.objects.create(place=request.POST.get('txt_place'),district=dist)
        catob=PLACE.objects.all().order_by('place')                                  # this function perform the display of entered data in list form
        return render(request,"Admin/PLACE.html",{'pla':catob,'Dis':disob})
    else:
        catob=PLACE.objects.all().order_by('place')                                # this function perform the display of entered data in list form
        return render(request,"Admin/PLACE.html",{'pla':catob,'Dis':disob})

def dltpla(request,delid):                            #delete function of place working
    PLACE.objects.get(id=delid).delete()
    return redirect('webadmin:Place')

def uppla(request,uppid):        
    disobj=DISTRICT.objects.all()                            # updation function of place working
    objplace=PLACE.objects.get(id=uppid)                
    if request.method=="POST":
        disid=request.POST.get('sel_district')
        objplace.district=DISTRICT.objects.get(id=disid)
        objplace.place=request.POST.get('txt_place')
        objplace.save()
        return redirect('webadmin:Place')
    else:
        return render(request,"Admin/EditPlace.html",{'CT':objplace,'Disob':disobj})


def COMPTYPE(request):
    if request.method=="POST":
        CMPTYPE.objects.create(cmptype=request.POST.get('txt_cmptype'))
        cmptypeob=CMPTYPE.objects.all()                                      # this function perform the display of entered data in list form
        return render(request,"Admin/Cmptype.html",{'cmptype':cmptypeob})                    
    else:
        cmptypeob=CMPTYPE.objects.all()                                     # this function perform the display of entered data in list form
        return render(request,"Admin/Cmptype.html",{'cmptype':cmptypeob})

def dltCOMPTYPE(request,delid):                           # deletion function of complaint type working
    CMPTYPE.objects.get(id=delid).delete()
    return redirect('webadmin:Cmptype')

def upCOMPTYPE(request,uppid):                                    # updation function of district working
    cmptypeob=CMPTYPE.objects.get(id=uppid)                
    if request.method=="POST":
        cmptypeob.cmptype=request.POST.get('txt_cmptype')
        cmptypeob.save()
        return redirect('webadmin:Cmptype')
    else:
        return render(request,"Admin/EditCmptype.html",{'CT':cmptypeob})




def HSPTLTYPEfn(request):
    if request.method=="POST":
        HSPTLTYPE.objects.create(hsptltype=request.POST.get('txt_hsptltype'))
        hsptltypeob=HSPTLTYPE.objects.all()                                      # this function perform the display of entered data in list form
        return render(request,"Admin/Hsptltype.html",{'hsptltype':hsptltypeob})                    
    else:
        hsptltypeob=HSPTLTYPE.objects.all()                                     # this function perform the display of entered data in list form
        return render(request,"Admin/Hsptltype.html",{'hsptltype':hsptltypeob})

def dltHSPTLTYPEfn(request,delid):                           # deletion function of complaint type working
    HSPTLTYPE.objects.get(id=delid).delete()
    return redirect('webadmin:Hsptltype')

def upHSPTLTYPEfn(request,uppid):                                    # updation function of district working
    hsptltypeob=HSPTLTYPE.objects.get(id=uppid)                
    if request.method=="POST":
        hsptltypeob.hsptltype=request.POST.get('txt_hsptltype')
        hsptltypeob.save()
        return redirect('webadmin:Hsptltype')
    else:
        return render(request,"Admin/EditHsptltype.html",{'HT':hsptltypeob})





def EMP_DEPTfn(request):
    if request.method=="POST":
        EMP_DEPARTMENT.objects.create(Emp_deptname=request.POST.get('txt_emp_dept'))
        Emp_deptob=EMP_DEPARTMENT.objects.all().order_by('Emp_deptname')                     
        return render(request,"Admin/EMP_DEPARTMENT.html",{'emp_dept':Emp_deptob})
    else:
        Emp_deptob=EMP_DEPARTMENT.objects.all().order_by('Emp_deptname')                                    # this function perform the display of entered data in list form
        return render(request,"Admin/EMP_DEPARTMENT.html",{'emp_dept':Emp_deptob})

def dltEMP_DEPTfn(request,delid):                           # deletion function of employee department working
    EMP_DEPARTMENT.objects.get(id=delid).delete()
    return redirect('webadmin:emp_department')

def upEMP_DEPTfn(request,uppid):                                    # updation function of district working
    Emp_deptob=EMP_DEPARTMENT.objects.get(id=uppid)                
    if request.method=="POST":
        Emp_deptob.Emp_deptname=request.POST.get('txt_emp_dept')
        Emp_deptob.save()
        return redirect('webadmin:emp_department')
    else:
        return render(request,"Admin/EDITEMP_DEPARTMENT.html",{'ET':Emp_deptob})




def EMP_SUBDEPTfn(request):
    emp_depobj=EMP_DEPARTMENT.objects.all()
    if request.method=="POST":
        EmpDepid=request.POST.get('sel_emp_dept')
        Depob=EMP_DEPARTMENT.objects.get(id=EmpDepid)
        EMP_SUBDEPT.objects.create(Emp_subdept_name=request.POST.get('txt_emp_subdept'),Emp_deptid=Depob)
        Emp_deptname=request.POST.get('txt_emp_dept')
        Emp_deptsubob=EMP_SUBDEPT.objects.all().order_by('Emp_subdept_name')                                     # this function perform the display of entered data in list form
        return render(request,"Admin/EMP_SUBDEPARTMENT.html",{'emp_subdept':Emp_deptsubob,'EDT':emp_depobj})                    
    else:
        Emp_deptsubob=EMP_SUBDEPT.objects.all().order_by('Emp_subdept_name')                                      # this function perform the display of entered data in list form
        return render(request,"Admin/EMP_SUBDEPARTMENT.html",{'emp_subdept':Emp_deptsubob,'EDT':emp_depobj})
        
def dltEMP_SUBDEPTfn(request,delid):                            #delete function of subdept working
    EMP_SUBDEPT.objects.get(id=delid).delete()
    return redirect('webadmin:emp_subdepartment')

def upEMP_SUBDEPTfn(request,uppid):        
    Emp_deptobj=EMP_DEPARTMENT.objects.all()                            # updation function of place working
    objsub_dept=EMP_SUBDEPT.objects.get(id=uppid)                
    if request.method=="POST":
        Emp_deptid_ob=request.POST.get('sel_emp_dept')
        objsub_dept.Emp_deptid=EMP_DEPARTMENT.objects.get(id=Emp_deptid_ob)
        objsub_dept.Emp_subdept_name=request.POST.get('txt_emp_subdept')
        objsub_dept.save()
        return redirect('webadmin:emp_subdepartment')
    else:
        return render(request,"Admin/EDITEMP_SUBDEPARTMENT.html",{'EDT':objsub_dept,'Deptob':Emp_deptobj})

def AjaxSubDep(request):
    deptob=request.GET.get('dept')
    subdepob=EMP_SUBDEPT.objects.filter(Emp_deptid=deptob)
    return render(request,"Admin/Ajax_SubDep.html",{'SUB':subdepob})




def EMP_GRADEPOSTfn(request):
    emp_depobj=EMP_DEPARTMENT.objects.all()
    if request.method=="POST":
        Emp_subdep_id=request.POST.get('sel_subdept')
        subdep_ob=EMP_SUBDEPT.objects.get(id=Emp_subdep_id)
        EMP_GRADEPOST.objects.create(Emp_gradepost=request.POST.get('txt_emp_gradepost'),Emp_subdept=subdep_ob)
        Display_gradepostob=EMP_GRADEPOST.objects.all().order_by('Emp_gradepost')                                       # this function perform the display of entered data in list form
        return render(request,"Admin/EMP_GRADEPOST.html",{'emp_gradepost':Display_gradepostob,'DP':emp_depobj})                    
    else:
        Display_gradepostob=EMP_GRADEPOST.objects.all().order_by('Emp_gradepost')                                        # this function perform the display of entered data in list form
        return render(request,"Admin/EMP_GRADEPOST.html",{'emp_gradepost':Display_gradepostob,'DP':emp_depobj})
        
def dltEMP_GRADEPOSTfn(request,delid):                            #delete function of subdept working
    EMP_GRADEPOST.objects.get(id=delid).delete()
    return redirect('webadmin:emp_gradepost')



def DR_DEPTfn(request):
    if request.method=="POST":
        DR_DEPARTMENT.objects.create(Dr_deptname=request.POST.get('txt_dr_deptname'))
        DR_deptob=DR_DEPARTMENT.objects.all().order_by('Dr_deptname')                                         # this function perform the display of entered data in list form
        return render(request,"Admin/DR_DEPARTMENT.html",{'dr_dept':DR_deptob})                    
    else:
        DR_deptob=DR_DEPARTMENT.objects.all().order_by('Dr_deptname')                                        # this function perform the display of entered data in list form
        return render(request,"Admin/DR_DEPARTMENT.html",{'dr_dept':DR_deptob})

def dltDR_DEPARTMENTfn(request,delid):                           # deletion function of complaint type working
    DR_DEPARTMENT.objects.get(id=delid).delete()
    return redirect('webadmin:dr_department')

def upDR_DEPARTMENTfn(request,uppid):                                    # updation function of district working
    DR_deptob=DR_DEPARTMENT.objects.get(id=uppid)                
    if request.method=="POST":
        DR_deptob.Dr_deptname=request.POST.get('txt_dr_deptname')
        DR_deptob.save()
        return redirect('webadmin:dr_department')
    else:
        return render(request,"Admin/EDITDR_DEPARTMENT.html",{'DT':DR_deptob})





def EMP_REGfn(request):
    emp_depobj=EMP_DEPARTMENT.objects.all().order_by('Emp_deptname') 
    if request.method=="POST" and request.FILES:
        Emp_gradepostob=request.POST.get('sel_emp_grade')
        gradepost_ob=EMP_GRADEPOST.objects.get(id=Emp_gradepostob)
        EMP_REGISTRATION.objects.create(Emp_name=request.POST.get('txt_emp_name'),Emp_address=request.POST.get('txt_EMP_address'),
        Emp_contact=request.POST.get('txt_emp_contact'),Emp_emailid=request.POST.get('txt_emp_emailid'),Emp_gender=request.POST.get('gender'),
        Emp_age=request.POST.get('txt_emp_age'),Emp_photo=request.FILES.get('txt_empfile'),Emp_gradepost=gradepost_ob,
        doj=request.POST.get('txt_emp_doj'),PEN_NO=request.POST.get('txt_emp_pen'),Num_fam_members=request.POST.get('txt_fam_mems'),
        Emp_password=request.POST.get('emp_password'))
        Display_empregob=EMP_REGISTRATION.objects.filter(emp_sts=0)                                      # this function perform the display of entered data in list form
        return render(request,"Admin/EMP_REGISTRATION.html",{'emp_reg':Display_empregob,'DP':emp_depobj})                    
    else:
        Display_empregob=EMP_REGISTRATION.objects.filter(emp_sts=0)                                    # this function perform the display of entered data in list form
        return render(request,"Admin/EMP_REGISTRATION.html",{'emp_reg':Display_empregob,'DP':emp_depobj})

def AjaxGrade(request):
    subdepob=request.GET.get('dept')
    gradeob=EMP_GRADEPOST.objects.filter(Emp_subdept=subdepob)
    return render(request,"Admin/Ajax_GradePost.html",{'GP':gradeob})

def dltEMP_REGfn(request,delid):                            #delete function of subdept working
    emp=EMP_REGISTRATION.objects.get(id=delid)
    emp.emp_sts=1
    emp.save()
    return redirect('webadmin:emp_registration')

def history_backup(request):
    hb=EMP_REGISTRATION.objects.filter(emp_sts=1)
    return render(request,"Admin/RejectedEmpList.html",{'RE':hb})

def accptemp(request,aid):                            #delete function of subdept working
    emp=EMP_REGISTRATION.objects.get(id=aid)
    emp.emp_sts=0
    emp.save()
    return redirect('webadmin:emp_registration')



def HOS_REGfn(request):
    distobj=DISTRICT.objects.all()
    hstypeob=HSPTLTYPE.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=request.POST.get('sel_hos_place')
        plc=PLACE.objects.get(id=plcid)
        htypeid=request.POST.get('sel_hos_type')
        hst=HSPTLTYPE.objects.get(id=htypeid)
        HOS_REGISTRATION.objects.create(Hos_name=request.POST.get('txt_hos_name'),Hos_address=request.POST.get('txt_hos_address'),
        Hos_contact=request.POST.get('txt_hos_contact'),Hos_emailid=request.POST.get('txt_hos_emailid'),Hos_Place=plc,
        Hospital_type=hst,Hos_logo=request.FILES.get('txt_hosfile'),Hos_proof=request.FILES.get('txt_hos_proof'),
        Hos_password=request.POST.get('txt_hos_pswd'),Hos_isactive=request.POST.get('hospital_isactive'),
        Hos_establishment=request.POST.get('txt_hos_estblish'))
        HSPTL=HOS_REGISTRATION.objects.all().order_by('Hos_name')
        return render(request,"Admin/HOSPITAL_REG.html",{'DIS':distobj,'HST':hstypeob,'HSR':HSPTL})
    else:
        HSPTL=HOS_REGISTRATION.objects.all().order_by('Hos_name')
        return render(request,"Admin/HOSPITAL_REG.html",{'DIS':distobj,'HST':hstypeob,'HSR':HSPTL})

def dltHOS_REGfn(request,delid):                            #delete function of subdept working
    HOS_REGISTRATION.objects.get(id=delid).delete()
    return redirect('webadmin:hos_registration')

def insure(request,eid):
    employe=EMP_REGISTRATION.objects.get(id=eid)
    ids=employe.id
    emp_no=employe.PEN_NO
    med=Medisep_Insurance.objects.filter(Employee=employe).count()
    if med > 0:
        return redirect('webadmin:emp_registration')
    else:
        if request.method=="POST":
            Medisep_Insurance.objects.create(Insurance_amount=request.POST.get('txt_amount'),Emp_PENo=emp_no,Employee_id=ids)
            return redirect('webadmin:Admin_Home')
        else:
            return render(request,"Admin/Insurence.html")
    
def viewClaims(request):
    C=Claim.objects.filter(status=0)
    #C=Claim.objects.all()
    return render(request,"Admin/ViewClaims.html",{'sel':C})

def acceptclaim(request,cid):
    c=Claim.objects.get(id=cid)
    camount=c.claim_amount
    emp=c.Emp_PEno
   
    ins=Medisep_Insurance.objects.get(Emp_PENo=emp)
    amount=ins.Insurance_amount
    if int(camount) < int(amount):
        ins.Insurance_PaymentAmount=camount
        ins.save()
        c.status=1
        c.save()
        return redirect('webadmin:Admin_Home')
    else:
        return redirect('webadmin:Admin_Home')
        
def  rejectclaim(request,rid):
    c=Claim.objects.get(id=rid)
    c.status=2
    c.save()
    return redirect('webadmin:Admin_Home')


def viewcomplaints(request):
    user=Complaint.objects.filter(Member_id__gt=0)
    hospital=Complaint.objects.filter(hospital_id__gt=0)
    consultancy=Complaint.objects.filter(consultancy_id__gt=0)
    return render(request,"Admin/viewcomplaints.html",{'U':user,'H':hospital,'C':consultancy})

def viewfeedbacks(request):
    user=Feedback.objects.filter(Member_id__gt=0)
    hospital=Feedback.objects.filter(hospital_id__gt=0)
    consultancy=Feedback.objects.filter(consultancy_id__gt=0)
    doctor=Feedback.objects.filter(doctor_id__gt=0)
    return render(request,"Admin/viewfeedbacks.html",{'U':user,'H':hospital,'C':consultancy,'D':doctor})

    

