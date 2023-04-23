from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core import views

class TestUrls(SimpleTestCase):
    
        def test_index_url_is_resolved(self):
            url = reverse('index')
            self.assertEquals(resolve(url).func, views.index)
    
        def test_book_url_is_resolved(self):
            url = reverse('book')
            self.assertEquals(resolve(url).func, views.book)
        
        