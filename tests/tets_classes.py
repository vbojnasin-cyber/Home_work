import pytest
from src.classes import Product, Category  # Замените 'your_module' на имя вашего файла с классами


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category(product):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product])


def test_product_initialization(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products) == 1
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"


def test_product_count():
    initial_count = Category.product_count
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию и добавляем продукты
    category = Category("Смартфоны", "Смартфоны", [product1, product2])

    # Проверяем количество продуктов
    assert Category.product_count == initial_count + 2


def test_category_count():
    initial_count = Category.category_count
    category1 = Category("Смартфоны", "Смартфоны")
    category2 = Category("Телевизоры", "Телевизоры")

    # Проверяем количество категорий
    assert Category.category_count == initial_count + 2
