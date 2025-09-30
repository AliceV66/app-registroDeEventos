from django.db import models



class Evento(models.Model):
    nombre = models.CharField(max_length=100) # Respetando la restricción de que 'nombre' contanga como máximo 100 caracteres.
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Participante(models.Model):
    
    evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)  # Foreign Key que conecta a cada participante con su respectivo evento.
                                                                                                # on_deleted=models.CASCADE; Si un evento es borrado, se borran todos sus participantes
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.correo})"