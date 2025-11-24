
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('schedules/', views.schedules, name='schedules'),
    path('seats/', views.seat_selection, name='seat_selection'),
    path('history/', views.booking_history, name='booking_history'),
    path('payment/', views.payment, name='payment'),
    path('view-booking/', views.view_booking, name='view_booking'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
