from django.contrib import admin

from .models import Pedido, Item


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
            form.instance.amount = form.instance.calculate_amount()
            form.save()
