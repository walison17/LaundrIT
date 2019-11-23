from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import pedidos_admin, pedidos_usuario, adicionar_item, update_item
from .views import pagamento, suporte_admin, suporte_usuario, responder_suporte
from .views import ver_pedido

urlpatterns = [
    path('pedidos_admin/', pedidos_admin, name='pedidos_admin'),
    path('pedidos_usuario/', pedidos_usuario, name='pedidos_usuario'),
    path('adicionar_item/', adicionar_item, name='adcionar_item'),
    path('update_item/', update_item, name='update_item'),
    path('pagamento/', pagamento, name='pagamento'),
    path('suporte_admin/', suporte_admin, name='suporte_admin'),
    path('suporte_usuario/', suporte_usuario, name='suporte_usuario'),
    path('responder_suporte/<int:id>/', responder_suporte, name='responder_suporte'),
    path('ver_pedido/<int:id>/', ver_pedido, name="ver_pedido"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
