#from django.shortcuts import render
#from django.http import httpResponse
from django.views.generic import TemplateView

# Create your views here.
'''
def view_home(request):
    return httpResponse('pag')

def view_about(request):
    return httpResponse('about')

def view_contact(request):
    return httpResponse('contact')
    
def view_home(requets):
    return render (request, 'home.html')
    '''

class HomeView(TemplateView):
    template_name = "base/home.html"