from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# from django.db import models
from Base import models
from Base.models import Contact
from django.conf import settings
# Create your views here.

# def homePage(request):
#     return HttpResponse('Hello World!!!')

def homePage(request):
    return render(request,'home.html')

def contacts(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')
        print(name,email,content,number)
        
        if len(name)>=1 and len(name)<=30:
            pass
        else:
            messages.error(request,'Length of the name should be greater then 2 and less then 30')
            return render(request,'home.html')
        
        if len(email)>1 and len(email)<31:
            pass
        else:
            messages.error(request,'Length of the Email should be greater then 2 and less then 30')
            return render(request,'home.html')
        
        if len(number)>2 and len(number)<13:
            pass
        else:
            messages.error(request,'Length of the Number should be greater then 2 and less then 13')
            return render(request,'home.html')
        
        ins = models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
                
        messages.success(request,'Thanks for contacting us!! Your message has been saved')
        print('Data has been saved')
    
    return render(request,'home.html')

    
