from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    mail = forms.EmailField()
    mensaje = forms.CharField()

