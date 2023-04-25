from django.test import TestCase

class DoubleBooking(TestCase):
    def setUp(self) -> None:
        self.client.post('/book', data={
			'organiser': 'John',
			'title': 'Meeting',
			'details': 'Discuss the project',
			'date': '2021-01-01',
			'start_time': '09:00',
			'end_time': '10:00',
			'room': 1
		})
        
    def test_double_booking(self):
        res = self.client.post('/book', data={
            'organiser': 'John 2',
            'title': 'Meeting 2',
            'details': 'Discuss the project 2',
            'date': '2021-01-01',
            'start_time': '09:00',
            'end_time': '10:00',  
		})
        self.assertEqual(res.status_code, 301)
        
class PastBooking(TestCase):       
    def test_past_booking(self):
        res = self.client.post('/book', data={
                      'organiser': 'John',
                      'title': 'Meeting',
                        'title': 'Meeting',
                        'details': 'Discuss the project',
                        'date': '2001-01-01',
                        'start_time': '09:00',
                        'end_time': '10:00',
                        'room': 3
                        })
        
        self.assertEqual(res.status_code, 301)
            
                

      