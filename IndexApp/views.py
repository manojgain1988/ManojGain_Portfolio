from django.shortcuts import render,redirect
from IndexApp.models import ContactForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
 
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


def Profile(request):
    context={  
    }
    return render(request,'profile.html', context)

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


def AuthRegister(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exists !')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exists !')
            
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request, 'Your Register Successfully!')
                return redirect('login')
        else:
            messages.error(request, 'Your Passpord or Comfirm_Password  are not Same!')         
    return render(request,'register.html')




def AuthLogin(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        
        user=authenticate(request, username=name, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,' Your Login Successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Your Email or Password  are not Match!')
            return redirect('login')
    return render(request,'login.html')
 



def Forgotpassword(request):
    return render(request,'forgot.html')


def UserLogout(request):
   logout(request)
   messages.success(request,'Successfully Logout !')
   return redirect('login')
