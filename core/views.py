from django.shortcuts import redirect, render
from core.lib import create_booking, delete_booking
from core.models import Booking, Room


def book(request):
    if request.method == 'POST':
        booking = {
            "organiser": request.POST.get('organiser'),
            "date": request.POST.get('date'),
            "start_time": request.POST.get('start_time'),
            "end_time": request.POST.get('end_time'),
            "room_id": request.POST.get('room_id'),
            "title": request.POST.get('title'),
            "details": request.POST.get('details')
        }
        try:
            create_booking(booking)
        except Exception as e:
            return render(request, 'book.html', {'rooms': Room.objects.all(), 'error_messages': e, 'booking': booking, "room_id": int(booking["room_id"])})

        return redirect('index')
    else:

        return render(request, 'book.html', {'rooms': Room.objects.all()})


def delete(request, id):
    try:
        delete_booking(id)

    except Exception as e:
        return render(request, 'index.html', {'bookings': Booking.objects.all(), 'error': e}, status=404)
    return redirect('index')


def index(request):
    return render(request, 'index.html', {'bookings': Booking.objects.all()})
