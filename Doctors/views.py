from django.shortcuts import render,redirect
from Hospital.models import *
from Patients.models import *
from Doctors.models import *
from Employee.models import *
# Create your views here.

def dr_home(request):
    dr=DOCTOR_REGISTRATION.objects.get(id=request.session['did'])
    return render(request,"Doctors/Dr_Home.html",{'DR':dr})

def dr_profile(request):
    dr_prof=DOCTOR_REGISTRATION.objects.get(id=request.session["did"])
    return render(request,"Doctors/Dr_Profile.html",{'DrPF':dr_prof})

def dr_upProf(request,upid):
    if "did" in request.session:
        seldr=DOCTOR_REGISTRATION.objects.get(id=upid)
        if request.method=="POST":
            seldr.Doctor_name=request.POST.get('txt_dr_name')
            seldr.Doctor_contact=request.POST.get('txt_dr_cntct')
            seldr.Doctor_age=request.POST.get('txt_dr_age')
            seldr.Doctor_address=request.POST.get('txt_dr_address')
            seldr.save()
            return redirect('doctor:Dr_Profile')
        else:
            return render(request,"Doctors/Dr_EditProfile.html",{'UpDr':seldr})
    else:
        return redirect('guest:login')
    
def dr_changepass(request,cuid):
    change=DOCTOR_REGISTRATION.objects.get(id=cuid)
    pwd=change.Doctor_password
    if request.method=="POST":
        old=request.POST.get('cpwd')
        if old!=pwd:
            error="Password Not Correct"
            return render(request,"Doctors/Dr_ChangePwd.html",{'Error':error})
        else:
            new=request.POST.get('npwd')
            change=DOCTOR_REGISTRATION.objects.get(id=cuid)
            change.Doctor_password=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,"Doctors/Dr_ChangePwd.html")

def feedback(request):
    if 'did' in request.session:
        if request.method=="POST":
            dr=DOCTOR_REGISTRATION.objects.get(id=request.session['did'])
            Feedback.objects.create(description=request.POST.get('description'),doctor=dr)
            feed=Feedback.objects.filter(doctor=request.session['did'])
            return render(request,"Doctors/Feedback.html",{'F':feed})
        else:
            feed=Feedback.objects.filter(doctor=request.session['did'])
            return render(request,"Doctors/Feedback.html",{'F':feed})
    else:
        return redirect('guest:login')

def dltFEEDBACKfn(request,delid):                            #delete function of subdept working
    Feedback.objects.get(id=delid).delete()
    return redirect('doctor:Feedback')
    
def acceptedbookings(request):
    book=CheckUp_Details.objects.filter(token__Dr_availability_id__doctor_id=request.session['did'],checkd_status=1)
    return render(request,"Doctors/AcceptedUserBooking copy.html",{'book':book})

def medicinedetails(request,mid):
    check=CheckUp_Details.objects.get(id=mid)
    check.checkd_status='3'
    check.save()
    ids=check.id
    if request.method=="POST" and request.FILES:
        MedicineReport.objects.create(checkdetails_id=ids,medicine_report=request.FILES.get('file_report'),medicine_title=request.POST.get('txt_t'),medicine_remark=request.POST.get('txt_r'),major_details=request.POST.get('txt_md'),medicine=request.POST.get('txt_m'),is_major=request.POST.get('major'))
        return redirect('doctor:Viewbookings')
    return render(request,"Doctors/MedicineDetails.html")

def search_history(request):
    if request.method=="POST":
        Mem=MEM_REGISTRATION.objects.get(Mem_name=request.POST.get('u_name'),Mem_contact=request.POST.get('u_phoneno'))
        rep=MedicineReport.objects.filter(checkdetails_id__member_id_id=Mem)
        return render(request,"Doctors/SearchHistory.html",{'sel':rep})
    return render(request,"Doctors/SearchHistory.html")