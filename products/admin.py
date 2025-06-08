from django.contrib import admin
from .models import Supplier, Category, Product

# Register your models here.

# Le decimos a Django: "Queremos que estos modelos aparezcan en el panel de admin"
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)