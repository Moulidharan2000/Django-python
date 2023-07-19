from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("create_question/", views.create_question, name="create"),
    path("retrieve_question/", views.retrieve_question, name="retrieve"),
    path("update_question/", views.update_question, name="update"),
    path("delete_question/", views.delete_question, name="delete"),
    path("create_choice/", views.create_choice, name="create_c"),
    path("retrieve_choice/", views.retrieve_choice, name="retrieve_c"),
    path("update_choice/", views.update_choice, name="update_c"),
    path("delete_choice/", views.delete_choice, name="delete_c"),
]
