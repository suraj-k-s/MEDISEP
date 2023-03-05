from django.urls import path
from Hospital import views
app_name='hospital'

urlpatterns = [
    path('hs_home/',views.hs_home,name="HS_Home"),
    path('doctor_reg/',views.DR_REGfn,name="doctor_registration"),
    path('dltdoctor_reg/<int:delid>',views.dltDR_REGfn,name="dlt-DOCTOR_REGISTRATION"), #deletion path

    path('consultancy_reg/',views.CONSULTANCY_REGfn,name="consultancy_registration"),
    
    path('hs_profile/',views.hs_profile,name="HS_Profile"),
    path('up_profile/<int:upid>',views.hs_upProf,name="Up_Profile"),
    path('hs_changepass/<int:cuid>',views.hs_changepass,name="HS_ChangePwd"),

    path('feedback/',views.feedback,name="Feedback"),
    path('dltfeedback/<int:delid>',views.dltFEEDBACKfn,name="dlt-HOS_FEEDBACK"),

    path('complaint/',views.complaint,name="Complaint"),
    path('dltcomplaint/<int:delid>',views.dltCOMPLAINTfn,name="dlt-HOS_complaint"),

]