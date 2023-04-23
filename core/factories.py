import factory
from core.models import Room
# from core.models import Booking

class RoomFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Room
	id = factory.Faker('pyint', min_value=1, max_value=100)
	name = "Room: " + str(factory.Faker('pyint', min_value=1, max_value=20))
	capacity = factory.Faker('pyint', min_value=1, max_value=100) 

class BookingFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = "core.Booking"
	id = factory.Faker('pyint', min_value=1, max_value=100)
	room = factory.SelfAttribute('..room')
	start_time = factory.Faker('time', pattern="%H:%M:%S")
	end_time = factory.Faker('time', pattern="%H:%M:%S")
	date = factory.Faker('date', pattern="%Y-%m-%d")
