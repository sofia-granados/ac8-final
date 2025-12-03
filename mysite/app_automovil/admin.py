from django.contrib import admin
from .models import (
    Cliente_Taller, Vehiculo_Taller, Mecanico, 
    Orden_Reparacion, Repuesto, Detalle_Reparacion, Factura_Taller
)

admin.site.register(Cliente_Taller)
admin.site.register(Vehiculo_Taller)
admin.site.register(Mecanico)
admin.site.register(Orden_Reparacion)
admin.site.register(Repuesto)
admin.site.register(Detalle_Reparacion)
admin.site.register(Factura_Taller)