from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from . import models
def index(req):
    return render(req,"bapp/index.html")
def home(req):
    return render(req,"bapp/home.html")

def Blog(req):
    return render(req,"bapp/Blog.html")

def contact(req):
    if req.method=="POST":
        try:
            n=req.POST.get('name')
            e=req.POST.get('email')
            p=req.POST.get('phone')
            c=req.POST.get('cname')
            models.Contact(name=n,email=e,phone=p,comname=c).save()
            msg=" User Registered !"
            if True:
                send_mail(
                    '<Subject>User {} has been Registered'.format(n),
                    '<Body>A new user has been created',
                    'e',
                    ['renuchauhan0110@gmail.com'],
                    fail_silently=False,
                )
            return render(req,'bapp/thank.html',{'msg':msg})
        except Exception as e:

            return render(req,'bapp/contact.html',{"msg":e})


    return render(req,"bapp/contact.html")

def Services(req):
    return render(req,"bapp/Services.html")

def SocialMedia(req):
    return render(req,"bapp/SocialMedia.html")

def AboutUS(req):
    return render(req,"bapp/AboutUS.html")

