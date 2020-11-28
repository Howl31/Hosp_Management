"""hosp_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.index, name='home'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('delete_doctor(?p<int:pid>)/', views.delete_doctor, name='delete_doctor'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('delete_patient(?p<int:p1id>)/', views.delete_patient, name='delete_patient'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('delete_appointment(?p<int:p1id>)/', views.delete_appointment, name='delete_appointment'),
]
