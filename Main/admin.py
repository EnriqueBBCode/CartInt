from django.contrib import admin
from .models import *
from django.forms.widgets import TextInput
from django import forms

class CarrouselForm(forms.ModelForm):
    class Meta:
        model=Theme
        fields = '__all__'
        widgets={
            'main_color':TextInput(attrs={'type':'color'}),
            'button_colors':TextInput(attrs={'type':'color'})
        }

# admin.site.register(Theme)
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    form = CarrouselForm
admin.site.register(Header)
# admin.site.register(Carrousel)
@admin.register(Carrousel)
class CarrouselAdmin(admin.ModelAdmin):
    # resource_class = BookResource
    fieldsets = (
        ("Carrousel 1",{"fields":("title",'sub_title','image','button_link')}),
        ("Carrousel 2",{"fields":("title_1",'sub_title_1','image_1','button_link_1')}),
        ("Carrousel 3",{"fields":("title_2",'sub_title_2','image_2','button_link_2')}),
    )