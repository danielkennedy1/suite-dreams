from core.models import Booking, Room


def create_booking(request):
    organiser, date, start, end, title, details, room_id = request.POST.get('organiser'), request.POST.get('date'), request.POST.get('start'), request.POST.get('end'), request.POST.get('title'), request.POST.get('details'), request.POST.get('room')
    room = Room.objects.get(id=room_id)
    booking = Booking.objects.create(organiser=organiser, date=date, start_time=start, end_time=end, room=room,  title=title, details=details)
    booking.save()