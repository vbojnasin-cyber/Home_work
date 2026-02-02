import pytest
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def product():
    return Product(
        name="Яблоки",
        description="Фрукты",
        price=100,
        quantity=300
    )


@pytest.fixture
def smartphone():
    return Smartphone(
        name="iPhone 15",
        description="Смартфон Apple",
        price=89990,
        quantity=50,
        efficiency="A16 Bionic",
        model="15 Pro",
        memory=256,
        color="Титановый"
    )


@pytest.fixture
def lawngrass():
    return LawnGrass(
        name="Газонная трава Премиум",
        description="Трава для элитного газона",
        price=2500,
        quantity=150,
        country="Германия",
        germination_period=10,
        color="Изумрудный"
    )


def test_new_product(product):
    """Тест создания базового продукта"""
    assert product.quantity == 300
    assert product.price == 100
    assert product.name == "Яблоки"
    assert product.description == "Фрукты"
    assert product._Product__price == 100


def test_price_setter(product):
    """Тест сеттера цены"""
    product.price = 150
    assert product.price == 150


def test_price_setter_negative(product, capsys):
    """Тест сеттера с отрицательной ценой"""
    original_price = product.price
    product.price = -50

    # Проверяем что цена не изменилась
    assert product.price == original_price

    # Проверяем вывод сообщения об ошибке
    captured = capsys.readouterr()
    assert "Цена не может быть меньше 0" in captured.out


def test_product_add_same_type(product):
    """Тест сложения одинаковых типов продуктов"""
    product_2 = Product("Груши", "Фрукты", 200, 50)
    result = product + product_2
    assert result == 40000  # 100*300 + 200*50


def test_product_add_different_types(product, smartphone, lawngrass):
    """Тест что нельзя складывать разные типы продуктов"""
    with pytest.raises(TypeError, match="Нельзя складывать товары разных категорий"):
        product + smartphone

    with pytest.raises(TypeError, match="Нельзя складывать товары разных категорий"):
        smartphone + lawngrass

    with pytest.raises(TypeError, match="Нельзя складывать товары разных категорий"):
        lawngrass + product


def test_new_product_from_dict():
    """Тест создания продукта из словаря"""
    product_data = {
        "name": "banana",
        "description": "fruit",
        "price": 400,
        "quantity": 100
    }
    product_4 = Product.new_product(product_data)
    assert product_4.name == "banana"
    assert product_4.description == "fruit"
    assert product_4.price == 400
    assert product_4.quantity == 100  # ЗАКРЫВАЮЩАЯ СКОБКА ДОБАВЛЕНА!


def test_smartphone_creation(smartphone):
    """Тест создания смартфона"""
    assert smartphone.name == "iPhone 15"
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Титановый"
    assert smartphone.efficiency == "A16 Bionic"


def test_lawngrass_creation(lawngrass):
    """Тест создания газонной травы"""
    assert lawngrass.name == "Газонная трава Премиум"
    assert lawngrass.country == "Германия"
    assert lawngrass.germination_period == 10
    assert lawngrass.color == "Изумрудный"


def test_inheritance():
    """Тест наследования"""
    smartphone = Smartphone("Тест", "Описание", 100, 10, "a", "m", 128, "black")
    lawngrass = LawnGrass("Тест", "Описание", 50, 20, "RU", 14, "green")

    # Проверяем что оба являются Product
    assert isinstance(smartphone, Product)
    assert isinstance(lawngrass, Product)

    # Проверяем конкретные типы
    assert type(smartphone) == Smartphone
    assert type(lawngrass) == LawnGrass


def test_str_methods():
    """Тест строковых представлений"""
    product = Product("Яблоки", "Фрукты", 100, 300)
    smartphone = Smartphone("iPhone", "Смартфон", 1000, 10, "A16", "15", 256, "Черный")
    lawngrass = LawnGrass("Трава", "Газонная", 500, 100, "Россия", 14, "Зеленый")

    # Проверяем что __str__ работает
    assert "Яблоки" in str(product)
    assert "100" in str(product)

    assert "iPhone" in str(smartphone)
    assert "15" in str(smartphone)  # модель
    assert "256" in str(smartphone)  # память

    assert "Трава" in str(lawngrass)
    assert "Россия" in str(lawngrass)
    assert "14" in str(lawngrass)  # срок прорастания


def test_add_only_same_class():
    """Тест что можно складывать только одинаковые классы"""
    phone1 = Smartphone("Тел1", "Описание", 100, 5, "a", "m", 64, "black")
    phone2 = Smartphone("Тел2", "Описание", 200, 3, "b", "n", 128, "white")

    # Можно складывать одинаковые классы
    result = phone1 + phone2
    assert result == (100 * 5 + 200 * 3)

    # Нельзя складывать с другим классом
    product = Product("Продукт", "Описание", 50, 10)
    with pytest.raises(TypeError):
        phone1 + product


if __name__ == "__main__":
    pytest.main([__file__, "-v"])