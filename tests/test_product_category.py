import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class TestProduct:
    """Тесты для класса Product"""

    def test_create_product_with_zero_quantity_raises_error(self):
        """Тест: создание товара с нулевым количеством вызывает исключение"""
        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            Product("Тестовый товар", "Описание", 100, 0)

    def test_create_product_with_positive_quantity_success(self):
        """Тест: создание товара с положительным количеством проходит успешно"""
        product = Product("Тестовый товар", "Описание", 100, 10)
        assert product.name == "Тестовый товар"
        assert product.quantity == 10

    def test_create_lawn_grass_with_zero_quantity_raises_error(self):
        """Тест: создание LawnGrass с нулевым количеством вызывает исключение"""
        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            LawnGrass("Трава", "Газонная трава", 50, 0, "Россия", 30, "зеленый")

    def test_create_smartphone_with_zero_quantity_raises_error(self):
        """Тест: создание Smartphone с нулевым количеством вызывает исклющение"""
        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            Smartphone("Phone", "Смартфон", 500, 0, "высокая", "X10", 128, "черный")


class TestCategory:
    """Тесты для класса Category"""

    def test_average_price_with_products(self):
        """Тест: расчет средней цены для категории с товарами"""
        # Создаем категорию с товарами
        product1 = Product("Товар1", "Описание1", 100, 5)
        product2 = Product("Товар2", "Описание2", 200, 3)
        product3 = Product("Товар3", "Описание3", 300, 2)

        category = Category(
            "Тестовая категория", "Описание", [product1, product2, product3]
        )

        # Средняя цена: (100 + 200 + 300) / 3 = 200
        assert category.average_price() == 200

    def test_average_price_with_single_product(self):
        """Тест: расчет средней цены для категории с одним товаром"""
        product = Product("Товар1", "Описание1", 150, 10)
        category = Category("Тестовая категория", "Описание", [product])

        assert category.average_price() == 150

    def test_average_price_empty_category(self):
        """Тест: расчет средней цены для пустой категории"""
        category = Category("Пустая категория", "Описание")

        # Должен вернуть 0 при пустой категории
        assert category.average_price() == 0

    def test_average_price_after_adding_products(self):
        """Тест: расчет средней цены после добавления товаров"""
        category = Category("Тестовая категория", "Описание")

        # Сначала категория пустая
        assert category.average_price() == 0

        # Добавляем товары
        product1 = Product("Товар1", "Описание1", 100, 5)
        product2 = Product("Товар2", "Описание2", 300, 3)
        category.add_product(product1)
        category.add_product(product2)

        # Средняя цена: (100 + 300) / 2 = 200
        assert category.average_price() == 200

    def test_average_price_with_mixed_products(self):
        """Тест: расчет средней цены с товарами разных типов"""
        # Создаем товары разных типов
        product = Product("Товар", "Описание", 100, 5)
        lawn_grass = LawnGrass("Трава", "Газонная", 50, 10, "Россия", 30, "зеленый")
        smartphone = Smartphone(
            "Phone", "Смартфон", 500, 3, "высокая", "X10", 128, "черный"
        )

        category = Category(
            "Смешанная категория", "Описание", [product, lawn_grass, smartphone]
        )

        # Средняя цена: (100 + 50 + 500) / 3 ≈ 216.67
        expected_average = (100 + 50 + 500) / 3
        assert abs(category.average_price() - expected_average) < 0.01

    def test_old_tests_still_work(self):
        """Тест: проверка, что старые тесты все еще работают"""
        # Создание категории
        category = Category("Электроника", "Гаджеты и устройства")
        assert category.name == "Электроника"
        assert category.description == "Гаджеты и устройства"

        # Создание и добавление товара
        product = Product("Телефон", "Смартфон", 20000, 5)
        category.add_product(product)

        # Проверка строкового представления
        assert str(category) == "Электроника, количество продуктов: 5 шт."

        # Проверка геттера products
        assert "Телефон" in category.products
        assert "20000 руб." in category.products

        # Проверка счетчиков
        assert Category.category_count > 0
        assert Category.product_count > 0


if __name__ == "__main__":
    # Запуск тестов
    pytest.main([__file__, "-v"])
