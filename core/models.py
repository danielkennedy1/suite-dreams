from django.db import models

# Create your models here.


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.capacity}"


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f"{self.room} - {self.date} - {self.start_time} - {self.end_time}"
