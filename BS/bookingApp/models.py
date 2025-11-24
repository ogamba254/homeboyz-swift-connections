from django.db import models

class Bus(models.Model):
    number_plate = models.CharField(max_length=20)
    capacity = models.IntegerField()

    def __str__(self):
        return self.number_plate

class Route(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()

    def __str__(self):
        return f"{self.origin} → {self.destination}"

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger.name} - Seat {self.seat_number}"
