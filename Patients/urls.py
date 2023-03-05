from django.urls import path
from Patients import views
app_name='patient'

urlpatterns = [
    path('mem_home/',views.mem_home,name="MEM_Home"),
    path('mem_profile/',views.m_profile,name="Mem_Profile"),
    path('up_profile/<int:upid>',views.m_upProf,name="Up_Profile"),
    path('mem_changepass/<int:cmid>',views.M_changepass,name="M_ChangePwd"),
    path('doclist/<int:hid>',views.doclist,name="doclist"),
    path('viewavail/<int:did>',views.viewavail,name="viewavail"),
    path('viewtoken/<int:avid>',views.viewtoken,name="viewtoken"),
    path('booktoken/<int:tid>',views.booktoken,name="BookToken"),
    path('searchHosptl/',views.SearchHos,name="SearchHospital"),
    path('feedback/',views.feedback,name="Feedback"),
    path('dltfeedback/<int:delid>',views.dltFEEDBACKfn,name="dlt-PATIENT_FEEDBACK"),
    path('complaint/',views.complaint,name="Complaint"),
    path('dltcomplaint/<int:delid>',views.dltCOMPLAINTfn,name="dlt-PATIENT_COMPLAINT"),
]