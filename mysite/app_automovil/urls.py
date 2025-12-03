from django.urls import path
from . import views

app_name = 'app_automovil'

urlpatterns = [
    # Página principal
    path('', views.inicio, name='inicio'),
    
    # CRUD para Mecánicos
    path('mecanicos/', views.inicio_mecanicos, name='inicio_mecanicos'),
    path('mecanicos/agregar/', views.agregar_mecanico, name='agregar_mecanico'),
    path('mecanicos/actualizar/<int:id_mecanico>/', views.actualizar_mecanico, name='actualizar_mecanico'),
    path('mecanicos/borrar/<int:id_mecanico>/', views.borrar_mecanico, name='borrar_mecanico'),
    
    # CRUD para Clientes
    path('clientes/', views.inicio_clientes, name='inicio_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
    
    # CRUD para Vehículos
    path('vehiculos/', views.inicio_vehiculos, name='inicio_vehiculos'),
    path('vehiculos/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculos/actualizar/<int:id_vehiculo>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    path('vehiculos/borrar/<int:id_vehiculo>/', views.borrar_vehiculo, name='borrar_vehiculo'),
    
    # CRUD para Órdenes de Reparación
    path('ordenes/', views.inicio_ordenes, name='inicio_ordenes'),
    path('ordenes/agregar/', views.agregar_orden, name='agregar_orden'),
    path('ordenes/actualizar/<int:id_orden>/', views.actualizar_orden, name='actualizar_orden'),
    path('ordenes/borrar/<int:id_orden>/', views.borrar_orden, name='borrar_orden'),
    
    # CRUD para Repuestos
    path('repuestos/', views.inicio_repuestos, name='inicio_repuestos'),
    path('repuestos/agregar/', views.agregar_repuesto, name='agregar_repuesto'),
    path('repuestos/actualizar/<int:id_repuesto>/', views.actualizar_repuesto, name='actualizar_repuesto'),
    path('repuestos/borrar/<int:id_repuesto>/', views.borrar_repuesto, name='borrar_repuesto'),
    
    # CRUD para Detalles de Reparación
    path('detalles/', views.inicio_detalles, name='inicio_detalles'),
    path('detalles/agregar/', views.agregar_detalle, name='agregar_detalle'),
    path('detalles/actualizar/<int:id_detalle_rep>/', views.actualizar_detalle, name='actualizar_detalle'),
    path('detalles/borrar/<int:id_detalle_rep>/', views.borrar_detalle, name='borrar_detalle'),
    
    # CRUD para Facturas
    path('facturas/', views.inicio_facturas, name='inicio_facturas'),
    path('facturas/agregar/', views.agregar_factura, name='agregar_factura'),
    path('facturas/actualizar/<int:id_factura>/', views.actualizar_factura, name='actualizar_factura'),
    path('facturas/borrar/<int:id_factura>/', views.borrar_factura, name='borrar_factura'),
]