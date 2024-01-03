from django.forms.widgets import TextInput
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class CarrouselForm(forms.ModelForm):
    class Meta:
        model=Carrousel
        fields = '__all__'
        widgets={
            'main_color':TextInput(attrs={'type':'color'}),
            'button_colors':TextInput(attrs={'type':'color'})
        }
        
class ServiceForm(forms.ModelForm):
    title = forms.CharField(label='Title / Titulo',widget=forms.TextInput(attrs={'placeholder':'Title / Título','maxlength':'500'}))
    sub_title = forms.CharField(label='Subtitle / Subtítulo',widget=forms.Textarea(attrs={'placeholder':'Subtitle / Subtítulo'}))
    
    class Meta:
        model=Service
        fields = ['title','sub_title']
        
class ServiceItemForm(forms.ModelForm):
    name = forms.CharField(label='Name / Nombre',widget=forms.TextInput(attrs={'placeholder':'Name / Nombre','maxlength':'500'}))
    detail = forms.CharField(label='Details / Details',widget=CKEditorWidget())
    image = forms.ImageField(label='Icon / Icono')
    
    class Meta:
        model=Services_Item
        fields = '__all__'
        
class ContactUsForm(forms.ModelForm):
    map_link = forms.CharField(label='Map Link / Link del Mapa',widget=forms.TextInput(attrs={'placeholder':'Map Link / Link del Mapa','maxlength':'500'}))
    name = forms.CharField(label='Name / Nombre',widget=forms.TextInput(attrs={'placeholder':'Name / Nombre','maxlength':'500'}))
    email = forms.CharField(label='Email / Correo',widget=forms.TextInput(attrs={'placeholder':'Email / Correo','maxlength':'500'}))
    message = forms.CharField(label='Message / Mensaje',widget=forms.Textarea(attrs={'placeholder':'Message / Mensaje'}))
    send_text = forms.CharField(label='Send Text / Texto de Enviar',widget=forms.TextInput(attrs={'placeholder':'Send Text / Texto de Enviar','maxlength':'500'}))
    
    class Meta:
        model=ContactUs
        fields = '__all__'