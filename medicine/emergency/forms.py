from django import forms
from .models import Booking
from django.forms import TextInput, Select, Textarea

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['name','email','phone','doctor','booked','time','decs']
        widgets={
            'name':TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "placeholder":"Your Name",
                "style":"height: 55px;",
                "name":"name"
            }),
            'email':TextInput(attrs={
                    "type":"email",
                    "class":"form-control border-0",
                    "placeholder":"Your Email",
                    "style":"height: 55px;",
                    "name":"email"
            }),
            'phone':TextInput(attrs={
                    "type":"phone", 
                    "class":"form-control border-0", 
                    "placeholder":"Your Mobile", 
                    "style":"height: 55px;",
                    "name":"phone"
            }),
            'doctor':Select(attrs={
                    "class":"form-select border-0", 
                    "style":"height: 55px;",
                    "name":"doctor"
            }),
            'booked':TextInput(attrs={
                      "type":"date",
                      "class":"form-control border-0 datetimepicker-input",
                      "placeholder":"Choose Date", 
                      "style":"height: 55px;",
                      "name":"booked"
            }),
            'time':TextInput(attrs={
                       "type":"time",
                        "class":"form-control border-0 datetimepicker-input",
                        "placeholder":"Choose Date",
                        "style":"height: 55px;",
                        "name":"time",

            }),
            'decs':Textarea(attrs={
                "type":"textarea",
                "class":"form-control border-0",
                "placeholder":"Describe your problem",
                "rows":"5",
                "name":"decs"
            })
        }