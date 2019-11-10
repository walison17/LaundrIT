from django.contrib import admin

from .models import Pedido, Item, Roupa, Status


class ItemInline(admin.TabularInline):
    model = Item
    readonly_fields = ['preco_unitario']
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    inlines = [ItemInline]
    list_display = ['id', 'status', 'valor_total', 'created']
    readonly_fields = ['valor_total', 'created', 'modified']

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        if not change:
            form.instance.amount = form.instance.calcular_valor()
            form.save()

@admin.register(Roupa)
class Roupa(admin.ModelAdmin):
    model = Roupa
    list_display = ['nome_peca', 'preco']
    readonly_fields = ['created', 'modified']

@admin.register(Status)
class Status(admin.ModelAdmin):
    model = Status
    list_display = ['descricao', 'status_pedido', 'data_postagem']
    

