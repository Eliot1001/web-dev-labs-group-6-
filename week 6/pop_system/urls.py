from django.urls import path
from pop_system import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proposals/", views.proposal_list, name="proposal_list"),
]