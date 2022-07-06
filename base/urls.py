from django.urls import path
from .views import HomeView, view_base

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('',view_base),
    #path('home/', view_home),
   # path('about/', view_about),
   # path('contact/', view_contact),
   

]
