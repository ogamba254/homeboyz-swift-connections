import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','bs_project.settings')
import django
django.setup()
from bookingApp.models import Route
print('ROUTE COUNT:', Route.objects.count())
print('ORIGINS:', list(Route.objects.values_list('origin', flat=True)))
