from django.shortcuts import redirect, render

from core.models import Booking, Room

def book(request):
    x = Room(name="Room 1", capacity=10)
    x.save()

    rooms = Room.objects.all()
    return render(request, 'book.html', {'rooms': rooms})


def index(request):
    bookings = Booking.objects.all()
    return render(request, 'index.html', {'bookings': bookings})

def create_booking(request, method=["POST"]):
    organiser = request.POST.get('organiser')
    date = request.POST.get('date')
    start = request.POST.get('start')
    end = request.POST.get('end')

    room = Room.objects.get(id=request.POST.get('room'))

    booking = Booking.objects.create(organiser=organiser, date=date, start_time=start, end_time=end, room=room)
    booking.save()

    return redirect('index')