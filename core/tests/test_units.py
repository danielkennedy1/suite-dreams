from django.test import TestCase
from core.lib import create_booking
from core.models import Room, Room
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from unittest.case import _AssertRaisesContext

import sys

class CreateBookingTestCase(TestCase):

    def display_code(self, err: _AssertRaisesContext):
        error = "\n\nEXCEPTION CODE: " + str(err.exception.code) + "  <------" + "\n\n"
        sys.stderr.write(str(error))
    
    def display_error(self, err: _AssertRaisesContext):
        error = "\n\nEXCEPTION>" + str(err.exception) + "<------" + "\n\n"
        sys.stderr.write(str(error))

    def display(self, val):
        sys.stderr.write(val)	

    def setUp(self):
        self.correct_booking = {
            "organiser": "Test",
             "date": "2024-01-01",
             "start_time": "10:00",
             "end_time": "11:00",
             "room_id": 1,
             "title": "Test",
             "details": "Test"
        } 
        Room.objects.create(id=1, name="Test Room", capacity=1)

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
            
    
    def test_create_booking(self):
        create_booking(self.correct_booking)
        self.assertTrue(True)
    
    #Book a room that doesn't exist
    def test_create_booking_invalid_room(self):
        booking = self.correct_booking.copy()
        booking["room_id"] = 100
        with self.assertRaises(Room.DoesNotExist):
            create_booking(booking)
    
    #invalid date
    def test_create_booking_invalid_date(self):
        booking = self.correct_booking.copy()
        booking["date"] = "2024-01-32"
        with self.assertRaises(ValidationError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.code, "invalid_date")
    
    #empty fields
    def test_create_booking_empty_fields(self):
        for field in ["organiser"]:#, "title", "details"]:
            booking = self.correct_booking.copy()
            booking[field] = ""
            with self.assertRaises(ValidationError) as e:
                create_booking(booking)
                self.assertEqual(e.exception.code, f"empty_{field}")

    #invalid time
    def test_create_booking_invalid_time(self):
        booking = self.correct_booking.copy()
        booking["start_time"] = "25:00"
        with self.assertRaises(ValueError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.args[0], "time data '25:00' does not match format '%H:%M'")
    
    #booking too early (before 9am)
    def test_create_booking_too_early(self):
        booking = self.correct_booking.copy()
        booking["start_time"] = "07:00"
        with self.assertRaises(ValidationError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.code, "start_too_early")

    #booking too late (after 5pm)
    def test_create_booking_too_late(self):
        booking = self.correct_booking.copy()
        booking["end_time"] = "17:01"
        with self.assertRaises(ValidationError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.code, "end_too_late")
