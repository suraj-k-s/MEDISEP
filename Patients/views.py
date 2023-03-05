from datetime import date,datetime
from django.shortcuts import render,redirect
from Employee.models import *
from Admin.models import *
from Doctors.models import *
from Hospital.models import *
from Consultancy.models import *
from .models import *
# Create your views here.

def mem_home(request):
    mem=MEM_REGISTRATION.objects.get(id=request.session['mid'])
    return render(request,"Patients/Mem_Home.html",{'MEM':mem})

def m_profile(request):
    m_prof=MEM_REGISTRATION.objects.get(id=request.session["mid"])
    return render(request,"Patients/Mem_Profile.html",{'MP':m_prof})

def m_upProf(request,upid):
    if "mid" in request.session:
        selm=MEM_REGISTRATION.objects.get(id=upid)
        if request.method=="POST":
            selm.Mem_name=request.POST.get('txt_M_name')
            selm.Mem_contact=request.POST.get('txt_M_cntct')
            selm.Mem_age=request.POST.get('txt_M_age')
            selm.Mem_address=request.POST.get('txt_M_address')
            selm.save()
            return redirect('patient:Mem_Profile')
        else:
            return render(request,"Patients/Mem_EditProfile.html",{'UpM':selm})
    else:
        return redirect('guest:login')
    
def M_changepass(request,cmid):
    change=MEM_REGISTRATION.objects.get(id=cmid)
    pwd=change.Mem_password
    if request.method=="POST":
        old=request.POST.get('cpwd')
        if old!=pwd:
            error="Password Not Correct"
            return render(request,"Patients/Mem_ChangePwd.html",{'Error':error})
        else:
            new=request.POST.get('npwd')
            change=MEM_REGISTRATION.objects.get(id=cmid)
            change.Mem_password=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,"Patients/Mem_ChangePwd.html")

def SearchHos(request):
    distobj=DISTRICT.objects.all()
    if request.method=="POST":
        place=request.POST.get('sel_hos_place')
        pl=PLACE.objects.get(id=place)
        Hospit=HOS_REGISTRATION.objects.filter(Hos_Place_id=pl)
        return render(request,"Patients/SearchHospital.html",{'DIS':distobj,'data':Hospit})
    else:
        return render(request,"Patients/SearchHospital.html",{'DIS':distobj})
def doclist(request,hid):
    hos=HOS_REGISTRATION.objects.get(id=hid)
    dep=DR_DEPARTMENT.objects.all()
    docs=DOCTOR_REGISTRATION.objects.filter(Doctor_hospital_id=hos)
    if request.method=="POST":
        dept=request.POST.get('seldept')
        department=DR_DEPARTMENT.objects.get(id=dept)
        res=DOCTOR_REGISTRATION.objects.filter(Doctor_department_id=department,Doctor_hospital_id=hos)
        return render(request,"Patients/ViewDoctors.html",{'docs':res,'dept':dep})
    return render(request,"Patients/ViewDoctors.html",{'docs':docs,'dept':dep})

def viewavail(request,did):
    
    doc=DOCTOR_REGISTRATION.objects.get(id=did)
    av=DR_Availability.objects.filter(doctor_id=doc)
    return render(request,"Patients/ViewAvailability.html",{'ava':av})
def viewtoken(request,avid):
    request.session["avid"]=avid
    ability=DR_Availability.objects.get(id=avid)
    tokens=Doc_Token.objects.filter(Dr_availability_id=ability,Token_Booking_status=0)
    return render(request,"Patients/ViewToken.html",{'tok':tokens})

def booktoken(request,tid):
    ticket=Doc_Token.objects.get(id=tid)

    patient=MEM_REGISTRATION.objects.get(id=request.session['mid'])
    print(request.session['mid'])
    mydate=datetime.now()
    check=CheckUp_Details.objects.filter(member_id=request.session['mid'],checkd_bookingdate=mydate,token_id__Dr_availability_id=request.session["avid"]).count()
    print(check) 
    if check >0:
        return render(request,"Patients/SearchHospital.html")
    else:
        CheckUp_Details.objects.create(token=ticket,member_id=patient)   
        ticket.Token_Booking_status=1
        ticket.save()
       
        return redirect('patient:MEM_Home')

def feedback(request):
    if 'mid' in request.session:
        if request.method=="POST":
            mem=MEM_REGISTRATION.objects.get(id=request.session['mid'])
            Feedback.objects.create(description=request.POST.get('description'),Member=mem)
            feed=Feedback.objects.filter(Member=request.session['mid'])
            return render(request,"Patients/Feedback.html",{'F':feed})
        else:
            feed=Feedback.objects.filter(Member=request.session['mid'])
            return render(request,"Patients/Feedback.html",{'F':feed})
    else:
        return redirect('guest:login')

def dltFEEDBACKfn(request,delid):                            #delete function of subdept working
    Feedback.objects.get(id=delid).delete()
    return redirect('patient:Feedback')
    
def complaint(request):
    if 'mid' in request.session:
        ctype=CMPTYPE.objects.all()
        if request.method=="POST":
            mem=MEM_REGISTRATION.objects.get(id=request.session['mid'])
            ctypeid=request.POST.get('ctype')
            ct=CMPTYPE.objects.get(id=ctypeid)
            Complaint.objects.create(complainttype=ct,title=request.POST.get('title'),content=request.POST.get('content'),Member=mem)
            cmp=Complaint.objects.filter(Member=request.session['mid'])
            return render(request,"Patients/Complaint.html",{'C':cmp,'CT':ctype})
        else:
            cmp=Complaint.objects.filter(Member=request.session['mid'])
            return render(request,"Patients/Complaint.html",{'C':cmp,'CT':ctype})
    else:
        return redirect('guest:login')

def dltCOMPLAINTfn(request,delid):                            #delete function of subdept working
    Complaint.objects.get(id=delid).delete()
    return redirect('patient:Complaint')


