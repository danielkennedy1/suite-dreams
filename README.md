# Suite Dreams

A software testing project using the medium of an on-site Room Booking System that facilitates business-hours booking of multiple rooms and management of those bookings.

![Coverage](coverage.svg)
[![Coverage](https://github.com/danielkennedy1/suite-dreams/actions/workflows/coverage.yml/badge.svg?branch=main)](https://github.com/danielkennedy1/suite-dreams/actions/workflows/coverage.yml)
[![DevSkim](https://github.com/danielkennedy1/suite-dreams/actions/workflows/devskim.yml/badge.svg)](https://github.com/danielkennedy1/suite-dreams/actions/workflows/devskim.yml)
[![Django CI](https://github.com/danielkennedy1/suite-dreams/actions/workflows/django.yml/badge.svg)](https://github.com/danielkennedy1/suite-dreams/actions/workflows/django.yml)


## Authors

- [Daniel Kennedy](https://www.github.com/danielkennedy1)
- [Adam Byrne](https://www.github.com/theadambyrne)


## Features

- View bookings
- Add bookings
- Delete bookings


## Tech Stack

**Client:** TailwindCSS

**Server:** Django



## Installation

How to get up and running locally

```bash
  git clone https://github.com/danielkennedy1/suite-dreams.git
  cd suite-dreams
  
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
```
    
## Run 

```bash
    python manage.py runserver
```

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

## Tests

Our test suite uses Django's own test library, with fixtures including a Test DB, Client, setUp() in TestCases, and the runner itself

**Test Suite**
core.tests.cases.Cases contains the parameters for the parameterized test cases for both the unit and integration tests.

**Positive testing**
- Url resolution
- Normal HTTP GET request responses
- Normal HTTP POST responses & DB effects
- create_booking with correct input

**Unit tests**
- Booking Creation: business hours, input validation, made for future (mocked datetime.now())
- Booking Deletion: exists
- Model functionality & factories, associations in DB

**Integration tests**
- Booking Creation: overlap, End-to-end exception handling, incorrect room, 
- Coherence between error_code in backend and error_message in frontend using global test suite
- Nonexistent booking deletion failure