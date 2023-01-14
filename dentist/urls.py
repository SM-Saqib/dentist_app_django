from django.urls import path
from . import views

urlpatterns = [
    path('', views.dentist_project_login, name='dentist_project_login'),
    path('dentist_project_home/', views.dentist_project_home, name='dentist_project_home'),
    path('general_dental_care/', views.general_dental_care, name='general_dental_care'),
    path('appointment_schedule/', views.appointment_schedule, name='appointment_schedule'),
    path('procedures/', views.procedures, name='procedures'),

]

