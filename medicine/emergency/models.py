from django.db import models

class Department(models.Model):
    dep_name=models.TextField(max_length=20)
    dep_desc=models.TextField(max_length=100)
    def __str__(self):
        return self.dep_name
class Doctore(models.Model):
    doc_name=models.TextField(max_length=20)
    doc_image=models.TextField(max_length=200)
    doc_dep=models.ForeignKey(Department, models.CASCADE)
    def __str__(self):
        return self.doc_name
class Booking(models.Model):
    name=models.TextField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    doctor=models.ForeignKey(Doctore, models.CASCADE)
    booked=models.DateField()
    time=models.TimeField()
    decs=models.TextField(max_length=500)
    def __str__(self):
        return self.name
