from django.test import TestCase
from core.lib import create_booking, booking_overlaps, delete_booking
from core.models import Room, Booking
from django.core.exceptions import ValidationError
from parameterized import parameterized
from core.tests.cases import Cases
from freezegun import freeze_time


# Global set up as paramaterized tests are expanded before setUp is called
cases = Cases()
validation_test_cases = cases.validation_test_cases


class CreateBookingTestCase(TestCase):

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
        Booking.objects.create(
            id=1,
            room_id=1,
            organiser="Test",
            title="Test",
            details="Test",
            start_time="10:00",
            end_time="11:00",
            date="2024-01-01"
        )

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    # Create a booking with correct parameters, on the next day
    def test_booking_correct(self):
        booking = self.correct_booking.copy()
        booking["date"] = "2024-01-02"
        create_booking(booking)
        self.assertTrue(True)

    # Book a room that doesn't exist
    def test_create_booking_invalid_room(self):
        booking = self.correct_booking.copy()
        booking["room_id"] = 100
        with self.assertRaises(Room.DoesNotExist):
            create_booking(booking)

    # Booking parameter validation tests

    @parameterized.expand(validation_test_cases)
    def test_booking_validation(self, fields, values, expected_code, error_message):
        booking = self.correct_booking.copy()
        for field, value in zip(fields, values):
            booking[field] = value
        with self.assertRaises(ValidationError) as e:
            create_booking(booking)
        self.assertEqual(e.exception.error_list[0].code, expected_code)

    # invalid time

    def test_create_booking_invalid_time(self):
        booking = self.correct_booking.copy()
        booking["start_time"] = "25:00"
        with self.assertRaises(ValueError) as e:
            create_booking(booking)
        self.assertEqual(
            e.exception.args[0], "time data '25:00' does not match format '%H:%M'")

    # booking overlaps with another booking
    # note: correct_booking is 10:00 - 11:00 on 2024-01-01 in Test Room
    @ parameterized.expand([
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
    def test_booking_overlap(self, start_time, end_time, expected):
        booking = self.correct_booking.copy()
        booking["start_time"] = start_time
        booking["end_time"] = end_time
        self.assertEqual(expected, booking_overlaps(booking))


class TestDeleteBooking(TestCase):
    def setUp(self):
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

    def test_delete_booking(self):
        delete_booking(1)
        self.assertTrue(True)

    def test_delete_booking_invalid_id(self):
        with self.assertRaises(ValidationError) as e:
            delete_booking(100)
        self.assertEqual(e.exception.code, "booking_does_not_exist")
