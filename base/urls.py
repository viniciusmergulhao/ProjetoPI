from django.urls import path
from .views import HomeView, PerfilView, CadView, LoginView, PedidosView, BaseView, CarView, EuroView, FavView, RetroView, SacView, SelecView

urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('cadastro/', CadView.as_view()),
    path('perfil/', PerfilView.as_view()),
    path('login/', LoginView.as_view()),
    path('pedidos/', PedidosView.as_view()),
    path('', BaseView.as_view(), name = 'base'),
    path('carrinho/', CarView.as_view()),
    path('europeias/', EuroView.as_view(), name = 'euro'),
    path('favoritos/', FavView.as_view()),
    path('retro/', RetroView.as_view(), name = 'retro'),
    path('sac/', SacView.as_view()),
    path('selecoes/', SelecView.as_view(), name = 'selec'),

]
