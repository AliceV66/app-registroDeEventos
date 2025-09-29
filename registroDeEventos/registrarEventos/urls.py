from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.crear_evento, name='crear_evento'),
=======
    path('register/', views.register_event, name='register_event'),
>>>>>>> 23f8484 (implementacion del front, preparando para la conexion con back)
]