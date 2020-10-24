from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor+"--"+self.patient


class BlockChain(models.Model):
    block_chain = models.TextField()

    def __str__(self):
        return self.block_chain