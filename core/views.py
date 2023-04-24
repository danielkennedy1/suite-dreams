from django.shortcuts import redirect, render

from core.models import Booking


# Create your views here.
def book(request):
    return render(request, 'book.html')


def index(request):
    return render(request, 'index.html')

def create_booking(request, method=["POST"]):
    organiser = request.POST.get('organiser')
    date = request.POST.get('date')
    start = request.POST.get('start')
    end = request.POST.get('end')
    room = request.POST.get('room')

    booking = Booking.objects.create(organiser=organiser, date=date, start_time=start, end_time=end, room=room)
    booking.save()

    return redirect('index')