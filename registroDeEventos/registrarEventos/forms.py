from django import forms
<<<<<<< HEAD
from .models import Evento, Participante
import datetime

class EventoForm(forms.ModelForm):
    
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    # Validación para que la fecha del evento sea futura.
    def clean_fecha(self): 
        fecha = self.cleaned_data.get('fecha')

        if fecha and fecha < datetime.date.today():
            raise forms.ValidationError("La creación del evento debe considerar una fecha futura.")
        return fecha

    # Validación para que la combinación fecha y evento sea única.
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        fecha = cleaned_data.get("fecha")

        if nombre and fecha:
            if Evento.objects.filter(nombre=nombre, fecha=fecha).exists():
                raise forms.ValidationError(
                    "Ya existe un evento con este nombre en la misma fecha."
                )
        
        return cleaned_data 

class ParticipanteForm(forms.ModelForm):
    
    class Meta:
        model = Participante
        fields = ['nombre', 'correo']
=======
from django.forms import formset_factory

class EventForm(forms.Form):
    name = forms.CharField(max_length=100, label='Event Name')
    date = forms.DateTimeField(label='Event Date')
    location = forms.CharField(max_length=255, label='Location')
    description = forms.CharField(widget=forms.Textarea, label='Description')

class ParticipantForm(forms.Form):
    name = forms.CharField(max_length=100, label='Participant Name')
    email = forms.EmailField(label='Email')

ParticipantFormSet = formset_factory(ParticipantForm, extra=1)
>>>>>>> 23f8484 (implementacion del front, preparando para la conexion con back)
