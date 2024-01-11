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
    service = models.ForeignKey(Service,default=1,on_delete=models.CASCADE,related_name="items")
    name = models.CharField(max_length=500, verbose_name="Name / Nombre")
    detail = models.TextField(verbose_name="Details / Detalles")
    image = models.ImageField(upload_to=si_img, verbose_name="Image / Imagen")
    
    def __str__(self):
        return self.name
    
    def datails(self):
        return mark_safe(self.detail)
    
class AboutUs(models.Model):
    title = models.CharField(verbose_name="Title / Título", max_length=500)
    image = models.ImageField(upload_to=about_us,verbose_name="Image / Imagen")
    read_more = models.CharField(max_length=50,verbose_name="Learn More / Saber más")
    detail = models.TextField(verbose_name="Datails / Detalles")

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
    detail = models.TextField(verbose_name="Datails / Detalles")
    image = models.ImageField(upload_to=track_img, verbose_name="Image / Imagen")
    number_text = models.CharField(max_length=50, verbose_name="Traking Number Text / Texto de Encontrar Carga")
    btn = models.CharField(max_length=250, verbose_name="Track Button / Boton de Encontrar")
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    class Meta:
        verbose_name = 'Track Shiping / Encontrar Carga'
        verbose_name_plural = 'Track Shiping / Encontrar Carga'

class ReviewSection(models.Model):
    title = models.CharField(verbose_name="Title / Título", max_length=500)
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    def __str__(self):
        return "Reviews / Opiniones"
    
    class Meta:
        verbose_name = 'Reviews / Opiniones'
        verbose_name_plural = 'Reviews / Opiniones'
    
class Review(models.Model):
    section = models.ForeignKey(ReviewSection, on_delete=models.CASCADE,default=1,related_name="reviews")
    image = models.ImageField(upload_to=user_img,verbose_name="Image / Imagen")
    name = models.CharField(max_length=500,verbose_name="Name / Nombre")
    review = models.TextField(verbose_name="Review / Opinion")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Review / Opinion'
        verbose_name_plural = 'Reviews / Opiniones'
        
class ContactUs(models.Model):
    map_link = models.CharField(max_length=500,verbose_name="Map Link / Link del Mapa")
    name = models.CharField(max_length=500,verbose_name="Name / Nombre")
    email = models.CharField(max_length=500,verbose_name="Email / Email")
    phone = models.CharField(max_length=12,verbose_name="Phone Number / Número de Teléfono")
    message = models.CharField(max_length=500,verbose_name="Message / Mensaje")
    send_text = models.CharField(max_length=500,verbose_name="Send Text / Texto de Enviar")
    
    class Meta:
        verbose_name = 'Contact Us / Contactenos'
        verbose_name_plural = 'Contact Us / Contactenos'
    
    def get_object():
        return Theme.objects.get(pk=1)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    def __str__(self):
        return "Contact Us / Contactenos"
    
class Footer(models.Model):
    address = models.CharField(max_length=500, verbose_name="Address / Dirección")
    location = models.CharField(max_length=500, verbose_name="Location / Ubicación")
    phone = models.CharField(max_length=15,verbose_name="Phone / Teléfono")
    email = models.EmailField(verbose_name="Email / Email")
    
    facebook = models.CharField(max_length=500,blank=True,null=True)
    twitter = models.CharField(max_length=500,blank=True,null=True)
    linked_in = models.CharField(max_length=500,blank=True,null=True)
    instagram = models.CharField(max_length=500,blank=True,null=True)
    
    title = models.CharField(verbose_name="Title / Título", max_length=500)
    info = models.TextField(verbose_name="Info / Info")

    class Meta:
        verbose_name = 'Footer / Pie de Página'
        verbose_name_plural = 'Footer / Pie de Página'
    
    def get_object():
        return Theme.objects.get(pk=1)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    def __str__(self):
        return "Footer / Pie de Página"
    
class Suscribe(models.Model):
    email = models.CharField(max_length=500,verbose_name="Email / Email")
    texto_submit = models.CharField(max_length=500, verbose_name="Text Suscribe / Text de Suscripcion")
    copyright = models.CharField(max_length=500,verbose_name="Copyright")
    
    class Meta:
        verbose_name = 'Subscribe / Subscripción'
        verbose_name_plural = 'Subscribe / Subscripción'
    
    def get_object():
        return Theme.objects.get(pk=1)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    def __str__(self):
        return "Suscribe / Suscripción"