from django.forms.widgets import TextInput
from django import forms
from .models import Theme, Service, Services_Item
from ckeditor.widgets import CKEditorWidget

class CarrouselForm(forms.ModelForm):
    class Meta:
        model=Theme
        fields = '__all__'
        widgets={
            'main_color':TextInput(attrs={'type':'color'}),
            'button_colors':TextInput(attrs={'type':'color'})
        }
        
class ServiceForm(forms.ModelForm):
    title = forms.CharField(label='Title / Titulo',widget=forms.TextInput(attrs={'placeholder':'Title / Título','maxlength':'500'}))
    sub_title = forms.CharField(label='Subtitle / Subtítulo',widget=forms.Textarea(attrs={'placeholder':'Subtitle / Subtítulo','maxlength':'500'}))
    
    class Meta:
        model=Service
        fields = ['title','sub_title']
        
class ServiceItemForm(forms.ModelForm):
    name = forms.CharField(required=False,label='Name / Nombre',widget=forms.TextInput(attrs={'placeholder':'Title / Título','maxlength':'500'}))
    detail = forms.CharField(required=False,label='Details / Details',widget=CKEditorWidget())
    image = forms.ImageField(required=False,label='Select image / Seleccionar una imagen')
    
    class Meta:
        model=Services_Item
        fields = '__all__'