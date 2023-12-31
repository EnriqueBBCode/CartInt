from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Theme)
admin.site.register(Header)
# admin.site.register(Carrousel)
@admin.register(Carrousel)
class CarrouselAdmin(admin.ModelAdmin):
    # resource_class = BookResource
    fieldsets = (
        ("Slide1",{"fields":("title",'sub_title','image','button_link')}),
        ("Slide2",{"fields":("title_1",'sub_title_1','image_1','button_link_1')}),
        ("Slide3",{"fields":("title_2",'sub_title_2','image_2','button_link_2')}),
    )