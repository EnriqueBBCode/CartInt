from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Contacts / Contactos'
        verbose_name_plural = 'Contacts / Contactos'
        
    def __str__(self):
        return self.email