from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Contacts Subscribed / Contactos Subscritos'
        verbose_name_plural = 'Contacts Subscribed / Contactos Subscritos'
        
    def __str__(self):
        return self.email
  
class Manager2Deleted(models.Model):
    email = models.EmailField()
    
# class Manager(models.Model):
#     email = models.EmailField()
    
#     class Meta:
#         verbose_name = 'Managers / Gestores'
#         verbose_name_plural = 'Managers / Gestores'
        
#     def __str__(self):
#         return self.email
    
class Contacting(models.Model):
    name = models.CharField(max_length=300,verbose_name="Name / Nombre")
    email = models.EmailField(verbose_name="Email / Email")
    phone = models.CharField(max_length=12,verbose_name="Phone Number / Número de Teléfono")
    msg = models.TextField(verbose_name="Message / Mensaje")

    
    class Meta:
        verbose_name = 'Contacts / Contactos'
        verbose_name_plural = 'Contacts / Contactos'
        
    def __str__(self):
        return self.name + " " + self.email