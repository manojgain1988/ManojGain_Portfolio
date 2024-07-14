from django.contrib import admin
from IndexApp.models import Slider,About,Service,Portfolio,Client,TeamAbout,ContactMessage,ContactForm


# Register your models here.
admin.site.site_header= ' Admin | Manoj Gain'

class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
    
    
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
       
    
class TeamAboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
    
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
    
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
    
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'create_at']
    
    
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['id','title','address','create_at']
    
    
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','create_at']
    
    
    
admin.site.register(Slider, SliderAdmin )
admin.site.register(About, AboutAdmin )
admin.site.register(TeamAbout, TeamAboutAdmin )
admin.site.register(Service, ServiceAdmin )
admin.site.register(Portfolio, PortfolioAdmin )
admin.site.register(Client, ClientAdmin )
admin.site.register(ContactMessage, ContactMessageAdmin )
admin.site.register(ContactForm, ContactFormAdmin )