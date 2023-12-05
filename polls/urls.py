from django.urls import path
# from this directory (the polls app) import views
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
