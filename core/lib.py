from core.models import Booking, Room
from django.core.exceptions import ValidationError
from django.utils import timezone

# Check that booking does not overlap with another booking
def booking_overlaps(booking):
    bookings = Booking.objects.filter(room=Room.objects.get(id=booking['room_id']), date=booking['date'])
    new_start_time = timezone.datetime.strptime(booking["start_time"], "%H:%M").time()
    new_end_time = timezone.datetime.strptime(booking["end_time"], "%H:%M").time()

    for b in list(bookings):
        if not (
            (new_start_time < b.start_time and new_end_time <= b.start_time) # before
            or 
            (new_start_time >= b.end_time and new_end_time > b.end_time) # after
            ):
            return True
    return False

# Check that booking fields arent empty

def create_booking(booking):

    errors = []

    # Check if the organiser, title, or details fields are empty
    for field in ["organiser", "title", "details"]:
        if booking[field] == "":
            errors.append(ValidationError(f"{field} cannot be empty", code=f"empty_{field}"))
    
    # Check that booking start time is after opening time (9:00)
    if timezone.datetime.strptime(booking["start_time"], "%H:%M").time() < timezone.datetime.strptime("09:00", "%H:%M").time():
        errors.append(ValidationError("Booking start time is outside of opening hours", code='start_too_early', params={'start_time': booking['start_time']}))
    
    # Check that booking end time is before closing time (17:00)
    if timezone.datetime.strptime(booking["end_time"], "%H:%M").time() > timezone.datetime.strptime("17:00", "%H:%M").time():
        errors.append(ValidationError("Booking end time is outside of opening hours", code='end_too_late', params={'end_time': booking['end_time']}))

    # Check that booking start time is before booking end time
    if timezone.datetime.strptime(booking["start_time"], "%H:%M").time() >= timezone.datetime.strptime(booking["end_time"], "%H:%M").time():
        errors.append(ValidationError("Booking start time is after booking end time", code='start_after_end', params={'start_time': booking['start_time'], 'end_time': booking['end_time']}))
    
    # Check that booking does not overlap with another booking
    if booking_overlaps(booking):
        errors.append(ValidationError("Booking overlaps with another booking", code='overlap', params={'date': booking['date'], 'start_time': booking['start_time'], 'end_time': booking['end_time']}))

    if errors:
        raise ValidationError(errors)

    Booking.objects.create(
                        organiser=booking['organiser'], 
                        date=booking['date'], 
                        start_time=booking['start_time'], 
                        end_time=booking['end_time'], 
                        room=Room.objects.get(id=booking['room_id']),  
                        title=booking['title'], 
                        details=booking['details']
    )