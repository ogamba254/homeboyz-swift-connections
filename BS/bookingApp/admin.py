from django.contrib import admin
from .models import Bus, Route, Booking, Passenger

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Booking)
admin.site.register(Passenger)
