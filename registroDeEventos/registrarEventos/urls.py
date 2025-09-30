from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_evento, name='crear_evento'),]
