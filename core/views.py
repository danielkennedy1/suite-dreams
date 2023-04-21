from django.shortcuts import render


# Create your views here.
def book(request):
    return render(request, 'book.html')


def index(request):
    return render(request, 'index.html')
