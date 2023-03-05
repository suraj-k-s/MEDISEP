from django.urls import path
from Employee import views
app_name='employee'

urlpatterns = [
    path('emp_home/',views.emp_home,name="Emp_Home"),
    path('emp_profile/',views.emp_profile,name="Emp_Profile"),
    path('up_profile/<int:upid>',views.emp_upProf,name="Up_Profile"),
    path('emp_changepass/<int:cuid>',views.emp_changepass,name="Emp_ChangePwd"),
    path('mem_reg/',views.mem_reg,name="MEM_REG"),   
    path('claimreport/',views.viewclaimreport,name="ViewClaimReport"),  
    path('dtmem/<int:dmid>',views.dltmem,name="Dlt_MemReg"),
    
    path('viewmembers/<int:vmid>',views.view_memreg_details,name="view_mem_details"),  
    path('dtmember/<int:dmmid>',views.dltmemd,name="Dlt_MemDetails"),
    path('upMEM_DETAILS/<int:uppid>',views.upMEM_DETAILSfn,name="Up-MemDetails"),
]