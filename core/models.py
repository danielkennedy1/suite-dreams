from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.capacity} pax)"


class Booking(models.Model):

    id = models.IntegerField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    organiser = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    details = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f"{self.room} - {self.date} - {self.start_time} - {self.end_time}"
    
    class Meta:
        constraints = [
            #models.UniqueConstraint(fields=['room', 'date', 'start_time'], name='unique_booking'),
            #models.CheckConstraint(check=models.Q(start_time__lt=models.F('end_time')), name='start_time_before_end_time'),
            #models.CheckConstraint(check=models.Q(start_time__gte=timezone.time.strptime("09:00")), name='start_time_after_opening_time'),
        ]
    
