from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()            #  Traer todos los objetos de la tabla
    serializer_class = ProductSerializer        #  Decirle con qué clase debe traducirlos

