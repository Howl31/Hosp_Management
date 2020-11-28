from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *
import hashlib
# Create your views here.


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d_count = 0
    p_count = 0
    a_count = 0
    for i in doctor:
        d_count += 1
    for i in patient:
        p_count += 1
    for i in appointment:
        a_count += 1
    d = {'d_count': d_count, 'p_count': p_count, 'a_count': a_count}
    return render(request, 'index.html', d)


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def admin_logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['dname']
        c = request.POST['dcontact']
        sp = request.POST['spcl']
        try:
            Doctor.objects.create(name=n, contact=c, specialization=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)


def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n1 = request.POST['pname']
        c2 = request.POST['pcontact']
        gn = request.POST['gender']
        try:
            Patient.objects.create(name=n1, contact=c2, gender=gn)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def delete_patient(request, p1id):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=p1id)
    patient.delete()
    return redirect('view_patient')


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    d = {'app': app}
    return render(request, 'view_appointment.html', d)


def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d1 = request.POST['doctor']
        p = request.POST['patient']
        d2 = request.POST['date']
        tm = request.POST['time']
        doctor = Doctor.objects.filter(name=d1).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d2, time1=tm)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'doctor': doctor1, 'patient': patient1}
    return render(request, 'add_appointment.html', d)


def delete_appointment(request, p1id):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=p1id)
    appointment.delete()
    return redirect('view_appointment')
