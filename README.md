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

**Unit tests**
- Creation: overlap, business hours, valid inputs
- Deletion: exists


```bash
  python manage.py test
```
