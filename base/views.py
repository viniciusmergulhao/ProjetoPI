from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
'''
def view_home(request):
    return httpResponse('pag')

def view_about(request):
    return httpResponse('about')
'''




'''def view_home(request):
    return render (request, 'home.html')'''
  
def view_base(request):
    return render (request, 'base.html')


class HomeView(TemplateView):
     template_name = 'home.html'
