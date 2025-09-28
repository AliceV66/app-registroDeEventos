from django.contrib import admin
from .models import Evento, Participante

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'ubicacion')

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'evento')

admin.site.register(Evento, EventoAdmin)
admin.site.register(Participante, ParticipanteAdmin)