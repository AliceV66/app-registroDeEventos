from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.db import transaction
from django.contrib import messages
from .forms import EventoForm, ParticipanteForm
from .models import Evento, Participante



# Se crea el conjunto de formularios de Participantes vinculados al Evento.
def crear_evento(request):
    ParticipanteFormSet = inlineformset_factory(
        Evento,
        Participante,
        form=ParticipanteForm,
        extra=3,
        can_delete=False
    )

    # El usuario envía datos (método POST).
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        participante_formset = ParticipanteFormSet(request.POST)

        # Validación que tanto el evento como los participantes sean correctos.
        if evento_form.is_valid() and participante_formset.is_valid():
            with transaction.atomic(): # Asegura que todo se guarde correctamente o en caso contrario no se guarde nada.
                evento = evento_form.save() # Se guarda el evento.

                # Se preparan los partcipantes, pero aún no se guardan en la Base de Datos.
                participantes = participante_formset.save(commit=False)
                for participante in participantes:
                    participante.evento = evento # Se asigna el evento recién creado a cada participante.
                    participante.save() # Se guarda el participante en la Base de Datos.

            messages.success(request, '¡Evento Registrado con ÉXITO!')
            return redirect('crear_evento') # Se redirige para limpiar el formulario y evitar reenvíos.

    # El usuario visita la página (método GET).
    else:
        # Se muestran los formularios vacíos.
        evento_form = EventoForm()
        participante_formset = ParticipanteFormSet()

    # Se preparan los datos que se enviarán a la plantilla HTML.
    context = {
        'evento_form': evento_form,
        'participante_formset': participante_formset,
    }

    # Se rendereiza el HTML con los formularios.
    return render(request, 'registrarEventos/crear_evento.html', context)

