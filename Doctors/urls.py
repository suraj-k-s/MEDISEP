from django.urls import path
from Doctors import views
app_name='doctor'

urlpatterns = [
    path('dr_home/',views.dr_home,name="DR_Home"),
    path('dr_profile/',views.dr_profile,name="Dr_Profile"),
    path('up_profile/<int:upid>',views.dr_upProf,name="Up_Profile"),
    path('dr_changepass/<int:cuid>',views.dr_changepass,name="Dr_ChangePwd"),
    path('feedback/',views.feedback,name="Feedback"),
    path('dltfeedback/<int:delid>',views.dltFEEDBACKfn,name="dlt-DR_FEEDBACK"),

    path('viewbookings/',views.acceptedbookings,name="Viewbookings"),
    path('medicinedetails/<int:mid>',views.medicinedetails,name="medicinedetails"),
    path('search_history/',views.search_history,name="Search_History"),
]