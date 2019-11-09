from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import login, my_logout, home, cadastro

urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='my_logout'),
    path('cadastro/', cadastro, name='cadastro'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

