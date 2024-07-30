from django.shortcuts import render,  redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productos.models import Producto
from gestion.models import Stock
from .models import Pedido, Turno
from zonas.models import Zona

def cliente(request):
    productos = Producto.objects.all()
    return render(request, 'cliente/cliente.html', {'productos': productos})

def clienteform(request):
    # Filtrar turnos que tienen menos de 10 pedidos asignados
    turnos = Turno.objects.filter(pedidos_actuales__lt=10)
    medios = Pedido.PAGO_CHOICES
    zonas = Zona.objects.all()
    return render(request, "cliente/form_cliente.html", {"turnos": turnos, "medios": medios, "zonas": zonas})


@csrf_exempt
def crear_pedido(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        masasenpedido=int(data['masas'])
        masasdisponibles=Stock.objects.first()
        print(masasdisponibles)
        if masasenpedido > masasdisponibles.cantidad_masas:
            return JsonResponse({'error': 'No tenemos stock suficiente para tu pedido'}, status=405)
        else:

            horario = None
            if 'horario' in data and data['horario']:
                try:
                    horario = Turno.objects.get(id=data['horario'])
                    horario.pedidos_actuales += 1
                    horario.save()
                except Turno.DoesNotExist:
                    return JsonResponse({'error': 'Horario no válido'}, status=400)
            
            detalles = data['detalles']
            
            # Agregar el nombre de la zona y el costo al final de los detalles si es envío a domicilio
            if data['metodo_entrega'] == 'envio':
                try:
                    zona = Zona.objects.get(id=data['zona_id'])
                    detalles = detalles + f", {zona.nombre_zona}: ${zona.costo}"
                    print(detalles)
                except Zona.DoesNotExist:
                    return JsonResponse({'error': 'Zona no válida'}, status=400)
            
            # Convertir el horario elegido en un string antes de almacenarlo
            horario_str = horario.horario.strftime("%H:%M") if horario else None
            
            pedido = Pedido(
                nombre=data['nombre'],
                telefono=data['telefono'],
                cantidad=data['cantidad'],
                detalles=detalles,
                monto=data['monto'],
                estado='tomado',  # Estado por defecto
                horario=horario_str,
                medio_pago=data['medio_pago'],
                metodo_entrega=data['metodo_entrega'],
                direccion=data['direccion'] if data['metodo_entrega'] == 'envio' else '',
                observaciones=data['observaciones']
            )
            pedido.save()

            masasdisponibles.cantidad_masas -= masasenpedido
            masasdisponibles.save()

            return JsonResponse({'success': 'Pedido creado exitosamente'}, status=200)

    return JsonResponse({'error': 'Método de solicitud no permitido'}, status=405)