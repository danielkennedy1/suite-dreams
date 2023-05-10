from django.test import TestCase
from parameterized import parameterized
from core.models import Room, Booking
from core.tests.cases import Cases

cases = Cases()
validation_test_cases = cases.validation_test_cases


class ValidGetRequestTestCase(TestCase):
    @parameterized.expand([
        ('/', 'index.html'),
        ('/book/', 'book.html'),
    ])
    def test_get_request(self, url, template):
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)


class InvalidGetRequestTestCase(TestCase):
    def test_invalid_get_request(self):
        response = self.client.get('/invalid/')

        self.assertEqual(response.status_code, 404)


class ValidPostRequestTestCase(TestCase):

    def setUp(self):
        Room.objects.create(id=1, name="Test Room", capacity=1)

    def test_create_valid_booking(self):
        response = self.client.post('/book/', {
            'organiser': 'Test',
            'date': '2024-01-03',
            'start_time': '10:00',
            'end_time': '11:00',
            'room_id': '1',
            'title': 'Test',
            'details': 'Test'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTrue(Booking.objects.filter(id=1).exists())

    def test_delete_valid_booking(self):
        # Create a booking to delete
        Booking.objects.create(
            id=300,
            room_id=1,
            organiser="Test",
            title="Test",
            details="Test",
            start_time="10:00",
            end_time="11:00",
            date="2024-01-04"
        )
        self.assertTrue(Booking.objects.filter(id=300).exists())

        response = self.client.post('/delete/300')
        self.assertRedirects(response, '/')

        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(id=300)


class InvalidPostRequestTestCase(TestCase):
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

    # Delete a booking that doesn't exist
    def test_delete_nonexistent_booking(self):
        self.assertFalse(Booking.objects.filter(id=100).exists())

        response = self.client.post('/delete/100')

        # Should redirect to index with a 404
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 404)

    # Create a booking with invalid parameters
    @parameterized.expand(validation_test_cases)
    def test_create_invalid_booking(self, fields, values, error_code, error_message):
        booking_request = self.correct_booking.copy()

        for field, value in zip(fields, values):
            booking_request[field] = value

        response = self.client.post('/book/', booking_request)

        self.assertTemplateUsed(response, 'book.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, error_message)
