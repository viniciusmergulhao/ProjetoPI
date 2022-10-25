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
  

class CadView(TemplateView):
    template_name = 'cadastro.html'

class LoginView(TemplateView):
    template_name = 'base/pages/login.html'

class PerfilView(TemplateView):
    template_name = 'base/pages/perfil.html'

class PedidosView(TemplateView):
    template_name = 'base/pages/pedidos.html'

class BaseView(TemplateView):
    template_name = 'base/pages/home.html'

class CadView(TemplateView):
    template_name = 'base/pages/cadastro.html'

class CarView(TemplateView):
    template_name = 'base/pages/carrinho.html'

class EuroView(TemplateView):
    template_name = 'base/pages/europa.html'

class FavView(TemplateView):
    template_name = 'base/pages/favoritos.html'

class RetroView(TemplateView):
    template_name = 'base/pages/retro.html'

class SacView(TemplateView):
    template_name = 'base/pages/sac.html'

class SelecView(TemplateView):
    template_name = 'base/pages/selecoes.html'

class TesteView(TemplateView):
    template_name = 'teste.html'

    
    