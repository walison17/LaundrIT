from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import administrador_usuario, administrador_servico, historico_usuario, \
    administrador_roupa, historico_admin, status_admin, status_usuario, \
    status_comentar_status_pedido, buscar_por_status, historico_admin_pedido_ativo, \
    historico_admin_pedido_finalizado, historico_admin_pedido_cancelado,\
    historico_usuario_pedido_ativo, historico_usuario_pedido_finalizado, \
    historico_usuario_pedido_cancelado  




urlpatterns = [
    path('administrador_usuario/', administrador_usuario, name='administrador_usuario'),
    path('administrador_roupa/', administrador_roupa, name='administrador_roupa'),
    path('administrador_servico/', administrador_servico, name='administrador_servico'),
    path('historico_admin/', historico_admin, name='historico_admin'),
    path('historico_admin_pedido_ativo/', historico_admin_pedido_ativo, name="historico_admin_pedido_ativo"),
    path('historico_admin_pedido_finalizado/', historico_admin_pedido_finalizado, name="historico_admin_pedido_finalizado"),
    path('historico_admin_pedido_cancelado/', historico_admin_pedido_cancelado, name="historico_admin_pedido_cancelado" ),
    path('historico_usuario/', historico_usuario, name='historico_usuario'),
    path('historico_usuario_pedido_ativo/', historico_usuario_pedido_ativo, name="historico_usuario_pedido_ativo"),
    path('historico_usuario_pedido_finalizado/', historico_usuario_pedido_finalizado, name="historico_usuario_pedido_finalizado"),
    path('historico_usuario_pedido_cancelado/', historico_usuario_pedido_cancelado, name="historico_usuario_pedido_cancelado" ),
    path('status_admin/', status_admin, name='status_admin'),
    path('status_usuario/', status_usuario, name='status_usuario'),
    path('status_comentar_status_pedido/<int:id>/', status_comentar_status_pedido, name='status_comentar_status_pedido'),
    path('buscar_por_status/', buscar_por_status, name='buscar_por_status')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
