from django.db import models

# Create your models here.
class TimeSlot(models.Model):
    day = models.CharField(max_length=10)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    class_room = models.CharField(max_length=10)