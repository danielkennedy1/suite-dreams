from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Book(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_book_room(self):
        # user goes to the homepage
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(3)
        self.assertIn('Suite Dreams', self.browser.title)

        # user clicks on the book room button and is taken to the book page
        book_room_button = self.browser.find_element(By.ID, 'bookButton')
        book_room_button.click()
        self.browser.implicitly_wait(3)

        self.assertIn('book', self.browser.current_url)
        self.assertIn('Book | Suite Dreams', self.browser.title)

        # user fills in the form and submits it
        title_input = self.browser.find_element(By.ID, 'title')
        title_input.send_keys('test title')

        details_input = self.browser.find_element(By.ID, 'details')
        details_input.send_keys('test details')

        organiser_input = self.browser.find_element(By.ID, 'organiser')
        organiser_input.send_keys('Selenium')

        date_input = self.browser.find_element(By.ID, 'date')
        date_input.send_keys("2021-05-01")

        stime_input = self.browser.find_element(By.ID, 'start')
        stime_input.send_keys('10:00')

        etime_input = self.browser.find_element(By.ID, 'end')
        etime_input.send_keys('12:00')

        self.browser.execute_script(
            "document.getElementById('room').selectedIndex = 1;")

        submit_button = self.browser.find_element(By.ID, 'submit')
        submit_button.click()
