from django.contrib import admin
from .models import *
from .forms import *

# admin.site.register(Theme)
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    form = CarrouselForm
admin.site.register(Header)
# admin.site.register(Carrousel)
@admin.register(Carrousel)
class CarrouselAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Carrousel 1",{"fields":("title",'sub_title','image','button_link')}),
        ("Carrousel 2",{"fields":("title_1",'sub_title_1','image_1','button_link_1')}),
        ("Carrousel 3",{"fields":("title_2",'sub_title_2','image_2','button_link_2')}),
    )

class Service_Item_Inline(admin.StackedInline):  # O admin.StackedInline
    form = ServiceItemForm
    model = Services_Item
    extra = 0
    verbose_name = "Service / Servicio"
    verbose_name_plural = "Services / Servicios"
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
        
    inlines = [Service_Item_Inline]
    fieldsets = (
        ("Info",{"fields":("title",'sub_title')}),
    )
    
admin.site.register(AboutUs)
admin.site.register(Track)

class RevireInlines(admin.StackedInline):  # O admin.StackedInline
    model = Review
    extra = 0
    verbose_name = "Review / Opinion"
    verbose_name_plural = "Reviews / Opiniones"

@admin.register(ReviewSection)
class ReviewSectionAdmin(admin.ModelAdmin):
    inlines = [RevireInlines]
    fieldsets = (
        ("Title / Título",{"fields":("title",)}),
    )

admin.site.register(ContactUs)
admin.site.register(Footer)
admin.site.register(Suscribe)
admin.site.register(Shiping)

# class ContactUsAdmin(admin.ModelAdmin):
#     form = ContactUsForm

"""
https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d117459.10941738653!2d-82.3656448!3d23.0752256!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1ses-419!2scu!4v1705264250760!5m2!1ses-419!2scu
luismiguel@godjango.dev
lmdelbahia@gmail.com
"""