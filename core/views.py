from django.shortcuts import render


from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())



def regestr(request):
    template = loader.get_template('regestr.html')
    return HttpResponse(template.render())


