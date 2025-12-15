from django.urls import path
from . import views


urlpatterns = [
    path('',views.manage_iple,name="iple"),
    path('Schools',views.manage_schools,name="schools"),
    path('Passslip',views.manage_passslip,name="passslip"),
    path('Registration',views.manage_registration,name="registration"),
    path('About_us',views.manage_about_us,name="about_us"),
]