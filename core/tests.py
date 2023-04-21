from django.test import TestCase
from core.factories import RoomFactory

class RoomTestCase(TestCase):
    def test_room_creation(self):
        room = RoomFactory(name="Test Room", capacity=10)
        self.assertEqual(room.name, "Test Room")
        self.assertEqual(room.capacity, 10)
        

		