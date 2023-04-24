from django.shortcuts import redirect, render

from core.models import Booking, Room

def book(request):
    if request.method == 'POST':
        create_booking(request)
        return redirect('index')

    rooms = Room.objects.all()
    return render(request, 'book.html', {'rooms': rooms})


def index(request):
    bookings = Booking.objects.all()
    
    return render(request, 'index.html', {'bookings': bookings})

def create_booking(request):
    organiser = request.POST.get('organiser')
    date = request.POST.get('date')
    start = request.POST.get('start')
    end = request.POST.get('end')
    title = request.POST.get('title')
    details = request.POST.get('details')

    room = Room.objects.get(id=request.POST.get('room'))

    booking = Booking.objects.create(organiser=organiser, date=date, start_time=start, end_time=end, room=room,  title=title, details=details)
    booking.save()
