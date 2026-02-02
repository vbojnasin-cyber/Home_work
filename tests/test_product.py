from abc import ABC

import pytest

from src.base_product import BaseProduct
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class TestBaseProduct:
    """Тесты для абстрактного класса BaseProduct"""

    def test_base_product_is_abstract(self):
        """Проверяем, что BaseProduct - абстрактный класс"""
        assert isinstance(BaseProduct, type)
        assert ABC in BaseProduct.__bases__

    def test_cannot_instantiate_base_product(self):
        """Нельзя создать экземпляр абстрактного класса"""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100, 10)


class TestProductInheritance:
    """Тесты наследования от BaseProduct"""

    def test_product_inherits_from_base_product(self):
        """Product должен наследоваться от BaseProduct"""
        assert issubclass(Product, BaseProduct)

    def test_product_implements_abstract_methods(self):
        """Product должен реализовывать все абстрактные методы"""
        # Создаем экземпляр - если методы не реализованы, будет ошибка
        product = Product("Телефон", "Хороший телефон", 10000, 5)

        # Проверяем, что методы существуют
        assert hasattr(product, "__str__")
        assert hasattr(product, "__add__")
        assert hasattr(product, "price")
        assert hasattr(Product, "price") and isinstance(Product.price, property)


class TestSmartphoneAndLawnGrass:
    """Тесты для наследников Product"""

    def test_smartphone_inheritance(self):
        """Smartphone должен наследоваться от Product"""
        assert issubclass(Smartphone, Product)

    def test_lawn_grass_inheritance(self):
        """LawnGrass должен наследоваться от Product"""
        assert issubclass(LawnGrass, Product)

    def test_smartphone_creation(self):
        """Создание смартфона с дополнительными атрибутами"""
        phone = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=50000,
            quantity=10,
            efficiency=95.5,
            model="15 Pro",
            memory=256,
            color="Black",
        )

        assert phone.name == "iPhone"
        assert phone.model == "15 Pro"
        assert phone.memory == 256
        assert phone.color == "Black"

    def test_lawn_grass_creation(self):
        """Создание газонной травы с дополнительными атрибутами"""
        grass = LawnGrass(
            name="Трава газонная",
            description="Для дачи",
            price=1500,
            quantity=50,
            country="Россия",
            germination_period=30,
            color="Зеленый",
        )

        assert grass.name == "Трава газонная"
        assert grass.country == "Россия"
        assert grass.germination_period == 30
        assert grass.color == "Зеленый"


class TestReprMixin:
    """Тесты для миксина ReprMixin"""

    def test_product_has_repr_method(self):
        """Product должен иметь метод __repr__ после добавления миксина"""
        product = Product("Test", "Desc", 100, 10)
        assert hasattr(product, "__repr__")

        # Проверяем, что repr возвращает строку
        repr_str = repr(product)
        assert isinstance(repr_str, str)
        assert product.__class__.__name__ in repr_str

    def test_smartphone_repr(self):
        """Smartphone также должен иметь метод __repr__"""
        phone = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=50000,
            quantity=10,
            efficiency=95.5,
            model="15 Pro",
            memory=256,
            color="Black",
        )

        repr_str = repr(phone)
        assert "Smartphone" in repr_str
        assert "iPhone" in repr_str
        assert "15 Pro" in repr_str

    def test_repr_includes_attributes(self):
        """__repr__ должен включать атрибуты объекта"""
        product = Product("Телевизор", "4K", 30000, 3)
        repr_str = repr(product)

        # Проверяем наличие основных атрибутов в repr
        assert "Телевизор" in repr_str
        assert "4K" in repr_str
        assert "3" in repr_str
        # price может не быть в repr, так как это приватный атрибут
        # но можно проверить через свойство
        assert product.price == 30000


class TestOldTestsStillWork:
    """Тесты для проверки старой функциональности"""

    def test_price_property(self):
        """Тест свойства price"""
        product = Product("Тест", "Описание", 100, 5)

        # Проверяем getter
        assert product.price == 100

        # Проверяем setter с корректным значением
        product.price = 150
        assert product.price == 150

        # Проверяем setter с некорректным значением
        # (должно вывести сообщение в консоль, но не падать)
        product.price = -50
        assert product.price == 150  # Цена не должна измениться

    def test_add_method(self):
        """Тест сложения продуктов"""
        product1 = Product("Товар1", "Описание", 100, 2)  # 100 * 2 = 200
        product2 = Product("Товар2", "Описание", 200, 3)  # 200 * 3 = 600

        # Сложение одинаковых продуктов
        assert product1 + product2 == 800

        # Сложение разных категорий должно вызывать ошибку
        phone = Smartphone("iPhone", "Смартфон", 50000, 1, 95.5, "15 Pro", 256, "Black")

        with pytest.raises(
            TypeError, match="Нельзя складывать товары разных категорий"
        ):
            product1 + phone

    def test_str_method(self):
        """Тест строкового представления"""
        product = Product("Кофе", "Арабика", 500, 10)
        str_repr = str(product)

        assert "Кофе" in str_repr
        assert "500" in str_repr
        assert "10" in str_repr


# Тесты для проверки, что старые тесты все еще работают
def test_all_old_functionality():
    """Интеграционный тест всей старой функциональности"""
    # 1. Создание продуктов
    product = Product("Молоко", "Парное", 80, 50)
    phone = Smartphone(
        name="Samsung",
        description="Флагман",
        price=70000,
        quantity=5,
        efficiency=98.0,
        model="S23 Ultra",
        memory=512,
        color="Gray",
    )
    grass = LawnGrass(
        name="Трава",
        description="Для футбола",
        price=2000,
        quantity=100,
        country="Германия",
        germination_period=25,
        color="Темно-зеленый",
    )

    # 2. Проверка свойств
    assert product.name == "Молоко"
    assert phone.model == "S23 Ultra"
    assert grass.country == "Германия"

    # 3. Проверка методов
    assert isinstance(str(product), str)
    assert isinstance(str(phone), str)
    assert isinstance(str(grass), str)

    # 4. Проверка сложения (только одинаковые типы)
    product2 = Product("Хлеб", "Белый", 50, 30)
    assert product + product2 == (80 * 50 + 50 * 30)

    print("Все тесты старой функциональности прошли успешно!")
