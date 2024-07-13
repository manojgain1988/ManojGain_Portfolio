from django.contrib import admin
from IndexApp.models import ContactForm


# Register your models here.
admin.site.site_header= ' Admin | Manoj Gain'

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','create_at']
    
admin.site.register(ContactForm, ContactFormAdmin )