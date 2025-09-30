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
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del participante'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
        }
