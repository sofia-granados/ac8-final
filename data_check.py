from app_automovil.models import *

# Verificar si hay órdenes
print("Órdenes:", Orden_Reparacion.objects.count())

# Verificar si hay repuestos
print("Repuestos:", Repuesto.objects.count())

# Si no hay datos, crear algunos de prueba
if Orden_Reparacion.objects.count() == 0:
    print("Creando datos de prueba...")
    # Crear un cliente
    cliente = Cliente_Taller.objects.create(
        nombre="Cliente",
        apellido="Prueba",
        telefono="1234567890",
        email="cliente@test.com",
        direccion_cliente="Dirección prueba",
        dni="12345678",
        preferencia_contacto="Email"
    )
    
    # Crear un vehículo
    vehiculo = Vehiculo_Taller.objects.create(
        marca="Toyota",
        modelo="Corolla",
        ano=2020,
        matricula="ABC123",
        num_chasis="CHS123456",
        id_cliente=cliente,
        kilometraje_entrada=50000,
        color="Rojo",
        estado_general="Buen estado"
    )
    
    # Crear un mecánico
    mecanico = Mecanico.objects.create(
        nombre="Mecánico",
        apellido="Prueba",
        especialidad="General",
        telefono="0987654321",
        email="mecanico@test.com",
        salario=1000.00,
        certificado="Certificado prueba"
    )
    
    # Crear una orden
    orden = Orden_Reparacion.objects.create(
        id_vehiculo=vehiculo,
        fecha_salida_estimada="2024-12-31",
        estado_orden="PENDIENTE",
        diagnostico_inicial="Diagnóstico prueba",
        costo_estimado=500.00,
        id_mecanico_asignado=mecanico,
        observaciones="Observaciones prueba"
    )
    
    # Crear un repuesto
    repuesto = Repuesto.objects.create(
        nombre_repuesto="Filtro de aceite",
        descripcion="Filtro de aceite estándar",
        precio_unitario=25.00,
        stock=10,
        id_proveedor_repuesto=1,
        num_pieza_fabricante="FIL-001",
        compatibilidad_vehiculos="Toyota, Honda, Nissan"
    )
    
    print("Datos de prueba creados exitosamente")
