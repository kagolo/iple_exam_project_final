from django.urls import path
from . import views


urlpatterns = [
    path('',views.manage_iple,name="iple"),
    path('Schools',views.manage_schools,name="schools"),
    path('school/<int:school_id>/',views.manage_single_school,name="school"),
    path('Passslip/<int:school_id>/',views.manage_passslip,name="passslip"),
    path('Registration',views.manage_registration,name="registration"),
    path('About_us',views.manage_about_us,name="about_us"),
    path('Students',views.manage_student_in_students,name="student"),
    path("Contact",views.Manage_contact_us,name="contact"),
    path('Results-pdf/', views.generate_pdf, name='results_pdf'),
]  