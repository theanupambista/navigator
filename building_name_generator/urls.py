from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("generated-hash/", views.generateHash),
    path("view_map/", views.view_map),
    # urls for making multi dependent dropdown
    path('get_districts/', views.get_districts, name='get_districts'),
    path('get_municipalites/', views.get_municipalites, name='get_municipalites'),
]
