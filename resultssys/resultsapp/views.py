from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

from .models import *
from .schools_selector import(get_schools,get_school)
from .student_selector import(get_students, get_student)
from .homepage_selector import(get_all_about_us, get_about_us, get_schedules,get_schedule)

# Create your views here

# HOME PAGE
def manage_iple(request):
    get_single_schedules = get_schedules()
    context={
        "get_single_schedules":get_single_schedules,
    }
    return render(request, 'resultsapp/index.html', context)


# SCHOOLS
def manage_schools(request):

    get_all_schools = get_schools()
    
    context={
        "get_all_schools":get_all_schools,
        
    }
    return render(request, 'resultsapp/schools.html', context)
   

# PASSSLIP PAGE
def manage_passslip(request):
    
    context={
        
    }
    return render(request, 'resultsapp/pass_slip.html', context)

# STUDENTS PAGE
def manage_student_in_students(request):

    get_all_students = get_students()
    
    context={
        "get_all_schools":get_all_students,
        
    }
    
# REGISTRATION

def manage_registration(request):
    
    context={
        
    }
    return render(request, 'resultsapp/registration.html', context)

# ABOUT US

def manage_about_us(request):

    get_all_aboutus = get_all_about_us()
    context={
        "get_all_aboutus":get_all_aboutus,
    }
    return render(request, 'resultsapp/about_us.html', context)