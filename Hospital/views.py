from django.shortcuts import render,redirect
from Admin.models import *
from Hospital.models import*
from Patients.models import *
# Create your views here.

def hs_home(request):
    Hsptl=HOS_REGISTRATION.objects.get(id=request.session['hid'])
    return render(request,"Hospital/HS_Home.html",{'HSPTL':Hsptl})

def DR_REGfn(request):
    distobj=DISTRICT.objects.all().order_by('district')
    hospitalobj=HOS_REGISTRATION.objects.all()
    departmentobj=DR_DEPARTMENT.objects.all().order_by('Dr_deptname') 
    if request.method=="POST" and request.FILES:
        placeid=request.POST.get('sel_place')
        plcob=PLACE.objects.get(id=placeid)
        hosid=request.POST.get('sel_hospital_name')
        hospitalob=HOS_REGISTRATION.objects.get(id=hosid)
        dr_deptid=request.POST.get('sel_drdept_name')
        dr_deptob=DR_DEPARTMENT.objects.get(id=dr_deptid)
        DOCTOR_REGISTRATION.objects.create(Doctor_name=request.POST.get('txt_dr_name'),Doctor_address=request.POST.get('txt_dr_address'),
        Doctor_contact=request.POST.get('txt_dr_contact'),Doctor_emailid=request.POST.get('txt_dr_emailid'),
        Doctor_gender=request.POST.get('gender'),Doctor_age=request.POST.get('txt_dr_age'),
        Doctor_photo=request.FILES.get('txt_drfile'),Doctor_qualification=request.POST.get('txt_dr_qualification'),
        Doctor_place=plcob,Doctor_hospital=hospitalob,Doctor_department=dr_deptob,Doctor_password=request.POST.get('txt_dr_pswd'),
        Doctor_isactive=request.POST.get('doctor_isactive'),Doctor_doj=request.POST.get('txt_dr_doj'))
        DR_REG_DISPLAY=DOCTOR_REGISTRATION.objects.filter(Doctor_hospital=request.session["hid"])
        return render(request,"Hospital/DOCTOR_REGISTRATION.html",{'DIS':distobj,'HS':hospitalobj,'DR_dept':departmentobj,'DrReg':DR_REG_DISPLAY})
    else:
        DR_REG_DISPLAY=DOCTOR_REGISTRATION.objects.filter(Doctor_hospital=request.session["hid"])
        return render(request,"Hospital/DOCTOR_REGISTRATION.html",{'DIS':distobj,'HS':hospitalobj,'DR_dept':departmentobj,'DrReg':DR_REG_DISPLAY})


def dltDR_REGfn(request,delid):                            #delete function of subdept working
    DOCTOR_REGISTRATION.objects.get(id=delid).delete()
    return redirect('hospital:doctor_registration')



def CONSULTANCY_REGfn(request):
    if request.method=="POST" and request.FILES:
        hospitalobj=HOS_REGISTRATION.objects.get(id=request.session['hid'])
        CONSULTANCY_REGISTRATION.objects.create(Consultancy_name=request.POST.get('txt_consultancy_name'),
        Consultancy_hospital=hospitalobj,Consultancy_head=request.POST.get('txt_consultancy_head'),
        Consultancy_logo=request.FILES.get('txt_consultancyfile'),Consultancy_pswd=request.POST.get('txt_consultancy_pswd'))
        CONS_REG_DISPLAY=CONSULTANCY_REGISTRATION.objects.all()
        print(CONS_REG_DISPLAY)
        return render(request,"Hospital/CONSULTANCY_REG.html",{'ConsReg':CONS_REG_DISPLAY})
    else:
        CONS_REG_DISPLAY=CONSULTANCY_REGISTRATION.objects.all()
        return render(request,"Hospital/CONSULTANCY_REG.html",{'ConsReg':CONS_REG_DISPLAY})
    
def hs_profile(request):
    hs_prof=HOS_REGISTRATION.objects.get(id=request.session["hid"])
    return render(request,"Hospital/Hsptl_Profile.html",{'HSPF':hs_prof})

def hs_upProf(request,upid):
    if "hid" in request.session:
        seldr=HOS_REGISTRATION.objects.get(id=upid)
        if request.method=="POST":
            seldr.Hos_name=request.POST.get('txt_hs_name')
            seldr.Hos_contact=request.POST.get('txt_hs_cntct')
            seldr.Hos_emailid=request.POST.get('txt_hs_email')
            seldr.Hos_address=request.POST.get('txt_hs_address')
            seldr.save()
            return redirect('hospital:HS_Profile')
        else:
            return render(request,"Hospital/Hsptl_EditProfile.html",{'UpDr':seldr})
    else:
        return redirect('guest:login')
    
def hs_changepass(request,cuid):
    change=HOS_REGISTRATION.objects.get(id=cuid)
    pwd=change.Hos_password
    if request.method=="POST":
        old=request.POST.get('cpwd')
        if old!=pwd:
            error="Password Not Correct"
            return render(request,"Hospital/Hsptl_ChangePwd.html",{'Error':error})
        else:
            new=request.POST.get('npwd')
            change=HOS_REGISTRATION.objects.get(id=cuid)
            change.Hos_password=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,"Hospital/Hsptl_ChangePwd.html")

def feedback(request):
    if 'hid' in request.session:
        if request.method=="POST":
            hos=HOS_REGISTRATION.objects.get(id=request.session['hid'])
            Feedback.objects.create(description=request.POST.get('description'),hospital=hos)
            feed=Feedback.objects.filter(hospital=request.session['hid'])
            return render(request,"Hospital/Feedback.html",{'F':feed})
        else:
            feed=Feedback.objects.filter(hospital=request.session['hid'])
            return render(request,"Hospital/Feedback.html",{'F':feed})
    else:
        return redirect('guest:login')

def dltFEEDBACKfn(request,delid):                            #delete function of subdept working
    Feedback.objects.get(id=delid).delete()
    return redirect('hospital:Feedback')




def complaint(request):
    if 'hid' in request.session:
        ctype=CMPTYPE.objects.all()
        if request.method=="POST":
            hos=HOS_REGISTRATION.objects.get(id=request.session['hid'])
            ctypeid=request.POST.get('ctype')
            ct=CMPTYPE.objects.get(id=ctypeid)
            Complaint.objects.create(complainttype=ct,title=request.POST.get('title'),content=request.POST.get('content'),hospital=hos)
            cmp=Complaint.objects.filter(hospital=request.session['hid'])
            return render(request,"Hospital/Complaint.html",{'C':cmp,'CT':ctype})
        else:
            cmp=Complaint.objects.filter(hospital=request.session['hid'])
            return render(request,"Hospital/Complaint.html",{'C':cmp,'CT':ctype})
    else:
        return redirect('guest:login')  

def dltCOMPLAINTfn(request,delid):                            #delete function of subdept working
    Complaint.objects.get(id=delid).delete()
    return redirect('hospital:Complaint')