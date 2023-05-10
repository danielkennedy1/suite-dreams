# Suite Dreams

A software testing project using the medium of an on-site Room Booking System that facilitates business-hours booking of multiple rooms and management of those bookings.

We used TailwindCSS to style the frontend and took a full-stack approach with Django and its inbuilt sqllite functionality.

<br/>

![Coverage](coverage.svg)
![Dependabot](https://badgen.net/github/dependabot/ubuntu/yaru)
[![DevSkim](https://github.com/danielkennedy1/suite-dreams/actions/workflows/devskim.yml/badge.svg)](https://github.com/danielkennedy1/suite-dreams/actions/workflows/devskim.yml)
[![Django CI](https://github.com/danielkennedy1/suite-dreams/actions/workflows/django.yml/badge.svg)](https://github.com/danielkennedy1/suite-dreams/actions/workflows/django.yml)

<br/>

## Authors

- [Daniel Kennedy](https://www.github.com/danielkennedy1)
- [Adam Byrne](https://www.github.com/theadambyrne)

<br/>

## Features

- View bookings
- Add bookings
- Delete bookings

<br/>


## Installation

How to get up and running locally

```bash
  git clone https://github.com/danielkennedy1/suite-dreams.git
  cd suite-dreams
  
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
```
    
<br/>

## Run 

```bash
    python manage.py runserver
```

<br/>

##  Tests

To run tests, run the following command

```bash
  python manage.py test
```

Our test suite uses Django's own test library (extension of ```unittest```), with fixtures including a Test DB, Client, setUp() in TestCases, and the runner itself

<br/>

**Test Suite**
```core.tests.cases.Cases``` contains the parameters for the parameterized test cases for both the unit and integration tests.

<br/>

**Positive testing**
- Url resolution
- Normal HTTP GET request responses
- Normal HTTP POST responses & DB effects
- ```create_booking``` with correct input

<br/>

**Unit tests**
- Booking Creation: business hours, input validation, made for future (mocked ```datetime.now()```)
- Booking Deletion: exists
- Model functionality & factories, associations in DB

<br/>

**Integration tests**
- Booking Creation: overlap, End-to-end exception handling, incorrect room, 
- Coherence between ```error_code``` in backend and ```error_message``` in frontend using global test suite
- Nonexistent booking deletion failure

<br/>

## Contribution (approximate breakdown)
Daniel Kennedy and Adam Byrne declare this work as their own. All third-party code is listed as a dependency in ```requirements.txt```, and all third-party code is used in accordance with the license of the respective package. 

<br/>

### Daniel Kennedy ~ 60%
---
- Unit and Integration tests (models, validation of exception handling, overlaps)
- Positive testing (Create and Read)
- Dependency testing (dependabot)
- Controllers (Create)
- Views
- Models


<br/>

### Adam Byrne ~ 40%
---
- Unit and Integration tests (validation of exception handling)
- Positive testing (Delete, urls)
- Dependency testing (dependabot, devskim)
- Controllers (Read, Delete)
- Views
- Frontend
- CI/CD Build, Test & test metrics
