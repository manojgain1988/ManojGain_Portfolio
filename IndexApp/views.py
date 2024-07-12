from django.shortcuts import render
from IndexApp.models import ContactForm
# Create your views here.

def Index(request):
    context={  
    }
    return render(request,'index.html', context)

def About(request):
    context={  
    }
    return render(request,'about.html', context)

def Services(request):
    context={  
    }
    return render(request,'services.html', context)

def Team(request):
    context={  
    }
    return render(request,'team.html', context)

def Portfolio(request):
    context={  
    }
    return render(request,'portfolio.html', context)


def Testimonial(request):
    context={  
    }
    return render(request,'testimonial.html', context)

def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        obj=ContactForm(name=name,email=email,subject=subject,message=message)
        obj.save()
        
    context={  
    }
    return render(request,'contact.html', context)



def Login(request):
    context={  
    }
    return render(request,'login.html', context)

def Register(request):
    context={  
    }
    return render(request,'register.html', context)
