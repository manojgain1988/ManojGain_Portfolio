from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    subject = models.CharField(max_length=400, blank=True)
    message = models.CharField(max_length=700, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    