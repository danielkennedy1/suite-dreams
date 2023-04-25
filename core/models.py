from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.capacity} pax)"


class Booking(models.Model):

    def clean(self) -> None:
        start_dateTime = timezone.datetime.combine(self.date, self.start_time)
        if start_dateTime < timezone.now():
            raise ValidationError("Booking cannot be in the past")
        if start_dateTime > end_dateTime:
            raise ValidationError("Booking start time must be before end time")
        

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
