from django.urls import path
from pop_system import views

urlpatterns = [
    path("hello/", views.index)
]