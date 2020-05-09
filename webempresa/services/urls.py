from django.urls import path
from . import views

urlpatterns = [
    #Pats de core
    path('', views.services, name="services"),
]
