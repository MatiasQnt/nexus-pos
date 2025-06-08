from django.db import models

#   Model Proveedor
class Supplier(models.Model):
    # Campos que el usuario llenará
    name = models.CharField(max_length=100, verbose_name="Nombre")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")
    email = models.EmailField(null=True, blank=True, unique=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.name


#   Model Categoría
class Category(models.Model):
    # Campos que el usuario llenará
    name = models.CharField(max_length=250, verbose_name="Nombre")
    description = models.TextField(null=True, blank=True, verbose_name="Descripción")


    class Meta:
        verbose_name= "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.name
    

#   Model Producto
class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name="Nombre")
    sku = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="SKU / Código de Barras")
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Costo")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Venta")
    quantity = models.IntegerField(default=0, verbose_name="Stock Actual")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    # Foreign Keys
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoría")
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Proveedor")



    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.name