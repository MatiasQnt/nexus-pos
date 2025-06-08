from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
#Es el prefijo de la URL↓          ↓ La lógica que ejecutará
router.register(r'products', ProductViewSet, basename='products') # Nombre de la API

urlpatterns = router.urls # No me quedo del todo claro para que sirve esto
