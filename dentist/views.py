from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

import os

# Create your views here.
# create a view for the login page of dentist app
def dentist_project_login(request):
    template = loader.get_template('dentist_project_login.html')
    return render(request, 'dentist_project_login.html')



# create a view for the home page of dentist app
def dentist_project_home(request):
    return render(request, 'dentist_project_home.html')
# # create a view for the about page of dentist app
# def dentist_project_about(request):
#     template = loader.get_template('dentist_project_about.html')
#     return HttpResponse(template.render(request
#     ))

# # create a view for the contact page of dentist app
# def dentist_project_contact(request):
#     template = loader.get_template('dentist_project_contact.html')
#     return HttpResponse(template.render(request
#     ))

# general_dental_care 
def general_dental_care(request):
    return render(request, 'general_dental_care.html')

#appointment_schedule
def appointment_schedule(request):
    return render(request, 'appointment_schedule.html')

#procedures
def procedures(request):
    return render(request, 'procedures.html')