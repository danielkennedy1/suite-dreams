from django.shortcuts import redirect, render
from core.lib import create_booking
from core.models import Booking, Room

def book(request):
    if request.method == 'POST':
        create_booking(
            {
            "organiser": request.POST.get('organiser'),
             "date": request.POST.get('date'),
             "start_time": request.POST.get('start'),
             "end_time": request.POST.get('end'),
             "room_id": request.POST.get('room'),
             "title": request.POST.get('title'),
             "details": request.POST.get('details')
            }
        )
        return redirect('index')
    else: 
        return render(request, 'book.html', {'rooms': Room.objects.all()})


def index(request):
    return render(request, 'index.html', {'bookings': Booking.objects.all()})


