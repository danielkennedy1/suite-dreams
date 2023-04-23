from django.test import TestCase
from core.factories import RoomFactory
from core.factories import BookingFactory

class RoomTestCase(TestCase):
    def test_room_creation(self):
        room = RoomFactory(name="Test Room", capacity=10)
        self.assertEqual(room.name, "Test Room")
        self.assertEqual(room.capacity, 10)
        
class BookingTestCase(TestCase):
    def setUp(self):
        self.room = RoomFactory()
        self.booking = BookingFactory.build(room=self.room)

    def test_booking_room_association(self):
        self.assertEqual(self.booking.room, self.room)
        