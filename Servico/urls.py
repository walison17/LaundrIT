from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import pedido_comentar_status, administrador_status, \
    administrador_usuario, administrador_item, administrador_servico 



urlpatterns = [
    path('pedido_comentar_status/<int:id>/', pedido_comentar_status, name='pedido_comentar_status'),
    path('administrador_status/', administrador_status, name='administrador_status'),
    path('administrador_usuario/', administrador_usuario, name='administrador_usuario'),
    path('administrador_item/', administrador_item, name='administrador_item'),
    path('administrador_servico/', administrador_servico, name='administrador_servico'),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
