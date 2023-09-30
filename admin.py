# hostel_app/admin.py
from django.contrib import admin
from .models import Hostel, Student

admin.site.register(Hostel)
admin.site.register(Student)
