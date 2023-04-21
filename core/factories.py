import factory
from core.models import Room

class RoomFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Room

	name = "Room: " + str(factory.Faker('pyint', min_value=1, max_value=20))
	capacity = factory.Faker('pyint', min_value=1, max_value=100) 
