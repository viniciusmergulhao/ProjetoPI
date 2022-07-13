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
  

class HomeView(TemplateView):
     template_name = 'home.html'

class CadView(TemplateView):
    template_name = 'cadastro.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class PerfilView(TemplateView):
    template_name = 'perfil.html'

class PedidosView(TemplateView):
    template_name = 'pedidos.html'

class BaseView(TemplateView):
    template_name = 'Base.html'

class CadView(TemplateView):
    template_name = 'cadastro.html'

class CarView(TemplateView):
    template_name = 'carrinho.html'

class EuroView(TemplateView):
    template_name = 'europa.html'

class FavView(TemplateView):
    template_name = 'favoritos.html'

class RetroView(TemplateView):
    template_name = 'retro.html'

class SacView(TemplateView):
    template_name = 'sac.html'

class SelecView(TemplateView):
    template_name = 'selecoes.html'