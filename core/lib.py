from core.models import Booking, Room

def create_booking(request):
    room = Room.objects.get(id=request.POST.get('room'))
    Booking.objects.create(
                        organiser=     request.POST.get('organiser'), 
                        date=          request.POST.get('date'), 
                        start_time=    request.POST.get('start'), 
                        end_time=      request.POST.get('end'), 
                        room=          room,  
                        title=         request.POST.get('title'), 
                        details=       request.POST.get('details')
    )