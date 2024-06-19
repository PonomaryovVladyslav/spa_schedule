from django.contrib import admin
from .models import Employee, Schedule, Record, Procedure
# Register your models here.

admin.site.register(Employee)
admin.site.register(Schedule)
admin.site.register(Record)
admin.site.register(Procedure)