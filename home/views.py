from django.shortcuts import render
from home.models import Contact, Blogpost, portfolio
# Create your views here.
from datetime import datetime


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    lis = Blogpost.objects.all()
    return render(request,"blog.html",{'lis':lis})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("fname")
        email = request.POST.get("email")
        phone = request.POST.get("number")
        time = request.POST.get('datetime')
        file = request.POST.get("file")
        service = request.POST.get('Services')
        budget = request.POST.get("budget")
        message = request.POST.get('message')
        
      
        
        contact = Contact(fname=name, email= email, phone= phone, time= time,message=message,service=service,budget=budget )
        contact.save()
        
        return render(request,"contact.html")
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")

def blog_singal(request):
    lis = Blogpost.objects.all()

    return render(request,"blog-single.html", {'lis':lis})


