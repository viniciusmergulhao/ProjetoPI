from django.urls import path 
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'
    )
    #path('home/', view_home),
   # path('about/', view_about),
   # path('contact/', view_contact),
   

]
