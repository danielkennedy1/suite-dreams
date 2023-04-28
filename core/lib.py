from core.models import Booking, Room
from django.core.exceptions import ValidationError
from django.utils import timezone

def create_booking(booking):
    errors = []

    # 1. Organiser is not empty
    if not booking['organiser']:
        errors.append(ValidationError("Organiser cannot be empty", code='invalid_organiser', params={'organiser': booking['organiser']}))
    
    # 2. Room id is valid
    if not Room.objects.filter(id=booking['room_id']).exists():
        errors.append(ValidationError("Invalid room id", code='invalid_room_id', params={'room_id': booking['room_id']}))
    
    # 3. Date is valid
    try:
        booking['date'] = timezone.datetime.strptime(booking['date'], '%Y-%m-%d').date()
    except ValueError:
        errors.append(ValidationError("Invalid date", code='invalid_date', params={'date': booking['date']}))
    
    # 4. Start time is valid
    try:
        booking['start_time'] = timezone.datetime.strptime(booking['start_time'], '%H:%M').time()
    except ValueError:
        errors.append(ValidationError("Invalid start time", code='invalid_start_time', params={'start_time': booking['start_time']}))
    
    # 5. End time is valid
    try:
        booking['end_time'] = timezone.datetime.strptime(booking['end_time'], '%H:%M').time()
    except ValueError:
        errors.append(ValidationError("Invalid end time", code='invalid_end_time', params={'end_time': booking['end_time']}))
    
    # 6. Start time is before end time
    if booking['start_time'] > booking['end_time']:
        errors.append(ValidationError("Start time must be before end time", code='invalid_start_end_time', params={'start_time': booking['start_time'], 'end_time': booking['end_time']}))
    
    # 7. Booking is in the future
    start_dateTime = timezone.datetime.combine(booking['date'], booking['start_time'])
    if start_dateTime < timezone.now().replace(tzinfo=None):
        errors.append(ValidationError("Booking cannot be in the past", code='booking_in_past', params={'start_dateTime': start_dateTime}))
    
    # 8. Organiser is too long (max 100 chars)
    if len(booking['organiser']) > 100:
        errors.append(ValidationError("Organiser is too long, max 100 characters", code='organiser_too_long', params={'organiser': booking['organiser']}))

    # 9. Title is too long (max 100 chars)
    if len(booking['title']) > 100:
        errors.append(ValidationError("Title is too long, max 100 characters", code='title_too_long', params={'title': booking['title']}))

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