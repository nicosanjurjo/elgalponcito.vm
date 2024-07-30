from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.gestion, name='Gestion'),
    path('establecer_stock/', views.establecer_stock, name='establecerStock'),
    path('update_stock/', views.update_stock, name='update_stock')

]