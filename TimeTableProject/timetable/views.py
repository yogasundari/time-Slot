from django.shortcuts import render
from .models import TimeSlot

def timetable_view(request):
    time_table = TimeSlot.objects.all()
    return render(request,'timetable.html', {'time_table': time_table})

# Create your views here.
