from django.contrib import admin

from .models import Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    model = Servico
    list_display = ['nome_servico', 'preco']
    readonly_fields = ['created', 'modified']
