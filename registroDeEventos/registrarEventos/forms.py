from django import forms
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

class ParticipanteForm(forms.ModelForm):
    
    class Meta:
        model = Participante
        fields = ['nombre', 'correo']