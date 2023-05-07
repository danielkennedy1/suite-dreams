from django.urls import path
from . import views


urlpatterns = [
    path("book/", views.book, name="book"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("", views.index, name="index"),
]
