from django.shortcuts import redirect, render
from core.lib import create_booking
from core.models import Booking, Room

def book(request):
    if request.method == 'POST':
        create_booking(request)
        return redirect('index')
    else: 
        return render(request, 'book.html', {'rooms': Room.objects.all()})


def index(request):
    return render(request, 'index.html', {'bookings': Booking.objects.all()})


