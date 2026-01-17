import pytest

from src.classes import Product, Category


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест инициализации продукта"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.quantity == 5

    def test_product_price_getter(self):
        """Тест геттера цены"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)
        assert product.price == 10000.0

    def test_product_price_setter_valid(self):
        """Тест сеттера цены с корректным значением"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)
        product.price = 15000.0
        assert product.price == 15000.0

    def test_product_price_setter_invalid(self, capsys):
        """Тест сеттера цены с некорректным значением (отрицательная)"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)
        product.price = -5000.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 10000.0  # Цена не должна измениться

    def test_product_price_setter_zero(self, capsys):
        """Тест сеттера цены с нулевым значением"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 10000.0  # Цена не должна измениться

    def test_product_price_private_attribute(self):
        """Тест приватности атрибута __price"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)

        # Прямой доступ к __price должен вызывать ошибку
        with pytest.raises(AttributeError):
            _ = product.__price

        # Но доступ через property должен работать
        assert product.price == 10000.0

    def test_new_product_classmethod(self):
        """Тест класс-метода new_product"""
        product_data = {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 50000.0,
            "quantity": 3,
        }
        product = Product.new_product(product_data)

        assert isinstance(product, Product)
        assert product.name == "Ноутбук"
        assert product.description == "Игровой ноутбук"
        assert product.price == 50000.0
        assert product.quantity == 3

    def test_new_product_with_missing_data(self):
        """Тест класс-метода new_product с неполными данными"""
        product_data = {
            "name": "Планшет",
            "price": 15000.0,
            # Нет description и quantity
        }
        product = Product.new_product(product_data)

        assert product.name == "Планшет"
        assert product.price == 15000.0
        assert product.description is None  # get() вернет None если нет ключа
        assert product.quantity is None


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест инициализации категории"""
        category = Category("Электроника", "Техника")
        assert category.name == "Электроника"
        assert category.description == "Техника"

    def test_category_initialization_with_products(self):
        """Тест инициализации категории с товарами"""
        product1 = Product("Телефон", "Смартфон", 10000.0, 5)
        product2 = Product("Ноутбук", "Игровой", 50000.0, 3)

        category = Category("Электроника", "Техника", [product1, product2])
        assert Category.category_count == 1
        assert Category.product_count == 2

    def test_category_initialization_empty_products(self):
        """Тест инициализации категории с пустым списком товаров"""
        category = Category("Электроника", "Техника", [])
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_count(self):
        """Тест счетчика категорий"""
        assert Category.category_count == 0

        category1 = Category("Категория 1", "Описание 1")
        assert Category.category_count == 1

        category2 = Category("Категория 2", "Описание 2")
        assert Category.category_count == 2

    def test_product_count_initialization(self):
        """Тест счетчика товаров при инициализации"""
        product1 = Product("Телефон", "Смартфон", 10000.0, 5)
        product2 = Product("Ноутбук", "Игровой", 50000.0, 3)

        Category("Электроника", "Техника", [product1, product2])
        assert Category.product_count == 2

    def test_private_products_attribute(self):
        """Тест приватности атрибута __products"""
        category = Category("Электроника", "Техника")

        # Прямой доступ к __products должен вызывать ошибку
        with pytest.raises(AttributeError):
            _ = category.__products

    def test_add_product_method(self):
        """Тест метода add_product"""
        category = Category("Электроника", "Техника")
        product = Product("Телефон", "Смартфон", 10000.0, 5)

        initial_count = Category.product_count
        category.add_product(product)

        # Проверяем, что счетчик увеличился
        assert Category.product_count == initial_count + 1

    def test_add_multiple_products(self):
        """Тест добавления нескольких товаров"""
        category = Category("Электроника", "Техника")
        product1 = Product("Телефон", "Смартфон", 10000.0, 5)
        product2 = Product("Ноутбук", "Игровой", 50000.0, 3)

        category.add_product(product1)
        category.add_product(product2)

        assert Category.product_count == 2

    def test_products_property_getter(self):
        """Тест геттера products"""
        product1 = Product("Телефон", "Смартфон", 10000.0, 5)
        product2 = Product("Ноутбук", "Игровой", 50000.0, 3)

        category = Category("Электроника", "Техника", [product1, product2])

        products_string = category.products

        # Проверяем формат вывода
        assert "Телефон, 10000.0 руб. Остаток: 5 шт.\n" in products_string
        assert "Ноутбук, 50000.0 руб. Остаток: 3 шт.\n" in products_string
        # Проверяем, что строки разделены переносом
        lines = products_string.strip().split("\n")
        assert len(lines) == 2

    def test_products_property_empty_category(self):
        """Тест геттера products для пустой категории"""
        category = Category("Электроника", "Техника")
        assert category.products == ""

    def test_products_property_after_add_product(self):
        """Тест геттера products после добавления товаров"""
        category = Category("Электроника", "Техника")
        product = Product("Телефон", "Смартфон", 10000.0, 5)

        category.add_product(product)

        products_string = category.products
        assert "Телефон, 10000.0 руб. Остаток: 5 шт.\n" == products_string

    def test_product_count_with_add_product(self):
        """Тест счетчика товаров при использовании add_product"""
        category = Category("Электроника", "Техника")
        assert Category.product_count == 0

        product1 = Product("Телефон", "Смартфон", 10000.0, 5)
        category.add_product(product1)
        assert Category.product_count == 1

        product2 = Product("Ноутбук", "Игровой", 50000.0, 3)
        category.add_product(product2)
        assert Category.product_count == 2


class TestIntegration:
    """Интеграционные тесты для взаимодействия классов"""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_full_workflow(self, capsys):
        """Тест полного рабочего процесса"""
        # Создаем товары
        product1 = Product("Телефон", "Смартфон", 10000.0, 5)

        # Создаем товар через класс-метод
        product_data = {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 50000.0,
            "quantity": 3,
        }
        product2 = Product.new_product(product_data)

        # Создаем категорию
        category = Category("Электроника", "Техника")

        # Добавляем товары
        category.add_product(product1)
        category.add_product(product2)

        # Проверяем вывод через геттер
        products_list = category.products
        assert "Телефон, 10000.0 руб. Остаток: 5 шт.\n" in products_list
        assert "Ноутбук, 50000.0 руб. Остаток: 3 шт.\n" in products_list

        # Тестируем сеттер цены
        product1.price = 12000.0
        assert product1.price == 12000.0

        # Тестируем некорректную цену
        product1.price = -1000.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product1.price == 12000.0  # Цена не изменилась

        # Проверяем счетчики
        assert Category.category_count == 1
        assert Category.product_count == 2

    def test_multiple_categories(self):
        """Тест работы с несколькими категориями"""
        # Создаем товары
        product1 = Product("Телефон", "Смартфон", 10000.0, 5)
        product2 = Product("Ноутбук", "Игровой", 50000.0, 3)
        product3 = Product("Планшет", "Графический", 15000.0, 7)

        # Создаем категории
        category1 = Category("Смартфоны", "Мобильные телефоны", [product1])
        category2 = Category("Компьютеры", "ПК и ноутбуки", [product2, product3])

        # Проверяем счетчики
        assert Category.category_count == 2
        assert Category.product_count == 3

        # Проверяем вывод каждой категории
        assert "Телефон, 10000.0 руб. Остаток: 5 шт.\n" in category1.products
        assert "Ноутбук, 50000.0 руб. Остаток: 3 шт.\n" in category2.products
        assert "Планшет, 15000.0 руб. Остаток: 7 шт.\n" in category2.products


# Дополнительные тесты для edge cases
class TestEdgeCases:
    """Тесты для крайних случаев"""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_product_with_zero_quantity(self):
        """Тест товара с нулевым количеством"""
        product = Product("Телефон", "Смартфон", 10000.0, 0)
        assert product.quantity == 0

        category = Category("Электроника", "Техника", [product])
        assert "Телефон, 10000.0 руб. Остаток: 0 шт.\n" in category.products

    def test_category_with_same_product_twice(self):
        """Тест добавления одного товара дважды в категорию"""
        category = Category("Электроника", "Техника")
        product = Product("Телефон", "Смартфон", 10000.0, 5)

        category.add_product(product)
        category.add_product(product)  # Добавляем тот же товар еще раз

        assert Category.product_count == 2

        # В выводе будет две одинаковые строки
        products_string = category.products
        lines = products_string.strip().split("\n")
        assert len(lines) == 2
        assert all("Телефон, 10000.0 руб. Остаток: 5 шт." in line for line in lines)

    def test_product_price_very_small_positive(self):
        """Тест установки очень маленькой положительной цены"""
        product = Product("Телефон", "Смартфон", 10000.0, 5)
        product.price = 0.01  # Очень маленькая, но положительная цена
        assert product.price == 0.01
