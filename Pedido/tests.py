from django.test import TestCase
from decimal import Decimal

from model_bakery import baker

from .models import Pedido, Item


class TestPedidoModel(TestCase):
    def setUp(self):
        self.order = baker.make(Pedido)

    def test_calculate_amount(self):
        item1 = baker.make(Item, quantity=2, service__price=Decimal(1.5))
        item2 = baker.make(Item, quantity=1, service__price=Decimal(1.2))
        self.order.items.set([item1, item2])

        self.assertTrue(
            self.order.calculate_amount().compare(Decimal(4.2))
        )


class TestItemModel(TestCase):
    def test_set_unit_price_on_save(self):
        servico = baker.make('Servico.servico')
        item = baker.make(Item, quantity=2, servico=servico)

        self.assertEqual(item.preco_unitario, servico.preco)