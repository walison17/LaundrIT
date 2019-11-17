from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import login, home, cadastro

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

