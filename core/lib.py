from core.models import Booking, Room
from django.core.exceptions import ValidationError
from django.utils import timezone

def create_booking(booking):

    # Check if the organiser, title, or details fields are empty
    for field in ["organiser", "title", "details"]:
        if booking[field] == "":
            raise ValidationError(f"{field} cannot be empty", code=f"empty_{field}")
    
    # Check that booking start time is after opening time (9:00)
    if timezone.datetime.strptime(booking["start_time"], "%H:%M").time() < timezone.datetime.strptime("09:00", "%H:%M").time():
        raise ValidationError("Booking start time is outside of opening hours", code='start_too_early', params={'start_time': booking['start_time']})
    
    # Check that booking end time is before closing time (17:00)
    if timezone.datetime.strptime(booking["end_time"], "%H:%M").time() > timezone.datetime.strptime("17:00", "%H:%M").time():
        raise ValidationError("Booking end time is outside of opening hours", code='end_too_late', params={'end_time': booking['end_time']})

    Booking.objects.create(
                        organiser=booking['organiser'], 
                        date=booking['date'], 
                        start_time=booking['start_time'], 
                        end_time=booking['end_time'], 
                        room=Room.objects.get(id=booking['room_id']),  
                        title=booking['title'], 
                        details=booking['details']
    )