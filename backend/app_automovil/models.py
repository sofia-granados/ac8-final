from django.db import models

class Cliente_Taller(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    direccion_cliente = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now_add=True)
    preferencia_contacto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Vehiculo_Taller(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    matricula = models.CharField(max_length=20)
    num_chasis = models.CharField(max_length=50)
    id_cliente = models.ForeignKey(Cliente_Taller, on_delete=models.CASCADE, related_name='vehiculos')
    kilometraje_entrada = models.IntegerField()
    color = models.CharField(max_length=20)
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    estado_general = models.TextField()

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.matricula}"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

class Mecanico(models.Model):
    id_mecanico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_contratacion = models.DateField(auto_now_add=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    certificado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

    class Meta:
        verbose_name = "Mecánico"
        verbose_name_plural = "Mecánicos"

class Orden_Reparacion(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    id_orden = models.AutoField(primary_key=True)
    id_vehiculo = models.ForeignKey(Vehiculo_Taller, on_delete=models.CASCADE, related_name='ordenes')
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    fecha_salida_estimada = models.DateField()
    estado_orden = models.CharField(max_length=50, choices=ESTADOS, default='PENDIENTE')
    diagnostico_inicial = models.TextField()
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    id_mecanico_asignado = models.ForeignKey(Mecanico, on_delete=models.CASCADE, related_name='ordenes_asignadas')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Orden #{self.id_orden} - {self.estado_orden}"

    class Meta:
        verbose_name = "Orden de Reparación"
        verbose_name_plural = "Órdenes de Reparación"

class Repuesto(models.Model):
    id_repuesto = models.AutoField(primary_key=True)
    nombre_repuesto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_proveedor_repuesto = models.IntegerField()  # Simplificado para el ejemplo
    num_pieza_fabricante = models.CharField(max_length=50)
    compatibilidad_vehiculos = models.TextField()

    def __str__(self):
        return f"{self.nombre_repuesto} - Stock: {self.stock}"

    class Meta:
        verbose_name = "Repuesto"
        verbose_name_plural = "Repuestos"

class Detalle_Reparacion(models.Model):
    id_detalle_rep = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Orden_Reparacion, on_delete=models.CASCADE, related_name='detalles')
    id_repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE, related_name='detalles')
    cantidad_repuesto = models.IntegerField()
    precio_repuesto_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    mano_obra_horas = models.DecimalField(max_digits=5, decimal_places=2)
    costo_mano_obra_hora = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_item = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        try:
            cantidad = float(self.cantidad_repuesto)
            precio_unitario = float(self.precio_repuesto_unitario)
            horas = float(self.mano_obra_horas)
            costo_hora = float(self.costo_mano_obra_hora)
            
            subtotal = (cantidad * precio_unitario) + (horas * costo_hora)
            self.subtotal_item = subtotal
        except (TypeError, ValueError) as e:
            self.subtotal_item = 0
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle #{self.id_detalle_rep} - Orden #{self.id_orden.id_orden}"

    class Meta:
        verbose_name = "Detalle de Reparación"
        verbose_name_plural = "Detalles de Reparación"

class Factura_Taller(models.Model):
    ESTADOS_PAGO = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    id_factura = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Orden_Reparacion, on_delete=models.CASCADE, related_name='facturas')
    fecha_emision = models.DateField(auto_now_add=True)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50, choices=ESTADOS_PAGO, default='PENDIENTE')
    metodo_pago = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    id_cliente_factura = models.ForeignKey(Cliente_Taller, on_delete=models.CASCADE, related_name='facturas')
    iva_aplicado = models.DecimalField(max_digits=5, decimal_places=2, default=16.0)

    def __str__(self):
        return f"Factura #{self.id_factura} - ${self.total_factura}"

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
