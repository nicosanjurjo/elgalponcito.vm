from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from cliente.models import Pedido
from .models import Stock
from django.views.decorators.csrf import csrf_exempt
import json

def gestion(request):
    pedidos = Pedido.objects.all()
    cantidad = Stock.objects.all()
    return render(request, 'gestion/gestion.html', {'pedidos': pedidos, 'cantidad': cantidad})

@csrf_exempt
def establecer_stock(request):
    if request.method == 'POST':
        stock_anterior=Stock.objects.all()
        stock_anterior.delete()
        data = json.loads(request.body.decode('utf-8'))
        stock = Stock(cantidad_masas=data)
        stock.save()
        return JsonResponse({'status': 'success', 'new_stock': stock.cantidad_masas})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def update_stock(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        stock = Stock.objects.first()
        
        if action == 'incrementar':
            stock.cantidad_masas += 1
        elif action == 'decrementar':
            stock.cantidad_masas -= 1
        
        stock.save()
        return JsonResponse({'status': 'success', 'new_stock': stock.cantidad_masas})
    
    return JsonResponse({'status': 'error'}, status=400)