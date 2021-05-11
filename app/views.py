from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def aboutus(request):
    return render(request, 'home.html',{'title': 'Page Title', 'color': 'green'})

def contactus(request):
    return render(request, 'contact.html', {'pagename': 'Contact Us Page', 'color': 'blue'})

def add(request):
    value1 = int(request.POST['value1'])
    value2 = int(request.POST['value2'])
    return render(request, 'add.html',{'total': value1+value2, 'color': 'yellow'})

def travel(request):
    return render(request, 'index.html')