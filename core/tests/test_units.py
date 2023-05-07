from django.test import TestCase
from core.lib import create_booking, booking_overlaps
from core.models import Room, Booking
from django.core.exceptions import ValidationError
from unittest.case import _AssertRaisesContext
import sys
from parameterized import parameterized
import datetime

class CreateBookingTestCase(TestCase):

    # TODO - Delete these methods when done

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
        self.correct_booking_2 = self.correct_booking.copy()
        self.correct_booking_2["date"] = "2024-01-02"
        Room.objects.create(id=1, name="Test Room", capacity=1)
        Booking.objects.create(
            id=1, 
            room_id=1, 
            organiser="Test", 
            title="Test", 
            details="Test", 
            start_time="10:00", 
            end_time="11:00", 
            date="2024-01-02"
        )

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
            
    
    def test_1create_booking(self):
        create_booking(self.correct_booking)        
        self.assertTrue(True)
    
    #Book a room that doesn't exist
    def test_create_booking_invalid_room(self):
        booking = self.correct_booking.copy()
        booking["room_id"] = 100
        booking["date"] = "2024-01-03"
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
    @parameterized.expand([
        "organiser",
        "title",
        "details"
    ])
    def test_create_booking_empty_fields(self, field):
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
        self.assertEqual(e.exception.error_list[0].code, "start_too_early")

    #booking too late (after 5pm)
    def test_create_booking_too_late(self):
        booking = self.correct_booking.copy()
        booking["end_time"] = "17:01"
        with self.assertRaises(ValidationError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.error_list[0].code, "end_too_late")

    #booking overlaps with another booking
    #note: correct_booking_2 is 10:00 - 11:00 on 2024-01-02
    @parameterized.expand([
        ("09:00", "10:00", False),
        ("09:00", "10:01", True),
        ("09:00", "11:00", True),
        ("09:00", "11:01", True),
        ("10:00", "11:00", True),
        ("10:00", "11:01", True),
        ("10:30", "12:00", True),
        ("11:00", "12:00", False),
        ("11:01", "12:00", False)
    ])
    def test_2booking_overlap(self, start_time, end_time, expected):
        booking = self.correct_booking_2.copy()
        booking["start_time"] = start_time
        booking["end_time"] = end_time
        self.assertEqual(expected, booking_overlaps(booking))

    # Fields are too long
    @parameterized.expand([
        ("organiser", "a" * 101),
        ("title", "a" * 101),
    ])
    def test_create_booking_field_too_long(self, field, value):
        booking = self.correct_booking.copy()
        booking[field] = value
        with self.assertRaises(ValidationError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.error_list[0].code, f"{field}_too_long")

    # TODO: Mock the datetime module so we can test this properly

    # Booking is in the past
    @parameterized.expand([
        (datetime.timedelta(days=-1)),
        (datetime.timedelta(days=-2)),
        (datetime.timedelta(days=-300)),
    ])
    def test_create_booking_in_past(self, delta):
        booking = self.correct_booking.copy()
        booking["date"] = datetime.datetime.now().date().strftime("%Y-%m-%d")
        # Modify the booking by delta
        booking_time = datetime.datetime.strptime(booking["date"] + " " + booking["start_time"], "%Y-%m-%d %H:%M")
        booking_time += delta
        booking["date"] = booking_time.strftime("%Y-%m-%d")
        booking["start_time"] = booking_time.strftime("%H:%M")
        with self.assertRaises(ValidationError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.error_list[0].code, "booking_in_past")