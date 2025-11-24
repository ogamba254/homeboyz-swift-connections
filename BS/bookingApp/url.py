from django.urls import path
from . import views

urlpatterns = [
    path('seats/', views.seat_selection, name='seat_selection'),
    path('history/', views.booking_history, name='booking_history'),
]
