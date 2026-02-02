import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    Category.category_count = 0
    Category.product_count = 0
    return Category("Тестовая категория", "Описание категории")


@pytest.fixture
def smartphone():
    return Smartphone(
        name="Тестовый смартфон",
        description="Описание",
        price=1000,
        quantity=10,
        efficiency="Быстрый",
        model="Модель X",
        memory=128,
        color="Черный"
    )


@pytest.fixture
def lawngrass():
    return LawnGrass(
        name="Тестовая трава",
        description="Описание",
        price=500,
        quantity=20,
        country="Россия",
        germination_period=14,
        color="Зеленый"
    )


class TestCategoryUpdated:
    """Обновленные тесты для Category с новой функциональностью"""

    def test_add_smartphone_to_category(self, empty_category, smartphone):
        """Тест: добавление смартфона в категорию"""
        empty_category.add_product(smartphone)
        assert len(empty_category._Category__products) == 1
        assert empty_category._Category__products[0] == smartphone

    def test_add_lawngrass_to_category(self, empty_category, lawngrass):
        """Тест: добавление газонной травы в категорию"""
        empty_category.add_product(lawngrass)
        assert len(empty_category._Category__products) == 1
        assert empty_category._Category__products[0] == lawngrass

    def test_add_mixed_products_to_category(self, empty_category, smartphone, lawngrass):
        """Тест: добавление разных типов продуктов в одну категорию"""
        empty_category.add_product(smartphone)
        empty_category.add_product(lawngrass)

        assert len(empty_category._Category__products) == 2
        assert smartphone in empty_category._Category__products
        assert lawngrass in empty_category._Category__products

    def test_add_non_product_to_category(self, empty_category):
        """Тест: нельзя добавить не-Product объект"""
        with pytest.raises(TypeError) as exc_info:
            empty_category.add_product("не продукт")

        assert "Можно добавлять только объекты класса Product" in str(exc_info.value)

        with pytest.raises(TypeError):
            empty_category.add_product(123)

        with pytest.raises(TypeError):
            empty_category.add_product(None)

    def test_category_str_with_mixed_products(self, empty_category, smartphone, lawngrass):
        """Тест: строковое представление с разными продуктами"""
        empty_category.add_product(smartphone)  # quantity=10
        empty_category.add_product(lawngrass)  # quantity=20

        result = str(empty_category)
        assert "количество продуктов: 30" in result  # 10 + 20

    def test_products_property_with_inherited_classes(self, empty_category, smartphone, lawngrass):
        """Тест: property products с наследованными классами"""
        empty_category.add_product(smartphone)
        empty_category.add_product(lawngrass)

        products_str = empty_category.products

        # Проверяем, что строки содержат информацию о продуктах
        assert "Тестовый смартфон" in products_str
        assert "Модель X" in products_str  # из smartphone.__str__
        assert "Тестовая трава" in products_str
        assert "Россия" in products_str  # из lawngrass.__str__

    def test_category_counters_with_inheritance(self):
        """Тест счетчиков с наследованными классами"""
        Category.category_count = 0
        Category.product_count = 0

        cat = Category("Категория", "Описание")
        assert Category.category_count == 1
        assert Category.product_count == 0

        phone = Smartphone("Телефон", "Описание", 100, 5, "a", "m", 64, "black")
        grass = LawnGrass("Трава", "Описание", 50, 10, "RU", 14, "green")

        cat.add_product(phone)
        assert Category.product_count == 1

        cat.add_product(grass)
        assert Category.product_count == 2