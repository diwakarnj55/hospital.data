from django.shortcuts import render, redirect
from . models import Department, Doctore
from . forms import BookingForm

def index(request):
    dep=Department.objects.all()
    doc=Doctore.objects.all()
    form=BookingForm()
    data ={
        "dep":dep,
        "doc":doc,
        "form":form
    }
    if request.method=="POST":
        booking=BookingForm(request.POST)
        if booking.is_valid():
            booking.save()
            return render(request,"index.html",data)

    return render(request,"index.html",data)
