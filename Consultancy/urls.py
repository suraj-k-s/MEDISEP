from django.urls import path
from Consultancy import views
app_name='consultancy'

urlpatterns = [
    path('consultancy_home/',views.cn_home,name="CN_Home"),
    path('con_profile/',views.con_profile,name="Con_Profile"),
    path('up_profile/<int:upid>',views.con_upProf,name="Up_Profile"),
    path('con_changepass/<int:cuid>',views.con_changepass,name="Con_ChangePwd"),
    path('viewdoc/',views.viewdoc,name="viewdoc"),
    path('Add-Avail/<int:did>',views.adddc,name="Add-av"),
    path('dltavail/<int:delid>',views.availfn,name="dlt-avail"),

    path('tokengen/<int:avid>',views.token,name="genaratetoken"),
    path('dlttoken/<int:did>',views.dlt_token,name="dlt-token"),
    

    path('viewbookings/',views.viewbookings,name="viewbook"),
    path('feedback/',views.feedback,name="Feedback"),
    path('dltfeedback/<int:delid>',views.dltFEEDBACKfn,name="dlt-CONSULTANCY_FEEDBACK"),

    path('complaint/',views.complaint,name="Complaint"),
    path('dltcomplaint/<int:delid>',views.dltCOMPLAINTfn,name="dlt-CONSULTANCY_complaint"),

    path('accept/<int:aid>',views.accept,name="acceptbook"),
    path('reject/<int:rid>',views.reject,name="rejectbook"),
    path('acceptedbookings/',views.acceptedbookings,name="acceptedbookings"),
    path('rejectedbookings/',views.rejectedbookings,name="rejectedbookings"),
    path('viewmedicine/<int:aid>',views.viewmedicine,name="viewmedicine"),
    path('applyclaim/<int:aid>',views.applyclaim,name="applyclaim"),
    path('viewreq/',views.viewClaims,name="viewerequest"),
    
]