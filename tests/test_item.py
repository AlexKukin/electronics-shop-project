from src.item import Item
import pytest

"""Тесты для модуля item."""


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


# Тест расчета общей стоимости одинаковых товаров.
@pytest.mark.parametrize('item, excepted',
    [("item1", 200000),
     ("item2", 100000)]
)
def test_total_price(item, excepted, request):
    item = request.getfixturevalue(item)
    assert item.calculate_total_price() == excepted


# Тест расчета скидки на 1шт товара
@pytest.mark.parametrize('item, excepted',
    [("item1", 8000),
     ("item2", 16000)]# в исходном коде тут было ошибочно 20_000
)
def test_discount(item, excepted, request):
    item = request.getfixturevalue(item)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == excepted


# Тест формирования списка со всеми созданными товарами на уровне класса Item
@pytest.mark.parametrize('item',
    ['item1',
     'item2']
)
def test_fill_all(item, request):
    item = request.getfixturevalue(item)
    # Список не пуст
    assert any(Item.all) is True
    # Созданные элементы попали в список
    assert item in Item.all



