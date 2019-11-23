from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import login, home, cadastro, alterar_perfil

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('alterar-perfil/', alterar_perfil, name="alterar_perfil")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

