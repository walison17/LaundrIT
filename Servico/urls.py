from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import pedido_comentar_status, administrador_status, \
    administrador_usuario, administrador_item, administrador_servico, \
    historico_usuario, historico_admin, status_admin, status_usuario, \
    suporte_admin, suporte_usuario    




urlpatterns = [
    path('pedido_comentar_status/<int:id>/', pedido_comentar_status, name='pedido_comentar_status'),
    path('administrador_status/', administrador_status, name='administrador_status'),
    path('administrador_usuario/', administrador_usuario, name='administrador_usuario'),
    path('administrador_item/', administrador_item, name='administrador_item'),
    path('administrador_servico/', administrador_servico, name='administrador_servico'),
    path('historico_admin/', historico_admin, name='historico_admin'),
    path('historico_usuario/', historico_usuario, name='historico_usuario'),
    path('status_admin/', status_admin, name='status_admin'),
    path('status_usuario/', status_usuario, name='status_usuario'),
    path('suporte_admin/', suporte_admin, name='suporte_admin'),
    path('suporte_usuario/', suporte_usuario, name='suporte_usuario')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
