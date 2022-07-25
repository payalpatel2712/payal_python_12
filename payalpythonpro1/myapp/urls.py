from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about-us/',views.about,name='about-us'),
    path('gallery/',views.gallery,name='gallery'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('otp/',views.otp,name="otp"),
    path('newpassword/',views.newpassword,name="newpassword"),
    path('contact/',views.contact,name='contact'),
    path('logout/',views.logout,name='logout'),
    path('doctor_index/',views.doctor_index,name='doctor_index'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('doctors/',views.doctors,name='doctors'),
    path('doctor_detail/<int:pk>/',views.doctor_detail,name='doctor_detail'),
    path('doctorappointment/',views.doctorappointment,name='doctorappointment'),
    path('doctor_aprove_appointment/<int:pk>/',views.doctor_aprove_appointment,name='doctor_aprove_appointment'),
    path('doctor_cencel_appointment/<int:pk>/',views.doctor_cencel_appointment,name='doctor_cencel_appointment'),
    path('doctor_complete_appointment/<int:pk>/',views.doctor_complete_appointment,name='doctor_complete_appointment'),

    path('bookappointment/<int:pk>/',views.bookappointment,name='bookappointment'),
    path('myappointment/',views.myappointment,name='myappointment'),
    path('patient_cancel_appointment/<int:pk>/',views.patient_cancel_appointment,name='patient_cancel_appointment'),
    path('helth_profile',views.helth_profile,name='helth_profile'),

    ]
