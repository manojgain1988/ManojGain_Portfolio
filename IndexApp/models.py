from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to='slider/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
class About(models.Model):
    image = models.ImageField(upload_to='about/', blank=True)
    title = models.CharField(max_length=700, blank=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class TeamAbout(models.Model):
    image = models.ImageField(upload_to='teamAbout/', blank=True)
    title = models.CharField(max_length=700, blank=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Service(models.Model):
    icon = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=700, blank=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/', blank=True)
    title = models.CharField(max_length=700, blank=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Client(models.Model):
    name = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='client/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    subject = models.CharField(max_length=400, blank=True)
    message = models.CharField(max_length=700, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class ContactMessage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    road = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=400, blank=True)
    icon = models.CharField(max_length=100, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    