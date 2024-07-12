from django.contrib import admin
from IndexApp.models import ContactForm


# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','create_at']
    
admin.site.register(ContactForm, ContactFormAdmin )