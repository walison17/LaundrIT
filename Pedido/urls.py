from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import pedidos_admin, pedidos_usuario, adicionar_item, update_item, \
    pedido_comentar_status

urlpatterns = [
    path('pedidios_admin/', pedidos_admin, name='pedidos_admin'),
    path('pedidos_usuario/', pedidos_usuario, name='pedidos_usuario'),
    path('adicionar_item/', adicionar_item, name='adcionar_item'),
    path('update_item/', update_item, name='update_item'),
    path('pedido_comentar_status/<int:id>/', pedido_comentar_status, name='pedido_comentar_status'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
