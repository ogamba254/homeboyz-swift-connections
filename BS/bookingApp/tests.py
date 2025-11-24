from django.test import TestCase
from .models import Bus

class BusModelTest(TestCase):
    def test_create_bus(self):
        bus = Bus.objects.create(number_plate="KAA 123X", capacity=50)
        self.assertEqual(bus.number_plate, "KAA 123X")
