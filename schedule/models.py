from datetime import timedelta

from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


PROCEDURE_TYPE = (
    (timedelta(minutes=60), "Regular"),
    (timedelta(minutes=90), "Long"),
)


class Procedure(models.Model):
    name = models.CharField(max_length=100)
    time_duration = models.DurationField(choices=PROCEDURE_TYPE)


class Schedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Record(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    start_time = models.TimeField()

    def __str__(self):
        return f"Procedure duration: {self.procedure.time_duration}\n start time: {self.start_time}"