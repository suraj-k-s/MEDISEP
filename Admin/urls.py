from django.urls import path
from Admin import views
app_name='webadmin'

urlpatterns = [
    path('A_Home/',views.adminhome,name="Admin_Home"),
    path('dist/',views.dis,name="District"), 
    path('dltdis/<int:delid>',views.dltdis,name="Dlt-Dis"), #deletion path of district
    path('updis/<int:upid>',views.updis,name="Up-Dis"), #updation path of district

    path('place/',views.pla,name="Place"), 
    path('dltplace/<int:delid>',views.dltpla,name="Dlt-place"), #deletion path of place
    path('upplace/<int:uppid>',views.uppla,name="Up-place"), #updation path of place
   

    path('cmptype/',views.COMPTYPE,name="Cmptype"), 
    path('dltcmptype/<int:delid>',views.dltCOMPTYPE,name="dlt-COMPTYPE"), #deletion path of comlaint type
    path('upcmptype/<int:uppid>',views.upCOMPTYPE,name="Up-COMPTYPE"), #updation path of complaint type

    path('hsptltype/',views.HSPTLTYPEfn,name="Hsptltype"), 
    path('dlthsptltype/<int:delid>',views.dltHSPTLTYPEfn,name="dlt-HSPTLTYPE"), #deletion path of comlaint type
    path('uphsptltype/<int:uppid>',views.upHSPTLTYPEfn,name="Up-HSPTLTYPE"), #updation path of complaint type

    path('emp_department/',views.EMP_DEPTfn,name="emp_department"),
    path('dltemp_dept/<int:delid>',views.dltEMP_DEPTfn,name="dlt-EMP_DEPARTMENT"), #deletion path of doctor department
    path('upemp_dept/<int:uppid>',views.upEMP_DEPTfn,name="Up-EMP_DEPT"), #updation path of complaint type

    path('emp_subdepartment/',views.EMP_SUBDEPTfn,name="emp_subdepartment"), 
    path('dltemp_subdept/<int:delid>',views.dltEMP_SUBDEPTfn,name="dlt-EMP_SUBDEPARTMENT"), #deletion path of sub department
    path('upemp_subdept/<int:uppid>',views.upEMP_SUBDEPTfn,name="Up-EMP_SUBDEPARTMENT"), #updation path of complaint type

    path('dr_department/',views.DR_DEPTfn,name="dr_department"),
    path('dltdr_det/<int:delid>',views.dltDR_DEPARTMENTfn,name="dlt-DR_DEPARTMENT"), #deletion path of doctor department
    path('updr-dept/<int:uppid>',views.upDR_DEPARTMENTfn,name="Up-DR_DEPARTMENT"), #updation path of complaint type
    
    path('emp_gradepost/',views.EMP_GRADEPOSTfn,name="emp_gradepost"), 
    path('ajax_subdep/',views.AjaxSubDep,name="Ajax-SubDep"),
    path('dltemp_gradepost/<int:delid>',views.dltEMP_GRADEPOSTfn,name="dlt-EMP-GRADEPOST"),
    

    path('emp_reg/',views.EMP_REGfn,name="emp_registration"),
    path('ajax_gradepost/',views.AjaxGrade,name="Ajax-Grade"),
    path('dltemp_reg/<int:delid>',views.dltEMP_REGfn,name="dlt-EMP_REGISTRATION"), #deletion path employee reg
    path('history_backup/',views.history_backup,name="History-Backup"),
    path('accptemp/<int:aid>',views.accptemp,name="Accept_Emp"),
    

    path('hos_reg/',views.HOS_REGfn,name="hos_registration"),
    path('dlthos_reg/<int:delid>',views.dltHOS_REGfn,name="dlt-HOS_REGISTRATION"),
    path('viewclaims/',views.viewClaims,name="ViewClaims"),  
    path('acceptclaim/<int:cid>',views.acceptclaim,name="AcceptClaim"), 
    path('rejctclaim/<int:rid>',views.rejectclaim,name="RejectClaim"), 
    path('insure/<int:eid>',views.insure,name="add-insur"),
    path('viewcmp/',views.viewcomplaints,name="viewcomplaints"),  
    path('viewfeedbacks/',views.viewfeedbacks,name="viewfeedbacks"),  

]