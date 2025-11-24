
from django.shortcuts import render
from .models import Bus, Route, Booking

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def schedules(request):
    # Optionally pass routes/buses if needed
    return render(request, 'schedules.html')

def payment(request):
    return render(request, 'payment.html')

def view_booking(request):
    return render(request, 'view_booking.html')

def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')

def seat_selection(request):
    buses = Bus.objects.all()
    routes = Route.objects.all()
    return render(request, 'seat_selection.html', {'buses': buses, 'routes': routes})

def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'booking _history.html', {'bookings': bookings})
