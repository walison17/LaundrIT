from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import pedidos_admin, pedidos_usuario, adicionar_item, update_item

urlpatterns = [
    path('pedidios_admin/', pedidos_admin, name='pedidos_admin'),
    path('pedidos_usuario/', pedidos_usuario, name='pedidos_usuario'),
    path('adicionar_item/', adicionar_item, name='adcionar_item'),
    path('update_item/', update_item, name='update_item'),
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
