from django.shortcuts import render

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

def Pricing(request):
    context={  
    }
    return render(request,'pricing.html', context)

def Blog(request):
    context={  
    }
    return render(request,'blog.html', context)

def Testimonial(request):
    context={  
    }
    return render(request,'testimonial.html', context)

def Contact(request):
    context={  
    }
    return render(request,'contact.html', context)