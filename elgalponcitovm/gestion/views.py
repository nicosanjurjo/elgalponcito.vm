from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from cliente.models import Pedido, Turno
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
        if data == 0:
            Turno.objects.all().update(pedidos_actuales=0)
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

@csrf_exempt
def obtener_pedido(request):
    if request.method == 'GET':
        pedido_id = request.GET.get('id')
        pedido = get_object_or_404(Pedido, id=pedido_id)
        pedido_data = {
            'id': pedido.id,
            'ingreso': pedido.created_at,
            'nombre': pedido.nombre,
            'telefono': pedido.telefono,
            'cantidad': pedido.cantidad,
            'detalles': pedido.detalles,
            'monto': pedido.monto,
            'medio': pedido.medio_pago,
            'horario': pedido.horario,
            'direccion': pedido.direccion,
            'observaciones': pedido.observaciones,
            'estado': pedido.estado,
        }
        return JsonResponse(pedido_data)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_pedido(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('id')
        nuevo_estado = request.POST.get('estado')
        pedido = get_object_or_404(Pedido, id=pedido_id)
        pedido.estado = nuevo_estado
        pedido.save()
        return JsonResponse({'success': 'Pedido actualizado correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)