from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import (
    Mecanico, Cliente_Taller, Vehiculo_Taller, 
    Orden_Reparacion, Repuesto, Detalle_Reparacion, Factura_Taller
)
from django.utils import timezone

# ========== VISTA INICIAL ==========
def inicio(request):
    total_mecanicos = Mecanico.objects.count()
    total_clientes = Cliente_Taller.objects.count()
    total_vehiculos = Vehiculo_Taller.objects.count()
    total_ordenes = Orden_Reparacion.objects.count()
    total_repuestos = Repuesto.objects.count()
    total_facturas = Factura_Taller.objects.count()
    
    # Órdenes recientes
    ordenes_recientes = Orden_Reparacion.objects.order_by('-fecha_recepcion')[:5]
    
    # Mecánicos disponibles
    mecanicos = Mecanico.objects.all()[:5]
    
    context = {
        'total_mecanicos': total_mecanicos,
        'total_clientes': total_clientes,
        'total_vehiculos': total_vehiculos,
        'total_ordenes': total_ordenes,
        'total_repuestos': total_repuestos,
        'total_facturas': total_facturas,
        'ordenes_recientes': ordenes_recientes,
        'mecanicos': mecanicos,
    }
    return render(request, 'inicio.html', context)

# ========== CRUD MECÁNICOS (Ya hecho) ==========
def inicio_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'mecanico/ver_mecanico.html', {'mecanicos': mecanicos})

def agregar_mecanico(request):
    if request.method == 'POST':
        mecanico = Mecanico(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            especialidad=request.POST['especialidad'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            salario=request.POST['salario'],
            certificado=request.POST['certificado']
        )
        mecanico.save()
        return redirect('app_automovil:inicio_mecanicos')
    return render(request, 'mecanico/agregar_mecanico.html')

def actualizar_mecanico(request, id_mecanico):
    mecanico = get_object_or_404(Mecanico, id_mecanico=id_mecanico)
    if request.method == 'POST':
        mecanico.nombre = request.POST['nombre']
        mecanico.apellido = request.POST['apellido']
        mecanico.especialidad = request.POST['especialidad']
        mecanico.telefono = request.POST['telefono']
        mecanico.email = request.POST['email']
        mecanico.salario = request.POST['salario']
        mecanico.certificado = request.POST['certificado']
        mecanico.save()
        return redirect('app_automovil:inicio_mecanicos')
    return render(request, 'mecanico/actualizar_mecanico.html', {'mecanico': mecanico})

def borrar_mecanico(request, id_mecanico):
    mecanico = get_object_or_404(Mecanico, id_mecanico=id_mecanico)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('app_automovil:inicio_mecanicos')
    return render(request, 'mecanico/borrar_mecanico.html', {'mecanico': mecanico})

# ========== CRUD CLIENTES ==========
def inicio_clientes(request):
    clientes = Cliente_Taller.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        cliente = Cliente_Taller(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            direccion_cliente=request.POST['direccion_cliente'],
            dni=request.POST['dni'],
            preferencia_contacto=request.POST['preferencia_contacto']
        )
        cliente.save()
        return redirect('app_automovil:inicio_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente_Taller, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.direccion_cliente = request.POST['direccion_cliente']
        cliente.dni = request.POST['dni']
        cliente.preferencia_contacto = request.POST['preferencia_contacto']
        cliente.save()
        return redirect('app_automovil:inicio_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente_Taller, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('app_automovil:inicio_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ========== CRUD VEHÍCULOS ==========
def inicio_vehiculos(request):
    vehiculos = Vehiculo_Taller.objects.all()
    return render(request, 'vehiculo/ver_vehiculo.html', {'vehiculos': vehiculos})

def agregar_vehiculo(request):
    clientes = Cliente_Taller.objects.all()
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente_Taller, id_cliente=request.POST['id_cliente'])
        vehiculo = Vehiculo_Taller(
            marca=request.POST['marca'],
            modelo=request.POST['modelo'],
            ano=request.POST['ano'],
            matricula=request.POST['matricula'],
            num_chasis=request.POST['num_chasis'],
            id_cliente=cliente,
            kilometraje_entrada=request.POST['kilometraje_entrada'],
            color=request.POST['color'],
            estado_general=request.POST['estado_general']
        )
        vehiculo.save()
        return redirect('app_automovil:inicio_vehiculos')
    return render(request, 'vehiculo/agregar_vehiculo.html', {'clientes': clientes})

def actualizar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo_Taller, id_vehiculo=id_vehiculo)
    clientes = Cliente_Taller.objects.all()
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente_Taller, id_cliente=request.POST['id_cliente'])
        vehiculo.marca = request.POST['marca']
        vehiculo.modelo = request.POST['modelo']
        vehiculo.ano = request.POST['ano']
        vehiculo.matricula = request.POST['matricula']
        vehiculo.num_chasis = request.POST['num_chasis']
        vehiculo.id_cliente = cliente
        vehiculo.kilometraje_entrada = request.POST['kilometraje_entrada']
        vehiculo.color = request.POST['color']
        vehiculo.estado_general = request.POST['estado_general']
        vehiculo.save()
        return redirect('app_automovil:inicio_vehiculos')
    return render(request, 'vehiculo/actualizar_vehiculo.html', {'vehiculo': vehiculo, 'clientes': clientes})

def borrar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo_Taller, id_vehiculo=id_vehiculo)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('app_automovil:inicio_vehiculos')
    return render(request, 'vehiculo/borrar_vehiculo.html', {'vehiculo': vehiculo})

# ========== CRUD ÓRDENES DE REPARACIÓN ==========
def inicio_ordenes(request):
    ordenes = Orden_Reparacion.objects.all()
    return render(request, 'orden/ver_orden.html', {'ordenes': ordenes})

def agregar_orden(request):
    vehiculos = Vehiculo_Taller.objects.all()
    mecanicos = Mecanico.objects.all()
    if request.method == 'POST':
        vehiculo = get_object_or_404(Vehiculo_Taller, id_vehiculo=request.POST['id_vehiculo'])
        mecanico = get_object_or_404(Mecanico, id_mecanico=request.POST['id_mecanico_asignado'])
        orden = Orden_Reparacion(
            id_vehiculo=vehiculo,
            fecha_salida_estimada=request.POST['fecha_salida_estimada'],
            estado_orden=request.POST['estado_orden'],
            diagnostico_inicial=request.POST['diagnostico_inicial'],
            costo_estimado=request.POST['costo_estimado'],
            id_mecanico_asignado=mecanico,
            observaciones=request.POST['observaciones']
        )
        orden.save()
        return redirect('app_automovil:inicio_ordenes')
    return render(request, 'orden/agregar_orden.html', {'vehiculos': vehiculos, 'mecanicos': mecanicos})

def actualizar_orden(request, id_orden):
    orden = get_object_or_404(Orden_Reparacion, id_orden=id_orden)
    vehiculos = Vehiculo_Taller.objects.all()
    mecanicos = Mecanico.objects.all()
    if request.method == 'POST':
        vehiculo = get_object_or_404(Vehiculo_Taller, id_vehiculo=request.POST['id_vehiculo'])
        mecanico = get_object_or_404(Mecanico, id_mecanico=request.POST['id_mecanico_asignado'])
        orden.id_vehiculo = vehiculo
        orden.fecha_salida_estimada = request.POST['fecha_salida_estimada']
        orden.estado_orden = request.POST['estado_orden']
        orden.diagnostico_inicial = request.POST['diagnostico_inicial']
        orden.costo_estimado = request.POST['costo_estimado']
        orden.id_mecanico_asignado = mecanico
        orden.observaciones = request.POST['observaciones']
        orden.save()
        return redirect('app_automovil:inicio_ordenes')
    return render(request, 'orden/actualizar_orden.html', {
        'orden': orden, 
        'vehiculos': vehiculos, 
        'mecanicos': mecanicos
    })

def borrar_orden(request, id_orden):
    orden = get_object_or_404(Orden_Reparacion, id_orden=id_orden)
    if request.method == 'POST':
        orden.delete()
        return redirect('app_automovil:inicio_ordenes')
    return render(request, 'orden/borrar_orden.html', {'orden': orden})

# ========== CRUD REPUESTOS ==========
def inicio_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'repuesto/ver_repuesto.html', {'repuestos': repuestos})

def agregar_repuesto(request):
    if request.method == 'POST':
        repuesto = Repuesto(
            nombre_repuesto=request.POST['nombre_repuesto'],
            descripcion=request.POST['descripcion'],
            precio_unitario=request.POST['precio_unitario'],
            stock=request.POST['stock'],
            id_proveedor_repuesto=request.POST['id_proveedor_repuesto'],
            num_pieza_fabricante=request.POST['num_pieza_fabricante'],
            compatibilidad_vehiculos=request.POST['compatibilidad_vehiculos']
        )
        repuesto.save()
        return redirect('app_automovil:inicio_repuestos')
    return render(request, 'repuesto/agregar_repuesto.html')

def actualizar_repuesto(request, id_repuesto):
    repuesto = get_object_or_404(Repuesto, id_repuesto=id_repuesto)
    if request.method == 'POST':
        repuesto.nombre_repuesto = request.POST['nombre_repuesto']
        repuesto.descripcion = request.POST['descripcion']
        repuesto.precio_unitario = request.POST['precio_unitario']
        repuesto.stock = request.POST['stock']
        repuesto.id_proveedor_repuesto = request.POST['id_proveedor_repuesto']
        repuesto.num_pieza_fabricante = request.POST['num_pieza_fabricante']
        repuesto.compatibilidad_vehiculos = request.POST['compatibilidad_vehiculos']
        repuesto.save()
        return redirect('app_automovil:inicio_repuestos')
    return render(request, 'repuesto/actualizar_repuesto.html', {'repuesto': repuesto})

def borrar_repuesto(request, id_repuesto):
    repuesto = get_object_or_404(Repuesto, id_repuesto=id_repuesto)
    if request.method == 'POST':
        repuesto.delete()
        return redirect('app_automovil:inicio_repuestos')
    return render(request, 'repuesto/borrar_repuesto.html', {'repuesto': repuesto})

# ========== CRUD DETALLES DE REPARACIÓN ==========
def inicio_detalles(request):
    detalles = Detalle_Reparacion.objects.all()
    return render(request, 'detalle/ver_detalle.html', {'detalles': detalles})

def agregar_detalle(request):
    ordenes = Orden_Reparacion.objects.all()
    repuestos = Repuesto.objects.all()
    
    if request.method == 'POST':
        try:
            orden_id = request.POST.get('id_orden')
            repuesto_id = request.POST.get('id_repuesto')
            
            if not orden_id or not repuesto_id:
                messages.error(request, 'Debe seleccionar una orden y un repuesto')
                return render(request, 'detalle/agregar_detalle.html', {
                    'ordenes': ordenes, 
                    'repuestos': repuestos
                })
            
            orden = get_object_or_404(Orden_Reparacion, id_orden=orden_id)
            repuesto = get_object_or_404(Repuesto, id_repuesto=repuesto_id)
            
            detalle = Detalle_Reparacion(
                id_orden=orden,
                id_repuesto=repuesto,
                cantidad_repuesto=int(request.POST['cantidad_repuesto']),
                precio_repuesto_unitario=float(request.POST['precio_repuesto_unitario']),
                mano_obra_horas=float(request.POST['mano_obra_horas']),
                costo_mano_obra_hora=float(request.POST['costo_mano_obra_hora'])
            )
            
            detalle.save()
            messages.success(request, 'Detalle agregado correctamente')
            return redirect('app_automovil:inicio_detalles')
            
        except Exception as e:
            messages.error(request, f'Error al agregar detalle: {str(e)}')
            return render(request, 'detalle/agregar_detalle.html', {
                'ordenes': ordenes, 
                'repuestos': repuestos
            })
    
    return render(request, 'detalle/agregar_detalle.html', {
        'ordenes': ordenes, 
        'repuestos': repuestos
    })

def actualizar_detalle(request, id_detalle_rep):
    detalle = get_object_or_404(Detalle_Reparacion, id_detalle_rep=id_detalle_rep)
    ordenes = Orden_Reparacion.objects.all()
    repuestos = Repuesto.objects.all()
    if request.method == 'POST':
        orden = get_object_or_404(Orden_Reparacion, id_orden=request.POST['id_orden'])
        repuesto = get_object_or_404(Repuesto, id_repuesto=request.POST['id_repuesto'])
        detalle.id_orden = orden
        detalle.id_repuesto = repuesto
        detalle.cantidad_repuesto = request.POST['cantidad_repuesto']
        detalle.precio_repuesto_unitario = request.POST['precio_repuesto_unitario']
        detalle.mano_obra_horas = request.POST['mano_obra_horas']
        detalle.costo_mano_obra_hora = request.POST['costo_mano_obra_hora']
        detalle.save()
        return redirect('app_automovil:inicio_detalles')
    return render(request, 'detalle/actualizar_detalle.html', {
        'detalle': detalle,
        'ordenes': ordenes,
        'repuestos': repuestos
    })

def borrar_detalle(request, id_detalle_rep):
    detalle = get_object_or_404(Detalle_Reparacion, id_detalle_rep=id_detalle_rep)
    if request.method == 'POST':
        detalle.delete()
        return redirect('app_automovil:inicio_detalles')
    return render(request, 'detalle/borrar_detalle.html', {'detalle': detalle})

# ========== CRUD FACTURAS ==========
def inicio_facturas(request):
    facturas = Factura_Taller.objects.all()
    return render(request, 'factura/ver_factura.html', {'facturas': facturas})

def agregar_factura(request):
    ordenes = Orden_Reparacion.objects.all()
    clientes = Cliente_Taller.objects.all()
    if request.method == 'POST':
        orden = get_object_or_404(Orden_Reparacion, id_orden=request.POST['id_orden'])
        cliente = get_object_or_404(Cliente_Taller, id_cliente=request.POST['id_cliente_factura'])
        factura = Factura_Taller(
            id_orden=orden,
            total_factura=request.POST['total_factura'],
            estado_pago=request.POST['estado_pago'],
            metodo_pago=request.POST['metodo_pago'],
            fecha_vencimiento=request.POST['fecha_vencimiento'],
            id_cliente_factura=cliente,
            iva_aplicado=request.POST['iva_aplicado']
        )
        factura.save()
        return redirect('app_automovil:inicio_facturas')
    return render(request, 'factura/agregar_factura.html', {'ordenes': ordenes, 'clientes': clientes})

def actualizar_factura(request, id_factura):
    factura = get_object_or_404(Factura_Taller, id_factura=id_factura)
    ordenes = Orden_Reparacion.objects.all()
    clientes = Cliente_Taller.objects.all()
    if request.method == 'POST':
        orden = get_object_or_404(Orden_Reparacion, id_orden=request.POST['id_orden'])
        cliente = get_object_or_404(Cliente_Taller, id_cliente=request.POST['id_cliente_factura'])
        factura.id_orden = orden
        factura.total_factura = request.POST['total_factura']
        factura.estado_pago = request.POST['estado_pago']
        factura.metodo_pago = request.POST['metodo_pago']
        factura.fecha_vencimiento = request.POST['fecha_vencimiento']
        factura.id_cliente_factura = cliente
        factura.iva_aplicado = request.POST['iva_aplicado']
        factura.save()
        return redirect('app_automovil:inicio_facturas')
    return render(request, 'factura/actualizar_factura.html', {
        'factura': factura,
        'ordenes': ordenes,
        'clientes': clientes
    })

def borrar_factura(request, id_factura):
    factura = get_object_or_404(Factura_Taller, id_factura=id_factura)
    if request.method == 'POST':
        factura.delete()
        return redirect('app_automovil:inicio_facturas')
    return render(request, 'factura/borrar_factura.html', {'factura': factura})