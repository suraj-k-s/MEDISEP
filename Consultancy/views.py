from django.shortcuts import render,redirect
from Consultancy.models import *
from Doctors.models import CheckUp_Details, MedicineReport
from Hospital.models import *
from Patients.models import *

# Create your views here.

def cn_home(request):
    return render(request,"Consultancy/Consultancy_Home.html")

def con_profile(request):
    con_prof=CONSULTANCY_REGISTRATION.objects.get(id=request.session["cid"])
    return render(request,"Consultancy/CN_Profile.html",{'ConPF':con_prof})

def con_upProf(request,upid):
    if "cid" in request.session:
        selcon=CONSULTANCY_REGISTRATION.objects.get(id=upid)
        if request.method=="POST":
            selcon.Emp_name=request.POST.get('txt_con_name')
            selcon.Emp_contact=request.POST.get('txt_con_head')
            selcon.save()
            return redirect('consultancy:Con _Profile')
        else:
            return render(request,"Consultancy/CN_EditProfile.html",{'UpCon':selcon})
    else:
        return redirect('guest:login')
    
def con_changepass(request,cuid):
    change=CONSULTANCY_REGISTRATION.objects.get(id=cuid)
    pwd=change.Consultancy_pswd
    if request.method=="POST":
        old=request.POST.get('cpwd')
        if old!=pwd:
            error="Password Not Correct"
            return render(request,"Consultancy/CN_ChangePwd.html",{'Error':error})
        else:
            new=request.POST.get('npwd')
            change=CONSULTANCY_REGISTRATION.objects.get(id=cuid)
            change.Consultancy_pswd=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,"Consultancy/CN_ChangePwd.html")
    
def viewdoc(request):
    hos=HOS_REGISTRATION.objects.get(id=request.session['hos'])
    doc=DOCTOR_REGISTRATION.objects.filter(Doctor_hospital_id=hos)
    return render(request,"Consultancy/ViewDoctors.html",{'doc':doc})

def adddc(request,did):
    con=CONSULTANCY_REGISTRATION.objects.get(id=request.session['cid'])
    doc=DOCTOR_REGISTRATION.objects.get(id=did)
    av=DR_Availability.objects.filter(doctor_id=doc)
    if request.method=="POST":
        DR_Availability.objects.create(avail_fromTime=request.POST.get('txt_f'),avail_toTime=request.POST.get('txt_t'),avail_date=request.POST.get('txt_d'),consultancy=con,doctor=doc)
        return redirect('consultancy:viewdoc')
    else:
        return render(request,"Consultancy/AddAvailability.html",{'av':av})

def availfn(request,delid):                           # deletion function of complaint type working
    DR_Availability.objects.get(id=delid).delete()
    return redirect('consultancy:viewdoc')

    
def token(request,avid):
    dr=DR_Availability.objects.get(id=avid)
    if request.method=="POST":
        count=int(request.POST.get('txt_c'))
        for i in range(1,count+1):
            Doc_Token.objects.create(token_no=i,Dr_availability=dr)
        return redirect('consultancy:viewdoc')
    else:
        dislay_tokens=Doc_Token.objects.filter(Dr_availability=dr)
        return render(request,"Consultancy/GenarateToken.html",{'dr_tokens':dislay_tokens})


def dlt_token(request,did):                           # deletion function of complaint type working
    Doc_Token.objects.get(id=did).delete()
    return redirect('consultancy:viewdoc')
    
def viewbookings(request):
    book=CheckUp_Details.objects.filter(token__Dr_availability_id__consultancy_id=request.session['cid'],checkd_status=0)
    return render(request,"Consultancy/ViewUserBooking.html",{'book':book})

def feedback(request):
    if 'cid' in request.session:
        if request.method=="POST":
            con=CONSULTANCY_REGISTRATION.objects.get(id=request.session['cid'])
            Feedback.objects.create(description=request.POST.get('description'),consultancy=con)
            feed=Feedback.objects.filter(consultancy=request.session['cid'])
            return render(request,"Consultancy/Feedback.html",{'F':feed})
        else:
            feed=Feedback.objects.filter(consultancy=request.session['cid'])
            return render(request,"Consultancy/Feedback.html",{'F':feed})
    else:
        return redirect('guest:login')

def dltFEEDBACKfn(request,delid):                            #delete function of subdept working
    Feedback.objects.get(id=delid).delete()
    return redirect('consultancy:Feedback')

    
def complaint(request):
    if 'cid' in request.session:
        ctype=CMPTYPE.objects.all()
        if request.method=="POST":
            con=CONSULTANCY_REGISTRATION.objects.get(id=request.session['cid'])
            ctypeid=request.POST.get('ctype')
            ct=CMPTYPE.objects.get(id=ctypeid)
            Complaint.objects.create(complainttype=ct,title=request.POST.get('title'),content=request.POST.get('content'),consultancy=con)
            cmp=Complaint.objects.filter(consultancy=request.session['cid'])
            return render(request,"Consultancy/Complaint.html",{'C':cmp,'CT':ctype})
        else:
            cmp=Complaint.objects.filter(consultancy=request.session['cid'])
            return render(request,"Consultancy/Complaint.html",{'C':cmp,'CT':ctype})
    else:
        return redirect('guest:login')  

def dltCOMPLAINTfn(request,delid):                            #delete function of subdept working
    Complaint.objects.get(id=delid).delete()
    return redirect('consultancy:Complaint')
    
def accept(request,aid):
    check=CheckUp_Details.objects.get(id=aid)
    check.checkd_status=1
    check.save()
    return redirect('consultancy:viewbook')

def reject(request,rid):
    check=CheckUp_Details.objects.get(id=rid)
    check.checkd_status=2
    check.save()
    return redirect('consultancy:viewbook')

def acceptedbookings(request):
    book=CheckUp_Details.objects.filter(token__Dr_availability_id__consultancy_id=request.session['cid'],checkd_status=1) | CheckUp_Details.objects.filter(token__Dr_availability_id__consultancy_id=request.session['cid'],checkd_status=3)
    return render(request,"Consultancy/AcceptedUserBooking copy.html",{'book':book})

def rejectedbookings(request):
    book=CheckUp_Details.objects.filter(token__Dr_availability_id__consultancy_id=request.session['cid'],checkd_status=2)
    return render(request,"Consultancy/RejectedUserBooking copy.html",{'book':book})

def viewmedicine(request,aid):
    check=CheckUp_Details.objects.filter(id=aid).exclude(checkd_status=2)
    res=MedicineReport.objects.filter(checkdetails_id__in=check)
    claimcount=Claim.objects.filter(medicine_id__in=res).count()
    return render(request,"Consultancy/ViewMedicineDetails.html",{'res':res,'coun':claimcount})

def applyclaim(request,aid):
    med=MedicineReport.objects.get(id=aid)
   
    con=CONSULTANCY_REGISTRATION.objects.get(id=request.session['cid'])
    if request.method=="POST":

        claim=Claim.objects.create(medicine_id=med,claim_amount=request.POST.get('txt_amount'),Emp_PEno=request.POST.get('txt_no'),consultancy_id=con)
        return redirect('consultancy:viewerequest')
    else:
        return render(request,"Consultancy/ApplyClaim.html")
    
def viewClaims(request):
    res=Claim.objects.filter(consultancy_id=request.session['cid'])
    return render(request,"Consultancy/ViewClaims.html",{'res':res})