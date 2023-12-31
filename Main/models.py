from django.db import models

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
    main_color = models.CharField(max_length=30)
    button_colors = models.CharField(max_length=30)
    
    def __str__(self):
        return self.main_color
    
class Header(models.Model):
    title = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Carrousel(models.Model):
    title = models.CharField(max_length=500)
    sub_title = models.TextField()
    image = models.ImageField(upload_to=carrousel_img)
    button_link = models.CharField(max_length=500)
    
    title_1 = models.CharField(max_length=500)
    sub_title_1 = models.TextField()
    image_1 = models.ImageField(upload_to=carrousel_img)
    button_link_1 = models.CharField(max_length=500)
    
    title_2 = models.CharField(max_length=500)
    sub_title_2 = models.TextField()
    image_2 = models.ImageField(upload_to=carrousel_img)
    button_link_2 = models.CharField(max_length=500)

class Service(models.Model):
    title = models.CharField(max_length=500)
    sub_title = models.TextField()
    
class Services_Item(models.Model):
    name = models.CharField(max_length=500)
    detail = models.TextField()
    image = models.ImageField(upload_to=si_img)
    
class AboutUs(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to=about_us)
    
class Track(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to=track_img)
    
class Our_clients(models.Model):
    title = models.CharField(max_length=500)

class Our_clients_items(models.Model):
    image = models.ImageField(upload_to=user_img)
    name = models.CharField(max_length=500)
    review = models.TextField()
    
class ContactUs(models.Model):
    map_link = models.CharField(max_length=500)
    
class Footer(models.Model):
    info = models.TextField()
    info_details = models.TextField()
    facebook = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    i_n = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    copyright = models.CharField(max_length=500)
    