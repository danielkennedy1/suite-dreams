from django.urls import path
from . import views


urlpatterns = [
    path("book/", views.book, name="book"),
    path("", views.index, name="index"),
    path("create_booking", views.create_booking, name="create_booking"),
]