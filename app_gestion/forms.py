from django import forms
from .models import Contacto, Obituario, DetalleObituario, Condolencia


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'tipoconsulta', 'mensaje', 'avisos']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'avisos': forms.CheckboxInput(),
        }
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono (opcional)',
            'tipoconsulta': 'Tipo de Consulta',
            'mensaje': 'Mensaje',
            'avisos': 'Deseo recibir avisos',
        }


class ObituarioForm(forms.ModelForm):
    class Meta:
        model = Obituario
        fields = ['nombre', 'fecha_fallecimiento', 'mensaje', 'imagen']


class DetalleObituarioForm(forms.ModelForm):
    class Meta:
        model = DetalleObituario
        fields = ['lugar_exequias', 'fecha_exequias','lugar_velatorio', 'destino_final', 'invitaciones']


class CondolenciaForm(forms.ModelForm):
    class Meta:
        model = Condolencia
        fields = ['nombre_remitente','email_remitente','telefono_remitente','mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 3}),
        }
