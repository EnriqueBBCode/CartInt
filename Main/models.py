from django.db import models
from django.utils.safestring import mark_safe

def carrousel_img(instance,filename):
    return f"carrousel/{filename}"

def si_img(instance,filename):
    return f"services_items/{filename}"

def about_us(instance,filename):
    return f"about_us/{filename}"
    
def track_img(instance,filename):
    return f"track_img/{filename}"

def user_img(instance,filename):
    return f"user_img/{filename}"

class Theme(models.Model):
    main_color = models.CharField(max_length=30,verbose_name="Main Color / Color Principal")
    button_colors = models.CharField(max_length=30,verbose_name="Button Colors / Colores de los Botones")
    
    def __str__(self):
        return mark_safe(f"<b style='text-transform:uppercase;font-weight:700;color:{self.main_color}'>Main Color / Color Principal</b> | <b style='text-transform:uppercase;font-weight:700;color:{self.button_colors}'>Main Color / Color Principal</b>")
    
    def get_object():
        # Intenta obtener la única instancia
        instance, created = Theme.objects.get_or_create(pk=1)
        return instance

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    class Meta:
        verbose_name = 'Theme / Tema'
        verbose_name_plural = 'Theme / Tema'
            
class Header(models.Model):
    title = models.CharField(verbose_name="Title/Título", max_length=200)
    phone = models.CharField(max_length=12,verbose_name="Phone / Teléfono")
    email = models.EmailField(verbose_name="Email")
    location = models.CharField(max_length=200, verbose_name="Location / Ubicación")
    
    def __str__(self):
        return "Header / Encabezado"
    
    def get_object():
        # Intenta obtener la única instancia
        instance, created = Theme.objects.get_or_create(pk=1)
        return instance

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    class Meta:
        verbose_name = 'Header / Encabezado'
        verbose_name_plural = 'Header / Encabezado'
    
class Carrousel(models.Model):
    title = models.CharField(verbose_name="Title / Título", max_length=500)
    sub_title = models.TextField(verbose_name="Subtitle / Subtítulo")
    image = models.ImageField(upload_to=carrousel_img, verbose_name="Image / Imágen")
    button_link = models.CharField(max_length=500, verbose_name="Button Link / Enlace del Botón")
    
    title_1 = models.CharField(max_length=500,verbose_name="Title / Título")
    sub_title_1 = models.TextField(verbose_name="Subtitle / Subtítulo")
    image_1 = models.ImageField(upload_to=carrousel_img, verbose_name="Image / Imágen")
    button_link_1 = models.CharField(max_length=500, verbose_name="Button Link / Enlace del Botón")
    
    title_2 = models.CharField(max_length=500,verbose_name="Title / Título")
    sub_title_2 = models.TextField(verbose_name="Subtitle / Subtítulo")
    image_2 = models.ImageField(upload_to=carrousel_img, verbose_name="Image / Imágen")
    button_link_2 = models.CharField(max_length=500, verbose_name="Button Link / Enlace del Botón")

    def __str__(self):
        return "Carrousel / Carrusel"

    def get_object():
        # Intenta obtener la única instancia
        instance, created = Theme.objects.get_or_create(pk=1)
        return instance

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    class Meta:
        verbose_name = 'Carrousel / Carrusel'
        verbose_name_plural = 'Carrousel / Carrusel'

class Service(models.Model):
    title = models.CharField(verbose_name="Title / Título", max_length=500)
    sub_title = models.TextField(verbose_name="Subtitle / Subtítulo")
    
    def get_object():
        return Theme.objects.get(pk=1)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Service / Servicio'
        verbose_name_plural = 'Services / Servicios'
    
class Services_Item(models.Model):
    service = models.ForeignKey(Service,default=1,on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Name / Nombre")
    detail = models.TextField(verbose_name="Details / Detalles")
    image = models.ImageField(upload_to=si_img, verbose_name="Image / Imagen")
    
    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    title = models.CharField(verbose_name="Title / Título", max_length=500)
    image = models.ImageField(upload_to=about_us,verbose_name="Image / Imagen")
    read_more = models.TextField(verbose_name="Learn More / Saber más")

    def get_object():
        return Theme.objects.get(pk=1)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'About Us / Acerca de Nosotros'
        verbose_name_plural = 'About Us / Acerca de Nosotros'
        
class Track(models.Model):
    title = models.CharField(verbose_name="Title / Título", max_length=500)
    image = models.ImageField(upload_to=track_img, verbose_name="Image / Imagen")
    number_text = models.CharField(max_length=250, verbose_name="Traking Number Text / Texto de Encontrar Carga")
    btn = models.CharField(max_length=250, verbose_name="Track Button / Boton de Encontrar")
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    class Meta:
        verbose_name = 'Track Shiping / Encontrar Carga'
        verbose_name_plural = 'Track Shiping / Encontrar Carga'

# class Our_clients(models.Model):
#     title = models.CharField(verbose_name="Title/Título", max_length=500)

# class Our_clients_items(models.Model):
#     image = models.ImageField(upload_to=user_img)
#     name = models.CharField(max_length=500)
#     review = models.TextField()
    
# class ContactUs(models.Model):
#     map_link = models.CharField(max_length=500)
    
# class Footer(models.Model):
#     info = models.TextField()
#     info_details = models.TextField()
#     facebook = models.CharField(max_length=500)
#     twitter = models.CharField(max_length=500)
#     i_n = models.CharField(max_length=500)
#     instagram = models.CharField(max_length=500)
#     copyright = models.CharField(max_length=500)
    