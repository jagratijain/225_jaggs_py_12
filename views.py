# hostel_app/views.py
from django.shortcuts import render
from .models import Hostel, Student

def index(request):
    hostels = Hostel.objects.all()
    students = Student.objects.all()
    return render(request, 'hostel_app/index.html', {'hostels': hostels, 'students': students})
