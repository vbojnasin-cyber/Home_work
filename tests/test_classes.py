import pytest
from src.classes import Product, Category


class TestProduct:
    def test_product_initialization(self):
        """Проверка корректности инициализации объектов класса Product"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 10000.0
        assert product.quantity == 5


class TestCategory:
    def test_category_initialization(self):
        """Проверка корректности инициализации объектов класса Category"""
        category = Category("Смартфоны", "Мобильные устройства", [])

        assert category.name == "Смартфоны"
        assert category.description == "Мобильные устройства"
        assert category.products == []
        assert len(category.products) == 0

    def test_category_with_products(self):
        """Проверка категории с товарами"""
        product1 = Product("Телефон1", "Описание1", 10000.0, 5)
        product2 = Product("Телефон2", "Описание2", 20000.0, 3)

        category = Category("Телефоны", "Мобильные", [product1, product2])

        assert category.name == "Телефоны"
        assert category.description == "Мобильные"
        assert len(category.products) == 2
        assert category.products[0].name == "Телефон1"
        assert category.products[1].name == "Телефон2"

    def test_category_count(self):
        """Подсчет количества категорий"""
        # Сбрасываем счетчик перед тестом
        Category.category_count = 0

        category1 = Category("Категория1", "Описание1", [])
        assert Category.category_count == 1

        category2 = Category("Категория2", "Описание2", [])
        assert Category.category_count == 2

        category3 = Category("Категория3", "Описание3", [])
        assert Category.category_count == 3

    def test_product_count(self):
        """Подсчет количества товаров"""
        # Сбрасываем счетчик перед тестом
        Category.product_count = 0
        Category.category_count = 0

        product1 = Product("Товар1", "Описание1", 100.0, 5)
        product2 = Product("Товар2", "Описание2", 200.0, 3)
        product3 = Product("Товар3", "Описание3", 300.0, 7)

        # Создаем категории с товарами
        category1 = Category("Кат1", "Описание", [product1, product2])
        assert Category.product_count == 2

        category2 = Category("Кат2", "Описание", [product3])
        assert Category.product_count == 3

        # Категория без товаров не должна увеличивать счетчик товаров
        category3 = Category("Кат3", "Описание", [])
        assert Category.product_count == 3  # остается 3

        # Категория с существующими товарами (дубликаты считаются отдельно)
        category4 = Category("Кат4", "Описание", [product1, product2, product3])
        assert Category.product_count == 6  # 3 + 3 = 6

    def test_multiple_categories_product_count(self):
        """Тест подсчета товаров при нескольких категориях"""
        Category.product_count = 0
        Category.category_count = 0

        # Создаем несколько товаров
        products = [
            Product(f"Товар{i}", f"Описание{i}", 100.0 * i, i)
            for i in range(1, 6)
        ]

        # Создаем категории с разным количеством товаров
        category1 = Category("Кат1", "Описание", products[:2])  # 2 товара
        category2 = Category("Кат2", "Описание", products[2:])  # 3 товара

        assert Category.category_count == 2
        assert Category.product_count == 5