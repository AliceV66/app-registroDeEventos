from django.contrib import admin
from .models import Evento, Participante

class ParticipanteInline(admin.TabularInline):
    model = Participante
    extra = 1

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'ubicacion')
    inlines = [ParticipanteInline]

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'evento')


admin.site.register(Evento, EventoAdmin)
admin.site.register(Participante, ParticipanteAdmin)