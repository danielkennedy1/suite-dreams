from django.test import TestCase

# No bookings => empty table with message "No bookings"
class EmptyTable(TestCase):
	def setUp(self):
		self.client.get('/', data=None)

	def test_empty_table(self):
		self.assertContains(self.client.get('/'), 'No bookings')