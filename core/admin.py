from django.contrib import admin

# Register your models here.

from core.models import Booking, Room

admin.site.register(Booking)
admin.site.register(Room)